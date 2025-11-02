"""
Patient Controller class for Hospital Management System.
Handles business logic and coordinates between PatientModel and PatientView.
"""

import json
import os
from model.PatientRecord import PatientRecord
from view.PatientView import PatientView
from view.PatientLookupView import PatientLookupView
from view.TreatmentSchedulerView import TreatmentSchedulerView
from view.SortingView import SortingView
from DataStructures.PatientHashTable import PatientHashTable
from DataStructures.TreatmentHeap import TreatmentHeap
from controller.SortingController import SortingController

class PatientController:

    def __init__(self, config_file="patient_config.json"):
        self.patient_table = PatientHashTable()
        self.treatment_heap = TreatmentHeap()
        
        # Enable Debugging
        self.patient_table.set_debug(True)
        self.treatment_heap.set_debug(True)
        
        self.view = PatientView()
        self.patient_lookup_view = PatientLookupView()
        self.treatment_scheduler_view = TreatmentSchedulerView()
        self.sorting_view = SortingView()
        self.config_file = config_file
        self.load_patients_from_config()
        self.sorting_controller = SortingController(self.patient_table, self.treatment_heap)

    def validate_patient_data(self, patient_id, name, age, department, urgency_level, treatment_status):
        try:
            patient_id = int(patient_id)
            if patient_id <= 0:
                raise ValueError("Patient ID must be a positive integer.")
        except ValueError:
            raise ValueError("Patient ID must be a valid integer.")
        
        if not name:
            raise ValueError("Name cannot be empty.")
        
        try:
            urgency_level = int(urgency_level)
            if not (1 <= urgency_level <= 5):
                raise ValueError("Urgency level must be between 1 and 5.")
        except ValueError:
            raise ValueError("Urgency level must be a valid integer between 1 and 5.")

    def add_patient(self):
        try:
            patient_id = self.patient_lookup_view.get_patient_id_input("Enter Patient ID")
            name = self.patient_lookup_view.get_name_input("Enter Patient Name")
            age = self.patient_lookup_view.get_age_input("Enter Patient Age")
            department = self.patient_lookup_view.get_department_input("Enter Department")
            urgency_level = self.patient_lookup_view.get_urgency_level_input("Enter Urgency Level (1-5)")
            treatment_status = self.patient_lookup_view.get_treatment_status_input("Enter Treatment Status")

            # Validate inputs
            self.validate_patient_data(patient_id, name, age, department, urgency_level, treatment_status)

            new_patient = PatientRecord(int(patient_id), name, int(age), department, int(urgency_level), treatment_status)
            self.patient_table.insert(new_patient)
            self.treatment_heap.insert(new_patient)
            self.patient_lookup_view.display_patient_added(patient_id)
        except ValueError as e:
            self.patient_lookup_view.display_error(str(e))

    def search_patient(self):
        patient_id = self.patient_lookup_view.get_patient_id_input("Enter Patient ID to search")
        try:
            patient_id = int(patient_id)
            record = self.patient_table.search(patient_id)
            if record:
                self.patient_lookup_view.display_patient_record(record)
            else:
                self.patient_lookup_view.display_patient_not_found(patient_id)
        except ValueError:
            self.patient_lookup_view.display_error("Patient ID must be a valid integer.")

    def remove_patient(self):
        patient_id = self.patient_lookup_view.get_patient_id_input("Enter Patient ID to remove")
        try:
            patient_id = int(patient_id)
            
            # Remove from hash table
            record = self.patient_table.delete(patient_id)
            if record:
                # Remove from treatment heap
                heap_patient = self.treatment_heap.remove_patient(patient_id)
                if heap_patient:
                    self.patient_lookup_view.display_patient_removed(patient_id)
                else:
                    self.patient_lookup_view.display_patient_removed(patient_id)
            else:
                self.patient_lookup_view.display_patient_not_found(patient_id)
        except ValueError as e:
            self.patient_lookup_view.display_error(f"Invalid input: {e}")
        except Exception as e:
            self.patient_lookup_view.display_error(f"Error removing patient: {e}")

    def load_patients_from_config(self):
        """Load patients from JSON configuration file."""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as file:
                    patients_data = json.load(file)
                    for patient_data in patients_data:
                        patient = PatientRecord(
                            int(patient_data['patient_id']),
                            patient_data['name'],
                            int(patient_data['age']),
                            patient_data['department'],
                            int(patient_data['urgency_level']),
                            patient_data['treatment_status']
                        )
                        self.patient_table.insert(patient)
                        self.treatment_heap.insert(patient)
                print(f"Loaded {len(patients_data)} patients from {self.config_file}")
            else:
                print(f"Configuration file {self.config_file} not found. Starting with empty patient database.")
        except Exception as e:
            print(f"Error loading patients from config: {e}")


    def peek_next_patient(self):
        """Peek at the next patient to be treated without removing them."""
        try:
            next_patient = self.treatment_heap.peek()
            if next_patient:
                priority = self.treatment_heap._calculate_priority(next_patient)
                self.treatment_scheduler_view.display_next_patient(next_patient, priority)
            else:
                self.treatment_scheduler_view.display_queue_empty()
        except Exception as e:
            self.treatment_scheduler_view.display_error(f"Error peeking at next patient: {e}")

    def extract_next_patient(self):
        """Extract and remove the next patient to be treated."""
        try:
            if self.treatment_heap.is_empty():
                self.treatment_scheduler_view.display_queue_empty()
                return None
            
            next_patient = self.treatment_heap.extract_priority()
            self.treatment_scheduler_view.display_patient_extracted(next_patient)
            return next_patient
        except Exception as e:
            self.treatment_scheduler_view.display_error(f"Error extracting next patient: {e}")
            return None

    def display_treatment_queue(self):
        """Display the current treatment queue."""
        try:
            if self.treatment_heap.is_empty():
                self.treatment_scheduler_view.display_queue_empty()
                return
            
            self.treatment_scheduler_view.display_treatment_queue_header()
            self.treatment_heap.display()
        except Exception as e:
            self.treatment_scheduler_view.display_error(f"Error displaying treatment queue: {e}")

    def update_patient_urgency(self):
        """Update a patient's urgency level."""
        try:
            patient_id = self.patient_lookup_view.get_patient_id_input("Enter Patient ID to update")
            patient_id = int(patient_id)
            
            # Check if patient exists
            patient = self.patient_table.search(patient_id)
            if not patient:
                self.patient_lookup_view.display_patient_not_found(patient_id)
                return
            
            new_urgency = self.patient_lookup_view.get_urgency_level_input("Enter new urgency level (1-5)")
            new_urgency = int(new_urgency)
            
            if not (1 <= new_urgency <= 5):
                self.patient_lookup_view.display_error("Urgency level must be between 1 and 5.")
                return
            
            # Update patient record and heap priority
            old_urgency = patient.get_urgency_level()
            patient.set_urgency_level(new_urgency)
            
            # Use decrease/increase-key strategy
            success = self.treatment_heap.update_patient_priority(patient_id, new_urgency=new_urgency)
            
            if success:
                self.patient_lookup_view.display_patient_updated(patient_id)
            else:
                self.patient_lookup_view.display_error(f"Failed to update patient {patient_id} in treatment heap.")
        except ValueError:
            self.patient_lookup_view.display_error("Invalid input. Please enter valid integers.")
        except Exception as e:
            self.patient_lookup_view.display_error(f"Error updating patient urgency: {e}")

    def update_patient_status(self):
        """Update a patient's treatment status."""
        try:
            patient_id = self.patient_lookup_view.get_patient_id_input("Enter Patient ID to update")
            patient_id = int(patient_id)
            
            # Check if patient exists
            patient = self.patient_table.search(patient_id)
            if not patient:
                self.patient_lookup_view.display_patient_not_found(patient_id)
                return
            
            new_status = self.patient_lookup_view.get_treatment_status_input("Enter new treatment status")
            
            # Update patient record and heap priority
            old_status = patient.get_treatment_status()
            patient.set_treatment_status(new_status)
            
            # Use decrease/increase-key strategy
            success = self.treatment_heap.update_patient_priority(patient_id, new_status=new_status)
            
            if success:
                self.patient_lookup_view.display_patient_updated(patient_id)
            else:
                self.patient_lookup_view.display_error(f"Failed to update patient {patient_id} in treatment heap.")
        except ValueError:
            self.patient_lookup_view.display_error("Invalid input. Please enter valid patient ID.")
        except Exception as e:
            self.patient_lookup_view.display_error(f"Error updating patient status: {e}")

    def update_patient_department(self):
        """Update a patient's department."""
        try:
            patient_id = self.patient_lookup_view.get_patient_id_input("Enter Patient ID to update")
            patient_id = int(patient_id)
            
            # Check if patient exists
            patient = self.patient_table.search(patient_id)
            if not patient:
                self.patient_lookup_view.display_patient_not_found(patient_id)
                return
            
            new_department = self.patient_lookup_view.get_department_input("Enter new department")
            
            # Validate department
            if not new_department.strip():
                self.patient_lookup_view.display_error("Department cannot be empty.")
                return
            
            # Update patient record and heap priority
            old_department = patient.get_department()
            patient.set_department(new_department)
            
            # Use decrease/increase-key strategy
            success = self.treatment_heap.update_patient_priority(patient_id, new_department=new_department)
            
            if success:
                self.patient_lookup_view.display_patient_updated(patient_id)
            else:
                self.patient_lookup_view.display_error(f"Failed to update patient {patient_id} in treatment heap.")
        except ValueError:
            self.patient_lookup_view.display_error("Invalid input. Please enter valid patient ID.")
        except Exception as e:
            self.patient_lookup_view.display_error(f"Error updating patient department: {e}")

    def run_patient_management(self):
        """Run patient management operations with sub-modules."""
        running = True
        while running:
            self.display_module2_menu()
            choice = self.get_module2_choice()
            
            if choice is None:
                continue
            
            if choice == 1:
                self.run_patient_lookup()
            elif choice == 2:
                self.run_treatment_scheduler()
            elif choice == 3:
                self.run_patient_record_sorting()
            elif choice == 4:
                running = False
            else:
                self.view.display_error("Invalid choice. Please select 1-4.")

    def display_module2_menu(self):
        """Display Module 2 main menu."""
        print("\nPATIENT MANAGEMENT SYSTEM")
        print("=" * 60)
        print("Module 2: Patient Management System")
        print("=" * 60)
        print("2.1. Patient Lookup")
        print("2.2. Treatment Scheduler")
        print("2.3. Patient Record Sorting")
        print("4. Back to Main Menu")
        print("=" * 60)

    def get_module2_choice(self):
        """Get user's Module 2 menu choice."""
        try:
            choice = input("Enter your choice (1-4): ").strip()
            return int(choice)
        except ValueError:
            print("Invalid input. Please enter a number.")
            return None

    def run_patient_lookup(self):
        """Run Patient Lookup sub-module (2.1)."""
        running = True
        while running:
            self.patient_lookup_view.display_patient_lookup_menu()
            choice = self.patient_lookup_view.get_patient_lookup_choice()
            
            if choice is None:
                continue
            
            if choice == 1:
                self.add_patient()
            elif choice == 2:
                self.search_patient()
            elif choice == 3:
                self.remove_patient()
            elif choice == 4:
                self.run_patient_update()
            elif choice == 5:
                self.display_all_patients()
            elif choice == 6:
                running = False
                self.patient_lookup_view.display_back_to_module2()
            else:
                self.patient_lookup_view.display_invalid_choice()

    def run_treatment_scheduler(self):
        """Run Treatment Scheduler sub-module (2.2)."""
        running = True
        while running:
            self.treatment_scheduler_view.display_treatment_scheduler_menu()
            choice = self.treatment_scheduler_view.get_treatment_scheduler_choice()
            
            if choice is None:
                continue
            
            if choice == 1:
                self.peek_next_patient()
            elif choice == 2:
                self.extract_next_patient()
            elif choice == 3:
                self.display_treatment_queue()
            elif choice == 4:
                self.run_priority_update()
            elif choice == 5:
                running = False
                self.treatment_scheduler_view.display_back_to_module2()
            else:
                self.treatment_scheduler_view.display_invalid_choice()

    def run_patient_record_sorting(self):
        """Run Patient Record Sorting sub-module (2.3)."""
        self.sorting_controller.run_sorting_interface()
        self.sorting_view.display_back_to_module2()

    def run_patient_update(self):
        """Run patient update operations."""
        self.patient_lookup_view.display_update_menu()
        choice = self.patient_lookup_view.get_update_choice()
        
        if choice is None:
            return
        
        if choice == 1:
            self.update_patient_urgency()
        elif choice == 2:
            self.update_patient_status()
        elif choice == 3:
            self.update_patient_department()
        elif choice == 4:
            return
        else:
            self.patient_lookup_view.display_invalid_choice()

    def run_priority_update(self):
        """Run priority update operations."""
        self.treatment_scheduler_view.display_priority_update_menu()
        choice = self.treatment_scheduler_view.get_priority_update_choice()
        
        if choice is None:
            return
        
        if choice == 1:
            self.update_patient_urgency()
        elif choice == 2:
            self.update_patient_status()
        elif choice == 3:
            self.update_patient_department()
        elif choice == 4:
            return
        else:
            self.treatment_scheduler_view.display_invalid_choice()

    def display_all_patients(self):
        """Display all patients in the system."""
        try:
            if self.patient_table.isEmpty():
                self.patient_lookup_view.display_no_patients()
                return
            
            self.patient_lookup_view.display_all_patients_header()
            
            # Get all patients from hash table using values() method
            all_patients = self.patient_table.values()
            for patient in all_patients:
                self.patient_lookup_view.display_patient_row(patient)
                
        except Exception as e:
            self.patient_lookup_view.display_error(f"Error displaying patients: {e}")

