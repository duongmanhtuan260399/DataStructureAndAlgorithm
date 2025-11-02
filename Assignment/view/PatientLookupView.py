"""
Patient Lookup View class for Hospital Management System.
Handles user interface for patient lookup operations (Sub-module 2.1).
"""

class PatientLookupView:
    """
    View class for Patient Lookup operations.
    Handles all user interface and display operations for patient lookup.
    """

    def display_patient_lookup_menu(self):
        """Display the patient lookup menu options."""
        print("\nPATIENT LOOKUP SYSTEM")
        print("=" * 60)
        print("Sub-module 2.1: Patient Lookup")
        print("=" * 60)
        print("1. Add Patient")
        print("2. Search Patient")
        print("3. Remove Patient")
        print("4. Update Patient Information")
        print("5. Display All Patients")
        print("6. Back to Module 2 Menu")
        print("=" * 60)

    def get_patient_lookup_choice(self):
        """Get user's patient lookup menu choice."""
        try:
            choice = input("Enter your choice (1-6): ").strip()
            return int(choice)
        except ValueError:
            print("Invalid input. Please enter a number.")
            return None

    def get_patient_id_input(self, prompt):
        """Get patient ID from user."""
        return input(f"{prompt}: ").strip()

    def get_name_input(self, prompt):
        """Get patient name from user."""
        return input(f"{prompt}: ").strip()

    def get_age_input(self, prompt):
        """Get patient age from user."""
        return input(f"{prompt}: ").strip()

    def get_department_input(self, prompt):
        """Get department from user."""
        return input(f"{prompt}: ").strip()

    def get_urgency_level_input(self, prompt):
        """Get urgency level from user."""
        return input(f"{prompt}: ").strip()

    def get_treatment_status_input(self, prompt):
        """Get treatment status from user."""
        return input(f"{prompt}: ").strip()

    def display_patient_record(self, record):
        """Display patient record information."""
        print("\nPatient Record:")
        print("-" * 40)
        print(f"ID: {record.patient_id}")
        print(f"Name: {record.name}")
        print(f"Age: {record.age}")
        print(f"Department: {record.department}")
        print(f"Urgency Level: {record.urgency_level}")
        print(f"Treatment Status: {record.treatment_status}")
        print(f"Treatment Time: {record.treatment_time} minutes")
        print("-" * 40)

    def display_patient_not_found(self, patient_id):
        """Display message when patient is not found."""
        print(f"Patient {patient_id} not found in the system.")

    def display_patient_added(self, patient_id):
        """Display success message when patient is added."""
        print(f"Success: Patient {patient_id} added successfully.")

    def display_patient_removed(self, patient_id):
        """Display success message when patient is removed."""
        print(f"Success: Patient {patient_id} removed successfully.")

    def display_patient_updated(self, patient_id):
        """Display success message when patient is updated."""
        print(f"Success: Patient {patient_id} updated successfully.")

    def display_all_patients_header(self):
        """Display header for all patients list."""
        print("\nALL PATIENTS IN SYSTEM")
        print("=" * 80)
        print(f"{'ID':<6} {'Name':<20} {'Age':<4} {'Department':<15} {'Urgency':<7} {'Status':<15} {'Time':<5}")
        print("-" * 80)

    def display_patient_row(self, patient):
        """Display a single patient row."""
        print(f"{patient.patient_id:<6} {patient.name:<20} {patient.age:<4} "
              f"{patient.department:<15} {patient.urgency_level:<7} "
              f"{patient.treatment_status:<15} {patient.treatment_time:<5}")

    def display_no_patients(self):
        """Display message when no patients are found."""
        print("No patients found in the system.")

    def display_update_menu(self):
        """Display patient update options."""
        print("\nUPDATE PATIENT INFORMATION")
        print("-" * 40)
        print("1. Update Urgency Level")
        print("2. Update Treatment Status")
        print("3. Update Department")
        print("4. Back to Patient Lookup Menu")
        print("-" * 40)

    def get_update_choice(self):
        """Get user's update menu choice."""
        try:
            choice = input("Enter your choice (1-4): ").strip()
            return int(choice)
        except ValueError:
            print("Invalid input. Please enter a number.")
            return None

    def display_success(self, message):
        """Display success message."""
        print(f"Success: {message}")

    def display_error(self, message):
        """Display error message."""
        print(f"Error: {message}")

    def display_separator(self):
        """Display separator line."""
        print("\n" + "=" * 60)

    def get_confirmation(self, message):
        """Get user confirmation."""
        response = input(f"{message} (y/n): ").strip().lower()
        return response in ['y', 'yes']

    def display_invalid_choice(self):
        """Display message for invalid choice."""
        print("Invalid choice. Please select 1-6.")

    def display_back_to_module2(self):
        """Display message when returning to Module 2."""
        print("\nReturning to Module 2: Patient Management System...")
