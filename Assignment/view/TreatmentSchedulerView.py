"""
Treatment Scheduler View class for Hospital Management System.
Handles user interface for treatment scheduling operations (Sub-module 2.2).
"""

class TreatmentSchedulerView:
    """
    View class for Treatment Scheduler operations.
    Handles all user interface and display operations for treatment scheduling.
    """

    def display_treatment_scheduler_menu(self):
        """Display the treatment scheduler menu options."""
        print("\nTREATMENT SCHEDULER SYSTEM")
        print("=" * 60)
        print("Sub-module 2.2: Treatment Scheduler")
        print("=" * 60)
        print("1. Peek Next Patient (View Next in Queue)")
        print("2. Extract Next Patient (Remove from Queue)")
        print("3. Display Treatment Queue")
        print("4. Update Patient Priority")
        print("5. Back to Module 2 Menu")
        print("=" * 60)

    def get_treatment_scheduler_choice(self):
        """Get user's treatment scheduler menu choice."""
        try:
            choice = input("Enter your choice (1-5): ").strip()
            return int(choice)
        except ValueError:
            print("Invalid input. Please enter a number.")
            return None

    def get_patient_id_input(self, prompt):
        """Get patient ID from user."""
        return input(f"{prompt}: ").strip()

    def get_urgency_level_input(self, prompt):
        """Get urgency level from user."""
        return input(f"{prompt}: ").strip()

    def get_treatment_status_input(self, prompt):
        """Get treatment status from user."""
        return input(f"{prompt}: ").strip()

    def get_department_input(self, prompt):
        """Get department from user."""
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

    def display_next_patient(self, patient, priority):
        """Display next patient in queue."""
        print("\nNEXT PATIENT IN TREATMENT QUEUE")
        print("=" * 50)
        self.display_patient_record(patient)
        print(f"Priority Score: {priority:.2f}")
        print("=" * 50)

    def display_patient_extracted(self, patient):
        """Display message when patient is extracted from queue."""
        print(f"\nSuccess: Patient {patient.patient_id} extracted for treatment.")
        self.display_patient_record(patient)

    def display_treatment_queue_header(self):
        """Display header for treatment queue."""
        print("\nCURRENT TREATMENT QUEUE")
        print("=" * 60)
        print("Patients are ordered by priority (highest priority first)")
        print("=" * 60)

    def display_queue_empty(self):
        """Display message when treatment queue is empty."""
        print("Treatment queue is empty. No patients waiting for treatment.")

    def display_priority_updated(self, patient_id, old_priority, new_priority):
        """Display message when patient priority is updated."""
        print(f"Success: Patient {patient_id} priority updated from {old_priority:.2f} to {new_priority:.2f}")

    def display_patient_not_found(self, patient_id):
        """Display message when patient is not found."""
        print(f"Patient {patient_id} not found in the treatment queue.")

    def display_priority_update_menu(self):
        """Display priority update options."""
        print("\nUPDATE PATIENT PRIORITY")
        print("-" * 40)
        print("1. Update Urgency Level")
        print("2. Update Treatment Status")
        print("3. Update Department")
        print("4. Back to Treatment Scheduler Menu")
        print("-" * 40)

    def get_priority_update_choice(self):
        """Get user's priority update menu choice."""
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
        print("Invalid choice. Please select 1-5.")

    def display_back_to_module2(self):
        """Display message when returning to Module 2."""
        print("\nReturning to Module 2: Patient Management System...")

    def display_priority_explanation(self):
        """Display explanation of priority calculation."""
        print("\nPRIORITY CALCULATION")
        print("-" * 30)
        print("Patient priority is calculated based on:")
        print("- Urgency Level (1-5, higher is more urgent)")
        print("- Treatment Status (affects priority)")
        print("- Department (affects treatment time)")
        print("- Lower priority score = Higher priority in queue")
        print("-" * 30)
