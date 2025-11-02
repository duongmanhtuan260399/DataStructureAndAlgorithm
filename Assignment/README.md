# Hospital Management System

## Module 1: Hospital Navigation System

```bash
# Run the main application
python hospital_main.py

# Select option 1: Hospital Navigation (Module 1)
```

### Expected Results
- Shortest path finding using A* algorithm
- Reachable departments using BFS traversal
- Cycle detection using DFS
- Hospital map visualization

## Module 2: Patient Management System
This module includes three sub-modules:  
- 2.1 Patient Lookup  
- 2.2 Treatment Scheduler  
- 2.3 Patient Record Sorting  

### Running Module 2
```bash
# Run the main application
python hospital_main.py

# Select option 2: Patient Management System (Module 2)
```
## 2.1. Patient Lookup
### Running Patient Lookup Module
```bash
# Run the main application
python hospital_main.py

# Select: 2 → 2.1
```

### Expected Results
- Patient lookup with O(1) average case complexity
- Hash table collision handling with linear probing
- Load factor management (grows at 0.7, shrinks at 0.2)
- Patient record insertion, search, and deletion

## 2.2 Treatment Scheduler

**Priority Heap Implementation** - Patient prioritization, treatment queue management

### Running Treatment Scheduler

```bash
# Run main application
python hospital_main.py
# Select: 2 → 2.2
```

### Expected Results
- Priority heap maintains correct ordering
- Patients extracted in priority order (highest first)
- Priority calculation: (6 - Urgency) + 1000 / TreatmentTime
- Heap property maintained after insertions and extractions
- O(log n) insertion and extraction complexity

## 2.3: Patient Record Sorting

**Sorting Algorithms Implementation** - Merge Sort, Quick Sort, performance comparison

### Running Sorting Module

```bash
# Run main application
python hospital_main.py

# Select: 2 → 2.3
```

### Expected Results
- Merge Sort: O(n log n) guaranteed time complexity
- Quick Sort variants: O(n log n) average, O(n²) worst case
- Performance comparison between algorithms
- Execution time measurements for different dataset sizes
- Sorting by treatment time in ascending order