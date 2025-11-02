"""
Sorting View class for Hospital Management System.
Handles all user interface and display operations for patient record sorting.
"""

class SortingView:
    """
    View class for Patient Record Sorting.
    Handles all user interface and display operations for sorting operations.
    """

    def display_sorting_menu(self):
        """Display the sorting menu options."""
        print("\nPATIENT RECORD SORTING SYSTEM")
        print("=" * 60)
        print("Sub-module 2.3: Patient Record Sorting")
        print("=" * 60)
        print("1. Merge Sort (by Treatment Duration)")
        print("2. Quick Sort - Median of Three (by Treatment Duration)")
        print("3. Performance Analysis")
        print("4. Generate Test Data")
        print("5. Back to Module 2 Menu")
        print("=" * 60)

    def get_sorting_choice(self):
        """Get user's sorting menu choice."""
        try:
            choice = input("Enter your choice (1-5): ").strip()
            return int(choice)
        except ValueError:
            print("Invalid input. Please enter a number.")
            return None

    def display_sorted_patients(self, patients, algorithm_name, execution_time):
        """Display sorted patients with timing information."""
        print(f"\n{algorithm_name} Results")
        print("=" * 60)
        print(f"Execution Time: {execution_time:.6f} seconds")
        print(f"Total Patients: {len(patients)}")
        print("\nSorted Patient Records (by Treatment Duration):")
        print("-" * 60)
        
        for i, patient in enumerate(patients, 1):
            print(f"{i:3d}. ID: {patient.patient_id:4d} | "
                  f"Name: {patient.name:20s} | "
                  f"Department: {patient.department:15s} | "
                  f"Treatment Time: {patient.treatment_time:3d} min | "
                  f"Urgency: {patient.urgency_level}")

    def display_performance_analysis_header(self):
        """Display performance analysis header."""
        print("\nPERFORMANCE ANALYSIS")
        print("=" * 60)

    def display_no_patients_message(self):
        """Display message when no patients are found."""
        print("No patients found. Please add patients first or generate test data.")

    def display_analyzing_patients(self, count):
        """Display message showing number of patients being analyzed."""
        print(f"Analyzing {count} patients...")

    def display_algorithm_testing(self, algorithm_name):
        """Display message when testing an algorithm."""
        print(f"\nTesting {algorithm_name}...")

    def display_algorithm_result(self, algorithm_name, execution_time):
        """Display result for a single algorithm test."""
        print(f"Success: {algorithm_name}: {execution_time:.6f} seconds")

    def display_performance_comparison_header(self):
        """Display performance comparison table header."""
        print("\nPERFORMANCE COMPARISON")
        print("=" * 80)
        print(f"{'Algorithm':<25} {'Time (seconds)':<15} {'Patients':<10}")
        print("-" * 80)

    def display_performance_row(self, algorithm_name, execution_time, patient_count):
        """Display a single row in the performance comparison table."""
        print(f"{algorithm_name:<25} {execution_time:<15.6f} {patient_count:<10}")

    def display_fastest_algorithm(self, algorithm_name, execution_time):
        """Display the fastest algorithm result."""
        print(f"\nFastest Algorithm: {algorithm_name} ({execution_time:.6f} seconds)")

    def display_test_data_generation(self):
        """Display message when generating test data."""
        print("Generating test data...")

    def display_test_data_generated(self, count):
        """Display message when test data generation is complete."""
        print(f"Generated {count} test patients")

    def display_no_patients_for_sorting(self):
        """Display message when no patients are available for sorting."""
        print("No patients found. Please add patients first.")

    def display_sorting_system_header(self):
        """Display the main sorting system header."""
        print("\nPATIENT RECORD SORTING SYSTEM")
        print("=" * 60)
        print("Sort patient records by treatment duration using various algorithms")

    def display_invalid_choice(self):
        """Display message for invalid menu choice."""
        print("Invalid choice. Please select 1-5.")

    def display_sorting_interrupted(self):
        """Display message when sorting interface is interrupted."""
        print("\n\nSorting interface interrupted by user.")

    def display_unexpected_error(self, error_message):
        """Display message for unexpected errors."""
        print(f"Unexpected error: {error_message}")

    def get_continue_input(self):
        """Get user input to continue."""
        return input("\nPress Enter to continue...")

    def get_error_continue_input(self):
        """Get user input to continue after an error."""
        return input("Press Enter to continue...")

    def get_test_data_count(self):
        """Get user input for number of test patients to generate."""
        while True:
            try:
                count = input("Enter number of test patients to generate (1-1000): ").strip()
                count = int(count)
                if 1 <= count <= 1000:
                    return count
                else:
                    print("Please enter a number between 1 and 1000.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def get_sort_order_type(self):
        """Get user input for sort order type."""
        while True:
            print("\nSelect treatment time order:")
            print("1. Random")
            print("2. Nearly Sorted (≤10% elements displaced)")
            print("3. Reversed")
            try:
                choice = input("Enter your choice (1-3): ").strip()
                choice = int(choice)
                if choice == 1:
                    return "random"
                elif choice == 2:
                    return "nearly_sorted"
                elif choice == 3:
                    return "reversed"
                else:
                    print("Invalid choice. Please enter 1, 2, or 3.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def display_back_to_module2(self):
        """Display message when returning to Module 2."""
        print("\nReturning to Module 2: Patient Management System...")
