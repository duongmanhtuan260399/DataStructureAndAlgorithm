"""
TreatmentHeap class for Hospital Management System.
Uses DSAHeap to manage patient priority queue based on treatment urgency and time.
"""

from DataStructures.DSAHeap import DSAHeap
from model.PatientRecord import PatientRecord

class TreatmentHeap:
    """
    Treatment heap for managing patient priority queue.
    Uses max heap to prioritize patients based on urgency and treatment time.
    Priority formula: Priority = (6 - U) + 1000 / T
    Where U = UrgencyLevel (1=highest, 5=lowest), T = Treatment time in minutes
    """
    
    def __init__(self, capacity=10):
        """
        Initialize the treatment heap.
        
        Args:
            capacity (int): Initial capacity of the heap
        """
        self.heap = DSAHeap(capacity)
        self.patient_count = 0
        self._debug = False
    
    def insert(self, patient):
        """
        Insert a patient into the treatment heap.
        
        Args:
            patient (PatientRecord): Patient to insert
            
        Raises:
            TypeError: If patient is not a PatientRecord instance
        """
        if not isinstance(patient, PatientRecord):
            raise TypeError("Patient must be a PatientRecord instance")
        
        if self._debug:
            print(f"\n[HEAP INSERT] Patient ID: {patient.get_patient_id()}, Name: {patient.get_name()}")
            print(f"Urgency Level: {patient.get_urgency_level()}")
            treatment_time = patient.calculate_treatment_time()
            print(f"Treatment Time: {treatment_time} minutes")
        
        # Calculate priority using the specified formula
        priority = self._calculate_priority(patient)
        
        if self._debug:
            print(f"Priority Calculation: (6 - {patient.get_urgency_level()}) + (1000 / {treatment_time}) = {priority:.2f}")
        
        # Insert into the underlying DSAHeap
        self.heap.add(priority, patient)
        self.patient_count += 1
    
    def peek(self):
        """
        Peek at the highest priority patient without removing them.
        
        Returns:
            PatientRecord: The highest priority patient, or None if heap is empty
        """
        if self.patient_count == 0:
            return None
        
        # Get the root entry from the heap
        root_entry = self.heap.heap[0]
        if root_entry is not None:
            return root_entry.get_value()

        return None
    
    def extract_priority(self):
        """
        Extract and remove the highest priority patient from the heap.
        
        Returns:
            PatientRecord: The highest priority patient
            
        Raises:
            IndexError: If heap is empty
        """
        if self.patient_count == 0:
            raise IndexError("Treatment heap is empty")
        
        if self._debug:
            print(f"\n[HEAP EXTRACT] Extracting highest priority patient")
            if self.patient_count > 0:
                peek_patient = self.peek()
                if peek_patient:
                    peek_priority = self._calculate_priority(peek_patient)
                    print(f"Current root: Patient ID: {peek_patient.get_patient_id()}, Priority: {peek_priority:.2f}")
        
        # Remove the highest priority patient
        patient = self.heap.remove()
        self.patient_count -= 1
        
        if self._debug:
            if patient:
                priority = self._calculate_priority(patient)
                print(f"Extracted: Patient ID: {patient.get_patient_id()}, Name: {patient.get_name()}, Priority: {priority:.2f}")
        
        return patient
    
    def _calculate_priority(self, patient):
        """
        Calculate priority for a patient using the specified formula.
        Priority = (6 - U) + 1000 / T
        Where U = UrgencyLevel (1=highest, 5=lowest), T = Treatment time in minutes
        
        Args:
            patient (PatientRecord): Patient to calculate priority for
            
        Returns:
            float: Calculated priority value
        """
        U = patient.get_urgency_level()  # Urgency level (1-5)
        T = patient.calculate_treatment_time()  # Treatment time in minutes
        
        # Apply the priority formula
        priority = (6 - U) + (1000.0 / T)
        
        return priority
    
    def is_empty(self):
        """
        Check if the treatment heap is empty.
        
        Returns:
            bool: True if heap is empty, False otherwise
        """
        return self.patient_count == 0
    
    def size(self):
        """
        Get the number of patients in the heap.
        
        Returns:
            int: Number of patients in the heap
        """
        return self.patient_count
    
    def remove_patient(self, patient_id):
        """
        Remove a patient from the heap by patient ID.
        
        Args:
            patient_id (int): ID of the patient to remove
            
        Returns:
            PatientRecord: The removed patient, or None if not found
            
        Raises:
            ValueError: If patient_id is not a valid integer
        """
        try:
            patient_id = int(patient_id)
        except (ValueError, TypeError):
            raise ValueError("Patient ID must be a valid integer")
        
        # Find the patient in the heap
        patient_index = self._find_patient_index(patient_id)
        if patient_index == -1:
            return None
        
        # Get the patient to return
        patient = self.heap.heap[patient_index].get_value()
        
        # Remove the patient by moving the last element to this position
        self._remove_patient_at_index(patient_index)
        
        return patient
    
    def _find_patient_index(self, patient_id):
        """
        Find the index of a patient in the heap by patient ID.
        
        Args:
            patient_id (int): ID of patient to find
            
        Returns:
            int: Index of patient in heap, or -1 if not found
        """
        for i in range(self.heap.count):
            entry = self.heap.heap[i]
            if entry is not None:
                patient = entry.get_value()
                if patient.get_patient_id() == patient_id:
                    return i
        return -1
    
    def _remove_patient_at_index(self, index):
        """
        Remove a patient at a specific index in the heap.
        Maintains heap property after removal.
        
        Args:
            index (int): Index of patient to remove
        """
        if index >= self.heap.count or index < 0:
            return
        
        # Move the last element to this position
        self.heap.heap[index] = self.heap.heap[self.heap.count - 1]
        self.heap.heap[self.heap.count - 1] = None
        self.heap.count -= 1
        self.patient_count -= 1
        
        # Restore heap property
        if index < self.heap.count and self.heap.count > 0:
            # Check if we need to trickle up or down
            parent_idx = (index - 1) // 2
            if index > 0 and self.heap.heap[parent_idx].get_priority() < self.heap.heap[index].get_priority():
                self.heap._trickle_up(index)
            else:
                self.heap._trickle_down(index, self.heap.count)
    
    def contains_patient(self, patient_id):
        """
        Check if a patient with the given ID exists in the heap.
        
        Args:
            patient_id (int): ID of patient to check
            
        Returns:
            bool: True if patient exists, False otherwise
        """
        try:
            patient_id = int(patient_id)
            return self._find_patient_index(patient_id) != -1
        except (ValueError, TypeError):
            return False
    
    def get_patient_priority(self, patient_id):
        """
        Get the priority of a patient by their ID.
        
        Args:
            patient_id (int): ID of patient to get priority for
            
        Returns:
            float: Priority value, or None if patient not found
        """
        try:
            patient_id = int(patient_id)
        except (ValueError, TypeError):
            return None
        
        patient_index = self._find_patient_index(patient_id)
        if patient_index == -1:
            return None
        
        return self.heap.heap[patient_index].get_priority()
    
    def display(self):
        """
        Display the treatment heap in a readable format.
        Shows patients in priority order with their details.
        """
        if self.patient_count == 0:
            print("Treatment heap is empty")
            return
        
        print(f"\n=== Treatment Heap ({self.patient_count} patients) ===")
        print("Priority Order (highest to lowest):")
        print("-" * 80)
        
        # Create a temporary heap to display without modifying the original
        temp_heap = DSAHeap(self.patient_count)
        
        # Copy all patients to temporary heap
        for i in range(self.heap.count):
            entry = self.heap.heap[i]
            if entry is not None:
                temp_heap.add(entry.get_priority(), entry.get_value())
        
        # Display patients in priority order
        rank = 1
        while temp_heap.count > 0:
            patient = temp_heap.remove()
            priority = self._calculate_priority(patient)
            treatment_time = patient.calculate_treatment_time()
            
            print(f"{rank:2d}. Priority: {priority:.2f} | "
                  f"ID: {patient.get_patient_id():3d} | "
                  f"Name: {patient.get_name():15s} | "
                  f"Dept: {patient.get_department():12s} | "
                  f"Urgency: {patient.get_urgency_level()} | "
                  f"Time: {treatment_time:3d}min | "
                  f"Status: {patient.get_treatment_status()}")
            rank += 1
        
        print("-" * 80)
    
    def set_debug(self, enabled):
        """
        Enable or disable debug logging for heap operations.
        
        Args:
            enabled (bool): True to enable debug logging, False to disable
        """
        self._debug = bool(enabled)
        self.heap.set_debug(enabled)
    
    def update_patient_priority(self, patient_id, new_urgency=None, new_status=None, new_department=None):
        """
        Update patient priority using decrease/increase-key strategy.
        More efficient than remove + re-insert approach.
        
        Args:
            patient_id (int): ID of patient to update
            new_urgency (int, optional): New urgency level (1-5)
            new_status (str, optional): New treatment status
            new_department (str, optional): New department
            
        Returns:
            bool: True if patient was found and updated, False otherwise
            
        """
        try:
            patient_id = int(patient_id)
        except (ValueError, TypeError):
            return False
        
        # Find patient index - O(n)
        patient_index = self._find_patient_index(patient_id)
        if patient_index == -1:
            return False
        
        # Get current entry and patient
        entry = self.heap.heap[patient_index]
        patient = entry.get_value()
        old_priority = entry.get_priority()
        
        # Update patient attributes
        if new_urgency is not None:
            patient.set_urgency_level(new_urgency)
        if new_status is not None:
            patient.set_treatment_status(new_status)
        if new_department is not None:
            patient.set_department(new_department)
        
        # Calculate new priority
        new_priority = self._calculate_priority(patient)
        
        # Update priority in-place
        entry._priority = new_priority
        
        # Restore heap property
        if new_priority > old_priority:
            self.heap._trickle_up(patient_index)    # Priority increased
        elif new_priority < old_priority:
            self.heap._trickle_down(patient_index, self.heap.count)  # Priority decreased
        # If same priority, no restoration needed
        
        return True