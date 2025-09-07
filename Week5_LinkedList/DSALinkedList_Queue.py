from DSALinkedList import DSALinkedList


class DSAQueue:
    """
    A Queue implementation using DSALinkedList.
    """
    
    def __init__(self):
        """Initialize an empty queue using DSALinkedList."""
        self._queue = DSALinkedList()
    
    def is_empty(self):
        """
        Check if the queue is empty.
        
        Returns:
            bool: True if the queue has no elements, False otherwise.
        """
        return self._queue.isEmpty()
    
    def enqueue(self, value):
        """
        Add an item to the rear of the queue.
        
        Args:
            value: The item to be added.
        """
        # Insert at the end of the linked list (rear of queue)
        self._queue.insertLast(value)
    
    def dequeue(self):
        """
        Remove and return the item from the front of the queue.
        
        Returns:
            The item at the front of the queue.
            
        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Queue Underflow: Cannot dequeue from an empty queue.")
        
        # Remove and return the first element
        return self._queue.removeFirst()
    
    def peek(self):
        """
        Return the item at the front of the queue without removing it.
        
        Returns:
            The item at the front of the queue.
            
        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot peek at an empty queue.")
        
        # Peek at the first element without removing it
        return self._queue.peekFirst()
    
    def get_count(self):
        """Return the number of items currently in the queue."""
        return self._queue.getCount()
    
    def __len__(self):
        """Allow using the built-in len() function on the queue."""
        return self.get_count()
    
    def __str__(self):
        """Provide a user-friendly string representation of the queue."""
        if self.is_empty():
            return "[]"
        
        # Display the queue from front to rear
        # We'll traverse the linked list and build the string representation
        values = []
        current = self._queue._head
        while current is not None:
            values.append(str(current.value))
            current = current.next
        
        return f"[{' '.join(values)}]"
