import numpy as np
class DSAHeap:
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
        self._debug = False

    def add(self, priority, value: object):
        if self.count == len(self.heap):
            # grow capacity (double)
            new_capacity = max(1, len(self.heap) * 2)
            new_heap = np.empty(new_capacity, dtype=object)
            for i in range(self.count):
                new_heap[i] = self.heap[i]
            self.heap = new_heap

        self.heap[self.count] = DSAHeap.DSAHeapEntry(priority, value)
        if self._debug:
            print(f"[HEAP ADD] Adding priority={priority}, value={value}")
            print("Heap state before trickle_up: ", end="")
            self.display()
        
        self._trickle_up(self.count)
        self.count += 1
        
        if self._debug:
            print(f"Heap state after insert (count={self.count}): ", end="")
            self.display()
            print()

    def remove(self):
        if self.count == 0:
            raise IndexError("Heap is empty")

        root_entry = self.heap[0]
        if self._debug:
            print(f"[HEAP REMOVE] Removing root with priority={root_entry.get_priority()}, value={root_entry.get_value()}")
            print(f"Heap state before removal (count={self.count}): ", end="")
            self.display()
        
        self.count -= 1
        if self.count > 0:
            self.heap[0] = self.heap[self.count]
            self.heap[self.count] = None
            self._trickle_down(0, self.count)
        else:
            self.heap[0] = None

        if self._debug:
            print(f"Heap state after remove (count={self.count}): ", end="")
            self.display()
            print()
        
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
        # Recursive trickle up to maintain max-heap property
        if index == 0:
            return
        parent_idx = (index - 1) // 2
        if self.heap[parent_idx].get_priority() < self.heap[index].get_priority():
            self.heap[parent_idx], self.heap[index] = self.heap[index], self.heap[parent_idx]
            self._trickle_up(parent_idx)

    def _trickle_down(self, curIdx: int, numItems: int):
        l_child_idx = (curIdx * 2) + 1
        r_child_idx = l_child_idx + 1
        if l_child_idx < numItems:
            large_idx = l_child_idx
            if r_child_idx < numItems:
                if self.heap[r_child_idx].get_priority() > self.heap[l_child_idx].get_priority():
                    large_idx = r_child_idx
            if self.heap[large_idx].get_priority() > self.heap[curIdx].get_priority():
                # swap
                self.heap[large_idx], self.heap[curIdx] = self.heap[curIdx], self.heap[large_idx]
                # recurse
                self._trickle_down(large_idx, numItems)

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
    
    def set_debug(self, enabled):
        """Enable or disable debug logging."""
        self._debug = bool(enabled)