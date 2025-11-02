"""
Sorting Controller class for Hospital Management System.
Handles patient record sorting operations using DSA sorting algorithms.
"""

import time
import numpy as np
from model.PatientRecord import PatientRecord
from view.SortingView import SortingView
from DataStructures.DSAsorts import mergeSort, quickSortMedian3
from DataStructures.PatientHashTable import PatientHashTable
from DataStructures.TreatmentHeap import TreatmentHeap

class SortResult:
    def __init__(self, patients, execution_time):
        self.patients = patients
        self.execution_time = execution_time
    
    def __iter__(self):
        yield self.patients
        yield self.execution_time
    
    def __getitem__(self, index):
        if index == 0:
            return self.patients
        elif index == 1:
            return self.execution_time
        else:
            raise IndexError("Index out of range")
    
    def __len__(self):
        return 2

class SortingController:

    def __init__(self, patient_table=None, treatment_heap=None):
        self.patient_table = patient_table or PatientHashTable()
        self.treatment_heap = treatment_heap or TreatmentHeap()
        self.view = SortingView()

    def display_sorting_menu(self):
        """Display the sorting menu options."""
        self.view.display_sorting_menu()

    def get_sorting_choice(self):
        """Get user's sorting menu choice."""
        return self.view.get_sorting_choice()

    def get_patients_list(self):
        """Get all patients from the hash table as a numpy array."""
        return self.patient_table.values()

    def sort_patients_merge_sort(self, patients):
        """Sort patients using merge sort by treatment duration without built-in list functions."""
        n = len(patients)
        if n == 0:
            return SortResult(patients, 0.0)

        patients = np.array(patients, dtype=object)
        treatment_times = np.empty(n)
        for i in range(n):
            treatment_times[i] = patients[i].treatment_time

        start_time = time.perf_counter()
        sorted_times = mergeSort(treatment_times.copy())  # your custom merge sort
        end_time = time.perf_counter()

        sorted_patients = np.empty(n, dtype=object)
        used_indices = np.zeros(n, dtype=bool)

        for i in range(n):
            target_time = sorted_times[i]
            j = 0
            while j < n:
                if not used_indices[j] and patients[j].treatment_time == target_time:
                    sorted_patients[i] = patients[j]
                    used_indices[j] = True
                    break
                j += 1

        return SortResult(sorted_patients, end_time - start_time)


    def sort_patients_quick_sort(self, patients):
        """Sort patients using quick sort with median of three pivot by treatment duration without built-in list functions."""
        n = len(patients)
        if n == 0:
            return SortResult(patients, 0.0)

        patients = np.array(patients, dtype=object)
        treatment_times = np.empty(n)
        for i in range(n):
            treatment_times[i] = patients[i].treatment_time

        start_time = time.perf_counter()
        sorted_times = quickSortMedian3(treatment_times.copy())
        end_time = time.perf_counter()

        sorted_patients = np.empty(n, dtype=object)
        used_indices = np.zeros(n, dtype=bool)

        for i in range(n):
            target_time = sorted_times[i]
            j = 0
            while j < n:
                if not used_indices[j] and patients[j].treatment_time == target_time:
                    sorted_patients[i] = patients[j]
                    used_indices[j] = True
                    break
                j += 1

        return SortResult(sorted_patients, end_time - start_time)


    def display_sorted_patients(self, patients, algorithm_name, execution_time):
        """Display sorted patients with timing information."""
        self.view.display_sorted_patients(patients, algorithm_name, execution_time)

    def generate_test_data(self, sort_order=None, num_patients=None):
        """Generate test patient data for sorting analysis.
        
        Args:
            sort_order (str, optional): Order for treatment times. 
                One of: "random", "nearly_sorted", or "reversed".
                If None, will prompt user for input.
            num_patients (int, optional): Number of patients to generate.
                If None, will prompt user for input.
        """
        # Get user input for number of test patients if not provided
        if num_patients is None:
            num_patients = self.view.get_test_data_count()
        
        # Get sort order if not provided
        if sort_order is None:
            sort_order = self.view.get_sort_order_type()
        
        departments = np.array(["Emergency", "ICU", "Operating Theatre", "Radiology", 
                      "Laboratory", "Pharmacy", "Outpatient", "Wards"])
        statuses = np.array(["Critical", "Stable", "Under Treatment", "Waiting", 
                   "Recovery", "Test Results", "Medication"])
        
        # Generate treatment times based on sort order
        treatment_times = self._generate_treatment_times(num_patients, sort_order)
        
        # Use numpy array to store test patients
        test_patients = np.empty(num_patients, dtype=object)
        base_id = len(self.patient_table) + 1
        
        self.view.display_test_data_generation()
        
        for i in range(num_patients):
            patient_id = base_id + i
            name = f"Test Patient {i+1}"
            age = np.random.randint(18, 80)
            department = np.random.choice(departments)
            urgency_level = np.random.randint(1, 6)
            treatment_status = np.random.choice(statuses)
            
            # Create patient with specified treatment_time
            patient = PatientRecord(patient_id, name, age, department, 
                                  urgency_level, treatment_status, 
                                  treatment_time=int(treatment_times[i]))
            test_patients[i] = patient
            self.patient_table.insert(patient)
            self.treatment_heap.insert(patient)
        
        self.view.display_test_data_generated(len(test_patients))
        return test_patients
    
    def _generate_treatment_times(self, num_patients, sort_order):
        """
        Generate treatment times based on specified sort order.
        
        Args:
            num_patients (int): Number of patients
            sort_order (str): One of "random", "nearly_sorted", or "reversed"
        
        Returns:
            numpy.ndarray: Array of treatment times in the specified order
        """
        # Base range for treatment times (30-300 minutes)
        min_time = 30
        max_time = 300
        
        if sort_order == "random":
            # Generate completely random treatment times
            treatment_times = np.random.randint(min_time, max_time + 1, size=num_patients)
        
        elif sort_order == "nearly_sorted":
            # Generate sorted array first
            treatment_times = np.linspace(min_time, max_time, num_patients, dtype=int)
            # Add small random variations
            variations = np.random.randint(-5, 6, size=num_patients)
            treatment_times = np.clip(treatment_times + variations, min_time, max_time)
            
            # Displace ≤10% of elements
            num_to_displace = max(1, int(num_patients * 0.1))  # At least 1 if num_patients > 0
            indices_to_displace = np.random.choice(num_patients, size=num_to_displace, replace=False)
            
            # Swap displaced elements with random positions
            for idx in indices_to_displace:
                swap_idx = np.random.randint(0, num_patients)
                if swap_idx != idx:
                    treatment_times[idx], treatment_times[swap_idx] = treatment_times[swap_idx], treatment_times[idx]
        
        elif sort_order == "reversed":
            # Generate sorted array in descending order
            treatment_times = np.linspace(max_time, min_time, num_patients, dtype=int)
            # Add small random variations
            variations = np.random.randint(-5, 6, size=num_patients)
            treatment_times = np.clip(treatment_times + variations, min_time, max_time)
        
        else:
            # Default to random if invalid sort_order
            treatment_times = np.random.randint(min_time, max_time + 1, size=num_patients)
        
        return treatment_times

    def run_performance_analysis(self):
        """Run comprehensive performance analysis on sorting algorithms."""
        self.view.display_performance_analysis_header()
        
        # Get current patients
        patients = self.get_patients_list()
        if len(patients) == 0:
            self.view.display_no_patients_message()
            return
        
        self.view.display_analyzing_patients(len(patients))
        
        # Test different sorting algorithms using numpy arrays
        algorithm_names = np.array(["Merge Sort", "Quick Sort (Median of Three)"])
        algorithm_types = np.array(["merge", "median3"])
        execution_times = np.zeros(2)
        patient_counts = np.zeros(2)
        
        for i in range(2):
            self.view.display_algorithm_testing(algorithm_names[i])
            
            if algorithm_types[i] == "merge":
                sorted_patients, exec_time = self.sort_patients_merge_sort(patients)
            else:
                sorted_patients, exec_time = self.sort_patients_quick_sort(patients)
            
            execution_times[i] = exec_time
            patient_counts[i] = len(sorted_patients)
            self.view.display_algorithm_result(algorithm_names[i], exec_time)
        
        # Display comparison table
        self.view.display_performance_comparison_header()
        
        for i in range(2):
            self.view.display_performance_row(algorithm_names[i], execution_times[i], int(patient_counts[i]))
        
        # Find fastest algorithm
        fastest_idx = np.argmin(execution_times)
        self.view.display_fastest_algorithm(algorithm_names[fastest_idx], execution_times[fastest_idx])

    def run_sorting_interface(self):
        """Run the main sorting interface."""
        self.view.display_sorting_system_header()
        
        running = True
        while running:
            try:
                self.display_sorting_menu()
                choice = self.get_sorting_choice()
                
                if choice is None:
                    continue
                
                patients = self.get_patients_list()
                
                if choice == 1:  # Merge Sort
                    if len(patients) == 0:
                        self.view.display_no_patients_for_sorting()
                        continue
                    sorted_patients, exec_time = self.sort_patients_merge_sort(patients)
                    self.display_sorted_patients(sorted_patients, "Merge Sort", exec_time)
                
                elif choice == 2:  # Quick Sort Median of Three
                    if len(patients) == 0:
                        self.view.display_no_patients_for_sorting()
                        continue
                    sorted_patients, exec_time = self.sort_patients_quick_sort(patients)
                    self.display_sorted_patients(sorted_patients, "Quick Sort (Median of Three)", exec_time)
                
                elif choice == 3:  # Performance Analysis
                    self.run_performance_analysis()
                
                elif choice == 4:  # Generate Test Data
                    self.generate_test_data()
                
                elif choice == 5:  # Back to Patient Menu
                    running = False
                
                else:
                    self.view.display_invalid_choice()
                
                if running:
                    self.view.get_continue_input()
                    
            except KeyboardInterrupt:
                self.view.display_sorting_interrupted()
                running = False
            except Exception as e:
                self.view.display_unexpected_error(str(e))
                self.view.get_error_continue_input()
