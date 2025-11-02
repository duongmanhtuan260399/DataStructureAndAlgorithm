#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#
import numpy as np


def mergeSort(A):
    if len(A) > 1:
        mergeSortRecurse(A, 0, len(A) - 1)
    return A

def mergeSortRecurse(A, leftIdx, rightIdx):
    if leftIdx < rightIdx:
        midIdx = (leftIdx + rightIdx) // 2
        mergeSortRecurse(A, leftIdx, midIdx)
        mergeSortRecurse(A, midIdx + 1, rightIdx)
        merge(A, leftIdx, midIdx, rightIdx)

def merge(A, leftIdx, midIdx, rightIdx):
    leftSize = midIdx - leftIdx + 1
    rightSize = rightIdx - midIdx
    
    leftArray = np.zeros(leftSize, dtype=A.dtype)
    rightArray = np.zeros(rightSize, dtype=A.dtype)
    
    for i in range(leftSize):
        leftArray[i] = A[leftIdx + i]
    for j in range(rightSize):
        rightArray[j] = A[midIdx + 1 + j]
    
    # Merge the temporary arrays back into A
    i = 0  # Initial index of left subarray
    j = 0  # Initial index of right subarray
    k = leftIdx  # Initial index of merged subarray
    
    while i < leftSize and j < rightSize:
        if leftArray[i] <= rightArray[j]:
            A[k] = leftArray[i]
            i += 1
        else:
            A[k] = rightArray[j]
            j += 1
        k += 1
    
    # Copy remaining elements of leftArray if any
    while i < leftSize:
        A[k] = leftArray[i]
        i += 1
        k += 1
    
    # Copy remaining elements of rightArray if any
    while j < rightSize:
        A[k] = rightArray[j]
        j += 1
        k += 1


def doPartitioning(A, leftIdx, rightIdx, pivotIdx):
    # Follow pseudocode exactly
    pivotValue = A[pivotIdx]
    
    # Swap pivot with right-most element
    A[pivotIdx], A[rightIdx] = A[rightIdx], A[pivotIdx]
    
    # Find all values smaller than the pivot and move them to the left-hand side
    currIdx = leftIdx
    for ii in range(leftIdx, rightIdx):
        if A[ii] < pivotValue: 
            A[ii], A[currIdx] = A[currIdx], A[ii]
            currIdx += 1
    
    newPivotIdx = currIdx
    A[rightIdx], A[newPivotIdx] = A[newPivotIdx], A[rightIdx]
    return newPivotIdx

def quickSortMedian3(A):
    if len(A) > 1:
        quickSortMedian3Recurse(A, 0, len(A) - 1)
    return A

def quickSortMedian3Recurse(A, leftIdx, rightIdx):
    if leftIdx < rightIdx:
        # Use median-of-three pivot selection
        pivotIdx = medianOfThree(A, leftIdx, rightIdx)
        # Partition the array and get the pivot index
        pivotIdx = doPartitioning(A, leftIdx, rightIdx, pivotIdx)
        # Recursively sort elements before and after partition
        quickSortMedian3Recurse(A, leftIdx, pivotIdx - 1)
        quickSortMedian3Recurse(A, pivotIdx + 1, rightIdx)

def medianOfThree(A, leftIdx, rightIdx):
    midIdx = (leftIdx + rightIdx) // 2
    
    # Get the three values
    first = A[leftIdx]
    middle = A[midIdx]
    last = A[rightIdx]
    
    # Find the median value
    if (first <= middle <= last) or (last <= middle <= first):
        return midIdx
    elif (middle <= first <= last) or (last <= first <= middle):
        return leftIdx
    else:
        return rightIdx



