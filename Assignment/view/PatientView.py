class PatientView:
    """
    View class for Patient Management.
    Handles all user interface and display operations for patients.
    """

    def get_patient_id_input(self, prompt):
        return input(f"{prompt}: ").strip()

    def get_name_input(self, prompt):
        return input(f"{prompt}: ").strip()

    def get_age_input(self, prompt):
        return input(f"{prompt}: ").strip()

    def get_department_input(self, prompt):
        return input(f"{prompt}: ").strip()

    def get_urgency_level_input(self, prompt):
        return input(f"{prompt}: ").strip()

    def get_treatment_status_input(self, prompt):
        return input(f"{prompt}: ").strip()

    def display_patient_record(self, record):
        print("\nPatient Record:")
        print(f"ID: {record.patient_id}")
        print(f"Name: {record.name}")
        print(f"Age: {record.age}")
        print(f"Department: {record.department}")
        print(f"Urgency Level: {record.urgency_level}")
        print(f"Treatment Status: {record.treatment_status}")

    def display_success(self, message):
        print(f"Success: {message}")

    def display_patient_menu(self):
        """Display the patient management menu options."""
        print("\nPATIENT MANAGEMENT MENU")
        print("=" * 60)
        print("1. Add Patient")
        print("2. Search Patient")
        print("3. Remove Patient")
        print("4. Update Patient Urgency")
        print("5. Update Patient Status")
        print("6. Update Patient Department")
        print("7. Peek Next Patient (Treatment Queue)")
        print("8. Extract Next Patient (Treatment Queue)")
        print("9. Display Treatment Queue")
        print("10. Sort Patient Records")
        print("11. Exit")

    def get_menu_choice(self):
        """Prompt the user to enter a menu choice."""
        return input("Enter your choice (1-11): ").strip()

    def display_error(self, message):
        print(f'Error: {message}')
