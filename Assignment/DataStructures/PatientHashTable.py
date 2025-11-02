from DataStructures.DSAHashTable import DSAHashTable
from model.PatientRecord import PatientRecord

class PatientHashTable(DSAHashTable):
    def __init__(self, capacity=None, probing_mode="linear"):
        super().__init__(capacity, probing_mode)
        # Initialize _debug attribute if not already set
        if not hasattr(self, '_debug'):
            self._debug = False

    def insert(self, record: PatientRecord):
        """Insert a patient record or update if duplicate found."""
        print(f"\nInserting patient ID {record.get_patient_id()}")
        if self.hasKey(record.get_patient_id()):
            print(f"Patient ID {record.get_patient_id()} already exists. Updating record.")
        self.put(record.get_patient_id(), record)

    def search(self, patient_id: str) -> PatientRecord:
        """Search for a patient by ID, return record or not found message."""
        try:
            return self.get(patient_id)
        except KeyError:
            print(f"Patient ID {patient_id} not found.")
            return None

    def delete(self, patient_id: str) -> PatientRecord:
        """Delete a patient record by ID, confirm deletion or handle missing key."""
        try:
            removed_record = self.remove(patient_id)
            print(f"Patient ID {patient_id} has been removed.")
            return removed_record
        except KeyError:
            print(f"Patient ID {patient_id} not found, cannot be deleted.")
            return None
