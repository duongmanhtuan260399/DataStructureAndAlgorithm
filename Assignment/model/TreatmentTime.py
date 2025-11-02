import numpy as np

class TreatmentTime:
    def __init__(self):
        # Department lookup - use indices for faster access
        self.department_names = np.array([
            "Emergency", "ICU", "Operating Theatre", "Radiology", 
            "Laboratory", "Pharmacy", "Outpatient", "Wards", "Reception"
        ])
        self.department_times = np.array([45, 120, 180, 30, 15, 10, 20, 60, 5])
        
        self.status_names = np.array([
            "Critical", "Stable", "Under Treatment", "Waiting", 
            "Recovery", "Test Results", "Medication", "Registration"
        ])
        self.status_adjustments = np.array([0.3, 1.0, 0.6, 1.0, 0.8, 1.2, 1.0, 0.5])
    
    def get_department_time(self, department):
        """Get base treatment time for department."""
        try:
            index = np.where(self.department_names == department)[0][0]
            return self.department_times[index]
        except IndexError:
            return 30  # Default
    
    def get_status_adjustment(self, treatment_status):
        """Get treatment status time adjustment."""
        try:
            index = np.where(self.status_names == treatment_status)[0][0]
            return self.status_adjustments[index]
        except IndexError:
            return 1.0  # Default