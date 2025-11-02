# Hospital Management System - Sample Input and Output

This document provides sample input and output scenarios for each module of the Hospital Management System.

## Module 1: Hospital Navigation System

### 1.1 Hospital Configuration Input

**Input File:** `config/hospital_config.json`

```json
[
  {
    "department": "Emergency",
    "corridors": [
      {
        "department": "Reception",
        "weight": 10
      },
      {
        "department": "ICU",
        "weight": 5
      }
    ]
  },
  {
    "department": "Reception",
    "corridors": [
      {
        "department": "Emergency",
        "weight": 10
      },
      {
        "department": "Outpatient",
        "weight": 8
      },
      {
        "department": "Pharmacy",
        "weight": 12
      }
    ]
  },
  {
    "department": "ICU",
    "corridors": [
      {
        "department": "Emergency",
        "weight": 5
      },
      {
        "department": "Operating Theatre",
        "weight": 7
      },
      {
        "department": "Radiology",
        "weight": 15
      }
    ]
  },
  {
    "department": "Outpatient",
    "corridors": [
      {
        "department": "Reception",
        "weight": 8
      },
      {
        "department": "Laboratory",
        "weight": 6
      }
    ]
  },
  {
    "department": "Pharmacy",
    "corridors": [
      {
        "department": "Reception",
        "weight": 12
      },
      {
        "department": "Laboratory",
        "weight": 4
      }
    ]
  },
  {
    "department": "Laboratory",
    "corridors": [
      {
        "department": "Outpatient",
        "weight": 6
      },
      {
        "department": "Pharmacy",
        "weight": 4
      },
      {
        "department": "Radiology",
        "weight": 9
      }
    ]
  },
  {
    "department": "Radiology",
    "corridors": [
      {
        "department": "ICU",
        "weight": 15
      },
      {
        "department": "Laboratory",
        "weight": 9
      },
      {
        "department": "Operating Theatre",
        "weight": 8
      }
    ]
  },
  {
    "department": "Operating Theatre",
    "corridors": [
      {
        "department": "ICU",
        "weight": 7
      },
      {
        "department": "Radiology",
        "weight": 8
      },
      {
        "department": "Wards",
        "weight": 12
      }
    ]
  },
  {
    "department": "Wards",
    "corridors": [
      {
        "department": "Operating Theatre",
        "weight": 12
      }
    ]
  },
  {
    "department": "Isolated Department",
    "corridors": []
  }
]
```

### 1.2 Shortest Path Finding (A* Algorithm)

**Input Scenarios:**

| Scenario | Start | End | Expected Path | Expected Cost |
|----------|-------|-----|---------------|---------------|
| Emergency to Pharmacy | Emergency | Pharmacy | Emergency → Reception → Pharmacy | 22 minutes |
| Reception to ICU | Reception | ICU | Reception → Emergency → ICU | 15 minutes |
| Outpatient to Operating Theatre | Outpatient | Operating Theatre | Outpatient → Laboratory → Radiology → Operating Theatre | 23 minutes |
| Laboratory to Wards | Laboratory | Wards | Laboratory → Radiology → Operating Theatre → Wards | 29 minutes |
| Isolated to Emergency | Isolated Department | Emergency | No path found | N/A |

**Sample Output:**
```
SHORTEST PATH: Reception → ICU
==================================================
Path: Reception → Emergency → ICU
Total Walking Time: 15 minutes
Number of Corridors: 2

Step-by-Step Directions:
   1. From Reception to Emergency
   2. From Emergency to ICU

============================================================
```

### 1.3 Reachable Departments (BFS)

**Input:** Start from Emergency Department

**Expected Output:**
```
REACHABLE DEPARTMENTS FROM: Emergency
==================================================

Level 0 (Walking time: 0 corridors away):
   Departments: Emergency

Level 1 (Walking time: 1 corridors away):
   Departments: Reception, ICU

Level 2 (Walking time: 2 corridors away):
   Departments: Outpatient, Pharmacy, Operating Theatre, Radiology

Level 3 (Walking time: 3 corridors away):
   Departments: Laboratory, Wards

============================================================
```

### 1.4 Cycle Detection (DFS)

**Input:** Start from Emergency Department

**Expected Output:**
```
CYCLE DETECTION FROM: Emergency
==================================================
1 cycle(s) found that include 'Emergency':
   Cycle 1: Emergency → Reception → Outpatient → Laboratory → Radiology → ICU → Emergency

============================================================
```

### 1.5 Hospital Map Display

**Expected Output:**
```
HOSPITAL FLOOR PLAN
==================================================
Weighted Undirected Graph: |V|=10, |E|=11
Emergency: [Reception(10), ICU(5)]
Reception: [Emergency(10), Outpatient(8), Pharmacy(12)]
ICU: [Emergency(5), Operating Theatre(7), Radiology(15)]
Outpatient: [Reception(8), Laboratory(6)]
Pharmacy: [Reception(12), Laboratory(4)]
Laboratory: [Outpatient(6), Pharmacy(4), Radiology(9)]
Radiology: [ICU(15), Laboratory(9), Operating Theatre(8)]
Operating Theatre: [ICU(7), Radiology(8), Wards(12)]
Wards: [Operating Theatre(12)]
Isolated Department: []

============================================================
```

## Module 2: Patient Management System

### 2.1 Patient Configuration Input

**Input File:** `config/patient_config.json`

```json
[
  {
    "patient_id": 1,
    "name": "John Smith",
    "age": 45,
    "department": "Emergency",
    "urgency_level": 5,
    "treatment_status": "Critical"
  },
  {
    "patient_id": 2,
    "name": "Jane Doe",
    "age": 32,
    "department": "Outpatient",
    "urgency_level": 2,
    "treatment_status": "Waiting"
  },
  {
    "patient_id": 3,
    "name": "Bob Johnson",
    "age": 67,
    "department": "ICU",
    "urgency_level": 4,
    "treatment_status": "Stable"
  },
  {
    "patient_id": 4,
    "name": "Alice Brown",
    "age": 28,
    "department": "Radiology",
    "urgency_level": 3,
    "treatment_status": "Under Treatment"
  },
  {
    "patient_id": 5,
    "name": "Charlie Wilson",
    "age": 55,
    "department": "Operating Theatre",
    "urgency_level": 5,
    "treatment_status": "Under Treatment"
  },
  {
    "patient_id": 6,
    "name": "Diana Lee",
    "age": 41,
    "department": "Laboratory",
    "urgency_level": 1,
    "treatment_status": "Test Results"
  },
  {
    "patient_id": 7,
    "name": "Eva Garcia",
    "age": 29,
    "department": "Pharmacy",
    "urgency_level": 2,
    "treatment_status": "Medication"
  },
  {
    "patient_id": 8,
    "name": "Frank Miller",
    "age": 73,
    "department": "Wards",
    "urgency_level": 3,
    "treatment_status": "Recovery"
  },
  {
    "patient_id": 9,
    "name": "Grace Taylor",
    "age": 36,
    "department": "Reception",
    "urgency_level": 1,
    "treatment_status": "Registration"
  },
  {
    "patient_id": 10,
    "name": "Henry Davis",
    "age": 52,
    "department": "Emergency",
    "urgency_level": 4,
    "treatment_status": "Critical"
  }
]
```

### 2.2 Patient Lookup (Hash Table Operations)

**Input Scenarios:**

| Operation | Patient ID | Expected Result | Complexity |
|-----------|------------|-----------------|------------|
| Search Hit | 1 | John Smith found | O(1) average |
| Search Hit | 5 | Charlie Wilson found | O(1) average |
| Search Miss | 15 | Patient not found | O(1) average |
| Search Miss | 99 | Patient not found | O(1) average |
| Insert New | 11 | Ivy Chen inserted | O(1) average |
| Delete | 3 | Bob Johnson deleted | O(1) average |

**Sample Output:**
```
============================================================
Enter Patient ID to search: 1

Patient Record:
----------------------------------------
ID: 1
Name: John Smith
Age: 45
Department: Emergency
Urgency Level: 5
Treatment Status: Critical
Treatment Time: 13 minutes
----------------------------------------

# Insert new patient
Enter Patient ID: 100
Enter Patient Name: David
Enter Patient Age: 40
Enter Department: Outpatient
Enter Urgency Level (1-5): 4
Enter Treatment Status: Medical
Success: Patient 100 added successfully.

# Remove existing patient
Enter Patient ID to remove: 5
Patient ID 5 has been removed.
Success: Patient 5 removed successfully.
```

---

## Module 3: Treatment Scheduler

### 3.1 Priority Heap Operations

**Priority Calculation Formula:** `(6 - Urgency) + 1000 / TreatmentTime`

**Input Scenarios:**

| Patient | Urgency | Treatment Time | Priority | Position |
|---------|---------|----------------|----------|----------|
| John Smith | 5 | 30 min | 1.033 | Top of heap |
| Alice Brown | 3 | 60 min | 3.017 | Middle of heap |
| Diana Lee | 1 | 120 min | 5.008 | Bottom of heap |
| Charlie Wilson | 5 | 180 min | 1.006 | Top of heap |
| Grace Taylor | 1 | 15 min | 5.067 | Middle of heap |

**Sample Output:**
```
NEXT PATIENT IN TREATMENT QUEUE
==================================================

Patient Record:
----------------------------------------
ID: 9
Name: Grace Taylor
Age: 36
Department: Reception
Urgency Level: 1
Treatment Status: Registration
Treatment Time: 2 minutes
----------------------------------------
Priority Score: 505.00
==================================================
```

## Module 4: Patient Record Sorting

### 4.1 Sorting Algorithm Performance

**Input:** 1000 patient records sorted by treatment time


**Sample Output:**
```
PERFORMANCE COMPARISON
================================================================================
Algorithm                 Time (seconds)  Patients  
--------------------------------------------------------------------------------
Merge Sort                0.009080        1030      
Quick Sort (Median of Three) 0.005344        1030      

Fastest Algorithm: Quick Sort (Median of Three) (0.005344 seconds)
```
