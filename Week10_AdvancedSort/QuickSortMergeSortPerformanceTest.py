#!/usr/bin/env python3
"""
QuickSort and MergeSort Performance Test
Generates performance data for QuickSort and MergeSort algorithms
across different array types and sizes, similar to the simple sorts comparison.
"""

import numpy as np
import timeit
import DSAsorts
import random
import csv
import sys
# Allow deeper recursion for large arrays
sys.setrecursionlimit(1000000)

# Configuration
REPEATS = 3           # Number of times to run sorts to get mean time
NEARLY_PERCENT = 0.10 # Percentage of items to move in nearly sorted array
RANDOM_TIMES = 100    # Number of times to randomly swap elements in array

# Test sizes (smaller range to avoid recursion issues)
SIZES = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

# Array types
ARRAY_TYPES = {
    'a': 'Ascending',
    'd': 'Descending', 
    'r': 'Random',
    'n': 'Nearly Sorted'
}

# Sort algorithms to test (focusing on QuickSort and MergeSort)
SORT_ALGORITHMS = {
    'q': ('QuickSort', DSAsorts.quickSort),
    't': ('QuickSort Median3', DSAsorts.quickSortMedian3),
    'u': ('QuickSort Random', DSAsorts.quickSortRandom),
    'm': ('MergeSort', DSAsorts.mergeSort)
}

def create_array(n, array_type):
    """Create an array of size n with the specified type"""
    A = np.arange(1, n+1, 1)  # Create array with values from 1 to n
    
    if array_type == 'a':
        # Already ascending
        pass
    elif array_type == 'd':
        # Convert to descending
        A = A[::-1]
    elif array_type == 'r':
        # Randomize the array
        for i in range(RANDOM_TIMES * n):
            x = int(random.random() * n)
            y = int(random.random() * n)
            A[x], A[y] = A[y], A[x]
    elif array_type == 'n':
        # Nearly sorted (10% moved)
        for i in range(int(n * NEARLY_PERCENT / 2 + 1)):
            x = int(random.random() * n)
            y = int(random.random() * n)
            A[x], A[y] = A[y], A[x]
    
    return A

def time_sort_algorithm(sort_func, A):
    """Time a sorting algorithm on array A"""
    # Create a copy to avoid modifying the original
    test_array = A.copy()
    
    # Time the sorting
    start_time = timeit.default_timer()
    sort_func(test_array)
    end_time = timeit.default_timer()
    
    # Verify the array is sorted
    for i in range(len(test_array) - 1):
        if test_array[i] > test_array[i + 1]:
            raise ValueError(f"Array not properly sorted by {sort_func.__name__}")
    
    return end_time - start_time

def run_performance_test():
    """Run comprehensive performance tests"""
    results = {}
    
    print("Running QuickSort and MergeSort Performance Test...")
    print("=" * 60)
    
    for size in SIZES:
        print(f"Testing size: {size}")
        results[size] = {}
        
        for array_type_code, array_type_name in ARRAY_TYPES.items():
            print(f"  Array type: {array_type_name}")
            results[size][array_type_name] = {}
            
            # Create the test array
            test_array = create_array(size, array_type_code)
            
            for sort_code, (sort_name, sort_func) in SORT_ALGORITHMS.items():
                print(f"    Testing {sort_name}...")
                
                # Run multiple times and average (discard first run)
                times = []
                for repeat in range(REPEATS):
                    time_taken = time_sort_algorithm(sort_func, test_array)
                    times.append(time_taken)
                
                # Average time (discard first run)
                avg_time = sum(times[1:]) / (REPEATS - 1)
                results[size][array_type_name][sort_name] = avg_time
                
                print(f"      Average time: {avg_time:.6f} seconds")
    
    return results

def save_results_to_csv(results, filename):
    """Save results to CSV file"""
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Wide header similar to the provided template
        array_type_order = ['Ascending', 'Nearly Sorted', 'Random', 'Descending']
        sort_order = ['QuickSort', 'QuickSort Median3', 'QuickSort Random', 'MergeSort']

        # First header row: group labels for array types
        header_top = ['Size']
        for at in array_type_order:
            header_top.extend([at, '', '', ''])
        writer.writerow(header_top)

        # Second header row: algorithm names under each group
        header_sub = ['']
        for _ in array_type_order:
            header_sub.extend(sort_order)
        writer.writerow(header_sub)
        
        # Rows: one per size, values arranged by array type groups and algorithms
        for size in SIZES:
            row = [size]
            for at in array_type_order:
                for sort_name in sort_order:
                    row.append(f"{results[size][at][sort_name]:.6f}")
            writer.writerow(row)
    
    print(f"Results saved to {filename}")

def create_comparison_table(results):
    """Create a formatted comparison table"""
    print("\n" + "=" * 100)
    print("QUICKSORT AND MERGESORT PERFORMANCE COMPARISON")
    print("=" * 100)
    
    # Create table structure similar to your existing data
    for array_type in ARRAY_TYPES.values():
        print(f"\n{array_type.upper()} ARRAYS:")
        print("-" * 80)
        print(f"{'Size':<6} {'QuickSort':<12} {'QuickSort M3':<12} {'QuickSort R':<12} {'MergeSort':<12}")
        print("-" * 80)
        
        for size in SIZES:
            row = f"{size:<6}"
            for sort_name in ['QuickSort', 'QuickSort Median3', 'QuickSort Random', 'MergeSort']:
                time_val = results[size][array_type][sort_name]
                row += f" {time_val:<12.6f}"
            print(row)

def main():
    """Main function"""
    print("QuickSort and MergeSort Performance Test")
    print("Testing QuickSort, QuickSort Median3, QuickSort Random, and MergeSort")
    print("Array types: Ascending, Descending, Random, Nearly Sorted")
    print("Sizes: 1, 2, 4, 8, 16, 32, 64, 128, 256, 512")
    print()
    
    # Run performance tests
    results = run_performance_test()
    
    # Display results
    create_comparison_table(results)
    
    # Save to CSV
    csv_filename = "QuickSortMergeSortPerformanceResults.csv"
    save_results_to_csv(results, csv_filename)
    
    print(f"\nPerformance test completed!")
    print(f"Results saved to: {csv_filename}")

if __name__ == "__main__":
    main()
