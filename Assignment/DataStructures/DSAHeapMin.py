import numpy as np

class DSAHeapMin:
    """
    Min-heap implementation for A* algorithm and other applications requiring min-heap behavior.
    Based on DSAHeap but modified to maintain min-heap property.
    """
    
    class DSAHeapEntry:
        def __init__(self, priority: int, value: object):
            self._priority = priority
            self._value = value
        def get_priority(self):
            return self._priority
        def get_value(self):
            return self._value

    def __init__(self, capacity: int = 5):
        self.heap = np.empty(capacity, dtype=object)
        self.count = 0

    def add(self, priority, value: object):
        if self.count == len(self.heap):
            # grow capacity (double)
            new_capacity = max(1, len(self.heap) * 2)
            new_heap = np.empty(new_capacity, dtype=object)
            for i in range(self.count):
                new_heap[i] = self.heap[i]
            self.heap = new_heap

        self.heap[self.count] = DSAHeapMin.DSAHeapEntry(priority, value)
        self._trickle_up(self.count)
        self.count += 1

    def remove(self):
        if self.count == 0:
            raise IndexError("Heap is empty")

        root_entry = self.heap[0]
        self.count -= 1
        if self.count > 0:
            self.heap[0] = self.heap[self.count]
            self.heap[self.count] = None
            self._trickle_down(0, self.count)
        else:
            self.heap[0] = None

        return root_entry.get_value()

    def display(self):
        print("[", end="")
        for i in range(self.count):
            entry = self.heap[i]
            print(f"({entry.get_priority()}, {entry.get_value()})", end="")
            if i < self.count - 1:
                print(", ", end="")
        print("]")

    def _trickle_up(self, index: int): 
        # Recursive trickle up to maintain min-heap property
        if index == 0:
            return
        parent_idx = (index - 1) // 2
        if self.heap[parent_idx].get_priority() > self.heap[index].get_priority():
            self.heap[parent_idx], self.heap[index] = self.heap[index], self.heap[parent_idx]
            self._trickle_up(parent_idx)

    def _trickle_down(self, curIdx: int, numItems: int):
        l_child_idx = (curIdx * 2) + 1
        r_child_idx = l_child_idx + 1
        if l_child_idx < numItems:
            small_idx = l_child_idx
            if r_child_idx < numItems:
                if self.heap[r_child_idx].get_priority() < self.heap[l_child_idx].get_priority():
                    small_idx = r_child_idx
            if self.heap[small_idx].get_priority() < self.heap[curIdx].get_priority():
                # swap
                self.heap[small_idx], self.heap[curIdx] = self.heap[curIdx], self.heap[small_idx]
                # recurse
                self._trickle_down(small_idx, numItems)

    def heapify(self):
        n = self.count
        if n <= 1:
            return
        for idx in range((n - 2) // 2, -1, -1):
            self._trickle_down(idx, n)

    def isEmpty(self):
        """Check if heap is empty."""
        return self.count == 0
    
    def is_empty(self):
        """Check if heap is empty (alias)."""
        return self.isEmpty()
    
    def getCount(self):
        """Get number of elements in heap."""
        return self.count
    
    def get_count(self):
        """Get number of elements in heap (alias)."""
        return self.getCount()
