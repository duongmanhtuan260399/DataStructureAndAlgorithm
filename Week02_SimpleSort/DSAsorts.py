#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#

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
    print(f"Sorted array: {A}")
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
    print(f"Sorted array: {A}")
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
    print(f"Sorted array: {A}")
    return A

def mergeSort(A):
    """ mergeSort - front-end for kick-starting the recursive algorithm
    """
    ...

def mergeSortRecurse(A, leftIdx, rightIdx):
    ...

def merge(A, leftIdx, midIdx, rightIdx):
    ...

def quickSort(A):
    """ quickSort - front-end for kick-starting the recursive algorithm
    """
    ...

def quickSortRecurse(A, leftIdx, rightIdx):
    ...

def doPartitioning(A, leftIdx, rightIdx, pivotIdx):
    ...


