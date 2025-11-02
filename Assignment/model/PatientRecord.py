"""
Patient Record class for Hospital Management System.
Represents a patient with all required fields for hash-based lookup.
"""

from model.TreatmentTime import TreatmentTime

class PatientRecord:
    """
    Patient record class containing all patient information.
    Used for hash table storage and retrieval operations.
    """
    
    def __init__(self, patient_id, name, age, department, urgency_level, treatment_status, treatment_time=None):
        """
        Initialize a patient record.
        
        Args:
            patient_id (int): Unique patient identifier
            name (str): Patient's full name
            age (int): Patient's age
            department (str): Department where patient is located
            urgency_level (int): Urgency level from 1-5 (1=lowest, 5=highest)
            treatment_status (str): Current treatment status
            treatment_time (int, optional): Treatment time in minutes. If not provided, will be calculated automatically.
        """
        self.patient_id = int(patient_id)
        self.name = name
        self.age = age
        self.department = department
        self.urgency_level = urgency_level
        self.treatment_status = treatment_status
        if treatment_time is not None:
            self.treatment_time = int(treatment_time)
        else:
            self.treatment_time = self.calculate_treatment_time()
    
    def get_patient_id(self):
        """Get patient ID."""
        return self.patient_id
    
    def get_name(self):
        """Get patient name."""
        return self.name
    
    def get_age(self):
        """Get patient age."""
        return self.age
    
    def get_department(self):
        """Get patient department."""
        return self.department
    
    def get_urgency_level(self):
        """Get urgency level."""
        return self.urgency_level
    
    def get_treatment_status(self):
        """Get treatment status."""
        return self.treatment_status
    
    def get_treatment_time(self):
        """Get treatment time."""
        return self.treatment_time
    
    def set_treatment_status(self, new_status):
        """Update treatment status."""
        self.treatment_status = new_status
    
    def set_department(self, new_department):
        """Update patient department."""
        self.department = new_department
    
    def set_urgency_level(self, new_level):
        """Update urgency level."""
        if 1 <= new_level <= 5:
            self.urgency_level = new_level
        else:
            raise ValueError("Urgency level must be between 1 and 5")
    
    def calculate_treatment_time(self):
        """
        Calculate estimated treatment time.
        Note: Urgency is not factored into treatment time as it's already
        handled in the priority calculation (Priority = (6 - U) + 1000 / T).
        
        Returns treatment time in minutes.
        """
        # Initialize calculator (could be a class variable to avoid repeated initialization)
        calculator = TreatmentTime()
        
        # Get base time from department
        base_time = calculator.get_department_time(self.department)
        
        # Apply status adjustment (urgency is handled in priority calculation)
        status_mult = calculator.get_status_adjustment(self.treatment_status)
        
        # Apply age factor
        age_mult = 1.0
        if self.age < 18:
            age_mult = 1.2  # Pediatric cases
        elif self.age > 65:
            age_mult = 1.3  # Elderly patients
        
        # Calculate final treatment time (urgency not included)
        treatment_time = base_time * status_mult * age_mult
        
        return int(treatment_time) 
    
    def __str__(self):
        """String representation of patient record."""
        return (f"PatientRecord(ID: {self.patient_id}, Name: {self.name}, "
                f"Age: {self.age}, Department: {self.department}, "
                f"Urgency: {self.urgency_level}, Status: {self.treatment_status})")
