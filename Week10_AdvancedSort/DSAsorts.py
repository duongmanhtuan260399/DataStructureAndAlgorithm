#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#
import numpy as np

# 1)
def bubbleSort(A):
    #Outer loop:  len(A) - 1 pass
    for n in range(len(A) - 1):
        swapped = False
        #Inner loop: swaps per each pass
        for i in range(len(A)-1-n):
            # Bubble up the larger number
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                #If there's a swap, change the flag to True
                swapped = True
        # No swap, array already sorted, escape the loop
        if not swapped:
            break
    return A

# 2)
def insertionSort(A):
    # Loop through the array
    for i in range(1,len(A)):
        # Keep a marker to swap with items to the left
        marker = i
        # Swap the marker backwards until it reaches the minimum position
        while marker > 0 and A[marker-1] > A[marker]:
            A[marker], A[marker-1] = A[marker-1], A[marker]
            marker-=1
    return A

# 3)
def selectionSort(A):
    # Loop through the array
    for i in range(len(A)):
        # Find the minimum number
        minIdx = i
        for j in range(i + 1, len(A)):
            if A[j] < A[minIdx]:
                minIdx = j
        # Swap the minimum number with the ith position
        A[i],A[minIdx] = A[minIdx],A[i]
    return A

def mergeSort(A):
    if len(A) > 1:
        mergeSortRecurse(A, 0, len(A) - 1)
    return A

def mergeSortRecurse(A, leftIdx, rightIdx):
    """ Recursively divide the array and merge sorted halves
    """
    if leftIdx < rightIdx:
        midIdx = (leftIdx + rightIdx) // 2
        mergeSortRecurse(A, leftIdx, midIdx)
        mergeSortRecurse(A, midIdx + 1, rightIdx)
        merge(A, leftIdx, midIdx, rightIdx)

def merge(A, leftIdx, midIdx, rightIdx):
    # Create temporary arrays for left and right halves using numpy
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

def quickSort(A):
    if len(A) > 1:
        quickSortRecurse(A, 0, len(A) - 1)
    return A

def quickSortRecurse(A, leftIdx, rightIdx):
    if leftIdx < rightIdx:
        pivotIdx = doPartitioning(A, leftIdx, rightIdx, (leftIdx + rightIdx) // 2)
        # Recursively sort elements before and after partition
        quickSortRecurse(A, leftIdx, pivotIdx - 1)
        quickSortRecurse(A, pivotIdx + 1, rightIdx)

def doPartitioning(A, leftIdx, rightIdx, pivotIdx):
    # Follow pseudocode exactly
    pivotValue = A[pivotIdx]
    
    # Swap pivot with right-most element
    A[pivotIdx], A[rightIdx] = A[rightIdx], A[pivotIdx]
    
    # Find all values smaller than the pivot and move them to the left-hand side
    currIdx = leftIdx
    for ii in range(leftIdx, rightIdx):  # up to rightIdx-1
        if A[ii] < pivotValue:  # strict < for stability per pseudocode intent
            A[ii], A[currIdx] = A[currIdx], A[ii]
            currIdx += 1
    
    # Put the pivot into its rightful place
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

def quickSortRandom(A):
    if len(A) > 1:
        quickSortRandomRecurse(A, 0, len(A) - 1)
    return A

def quickSortRandomRecurse(A, leftIdx, rightIdx):
    if leftIdx < rightIdx:
        # Use random pivot selection
        pivotIdx = randomPivot(A, leftIdx, rightIdx)
        # Partition the array and get the pivot index
        pivotIdx = doPartitioning(A, leftIdx, rightIdx, pivotIdx)
        # Recursively sort elements before and after partition
        quickSortRandomRecurse(A, leftIdx, pivotIdx - 1)
        quickSortRandomRecurse(A, pivotIdx + 1, rightIdx)

def randomPivot(A, leftIdx, rightIdx):
    """ Select a random element as pivot
    Returns the index of a randomly selected element
    """
    import random
    return random.randint(leftIdx, rightIdx)


