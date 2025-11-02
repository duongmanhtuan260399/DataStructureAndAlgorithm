from .DSALinkedList import DSALinkedList


class DSAStack:
    """
    A Stack implementation using DSALinkedList.
    
    This implementation uses a linked list to store elements, providing
    dynamic sizing and LIFO (Last In, First Out) behavior.
    """
    
    def __init__(self):
        """Initialize an empty stack using DSALinkedList."""
        self._stack = DSALinkedList()

    def is_empty(self):
        """
        Check if the stack is empty.
        
        Returns:
            bool: True if the stack has no elements, False otherwise.
        """
        return self._stack.isEmpty()
    
    def push(self, value):
        """
        Add an item to the top of the stack.
        
        Args:
            value: The item to be added.
        """
        # Insert at the beginning of the linked list (top of stack)
        self._stack.insertFirst(value)
    
    def pop(self):
        """
        Remove and return the item from the top of the stack.
        
        Returns:
            The item at the top of the stack.
            
        Raises:
            IndexError: If the stack is empty (stack underflow).
        """
        if self.is_empty():
            raise IndexError("Stack Underflow: Cannot pop from an empty stack.")
        
        # Get the top item and remove it from the beginning of the linked list
        return self._stack.removeFirst()
    
    def top(self):
        """
        Return the item at the top of the stack without removing it.
        
        Returns:
            The item at the top of the stack.
            
        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot get top from an empty stack.")
        
        # Peek at the first element without removing it
        return self._stack.peekFirst()
    
    def get_count(self):
        """Return the number of items currently in the stack."""
        return self._stack.getCount()
    
    def __len__(self):
        """Allow using the built-in len() function on the stack."""
        return self.get_count()
    
    def __str__(self):
        """Provide a user-friendly string representation of the stack."""
        if self.is_empty():
            return "[]"
        
        # Display the stack from top to bottom for intuitive representation
        # We'll traverse the linked list and build the string representation
        values = []
        current = self._stack._head
        while current is not None:
            values.append(str(current.value))
            current = current.next
        
        # Reverse to show top-to-bottom order
        values.reverse()
        return f"[{', '.join(values)}]"
