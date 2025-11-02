class DSALinkedList:
    """
    A doubly linked list implementation with DSAListNode as a private class.
    Supports insertion at first/last positions, removal from first/last positions,
    and peek operations.
    """
    
    class _DSAListNode:
        """
        Private class representing a node in the linked list.
        Each node contains a value and references to the next and previous nodes.
        """
        def __init__(self, value):
            self.value = value
            self.next = None
            self.prev = None
    
    def __init__(self):
        """Initialize an empty linked list."""
        self._head = None
        self._tail = None
        self._count = 0
    
    def isEmpty(self):
        """Check if the linked list is empty."""
        return self._head is None
    
    def getCount(self):
        """Return the number of elements in the linked list."""
        return self._count
    
    def __len__(self):
        """Return the number of elements in the linked list (for len() support)."""
        return self._count
    
    def insertFirst(self, value):
        """
        Insert a new node with the given value at the beginning of the list.
        Handles three cases:
        (a) Empty list
        (b) One-item list  
        (c) Multi-item list
        """
        new_node = self._DSAListNode(value)
        
        if self.isEmpty():
            # Case (a): Empty list
            self._head = new_node
            self._tail = new_node
        else:
            # Case (b) and (c): One-item or multi-item list
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node
        
        self._count += 1
    
    def insertLast(self, value):
        """
        Insert a new node with the given value at the end of the list.
        """
        new_node = self._DSAListNode(value)
        
        if self.isEmpty():
            # Empty list case
            self._head = new_node
            self._tail = new_node
        else:
            # Non-empty list case
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node
        
        self._count += 1
    
    def removeFirst(self):
        """
        Remove and return the value of the first node in the list.
        Handles three cases explicitly:
        (a) Empty list - raises exception
        (b) One-item list - special case (both first and last)
        (c) Multi-item list - normal case
        """
        if self.isEmpty():
            raise ValueError("Cannot remove from empty list")
        
        value = self._head.value
        
        if self._head == self._tail:
            # Case (b): One-item list (special case)
            self._head = None
            self._tail = None
        else:
            # Case (c): Multi-item list
            self._head = self._head.next
            self._head.prev = None
        
        self._count -= 1
        return value
    
    def removeLast(self):
        """
        Remove and return the value of the last node in the list.
        """
        if self.isEmpty():
            raise ValueError("Cannot remove from empty list")
        
        value = self._tail.value
        
        if self._head == self._tail:
            # One-item list case
            self._head = None
            self._tail = None
        else:
            # Multi-item list case
            self._tail = self._tail.prev
            self._tail.next = None
        
        self._count -= 1
        return value
    
    def peekFirst(self):
        """
        Return the value of the first node without removing it.
        """
        if self.isEmpty():
            raise ValueError("Cannot peek at empty list")
        return self._head.value
    
    def peekLast(self):
        """
        Return the value of the last node without removing it.
        """
        if self.isEmpty():
            raise ValueError("Cannot peek at empty list")
        return self._tail.value

    def display(self):
        """
        Display the contents of the linked list from head to tail
        without using any list methods.
        """
        if self.isEmpty():
            print("List is empty")
            return

        current = self._head
        # Iterate through the list and print each value
        while current is not None:
            print(current.value, end=" -> ")
            current = current.next

        # Print "None" to signify the end of the list
        print("None")

    
    
    def remove(self, valueToFind):
        """
        Remove the first occurrence of valueToFind from the list.
        Returns the value that was removed.
        If valueToFind is not found, raises ValueError.
        """
        if self.isEmpty():
            raise ValueError(f"Value {valueToFind} not found in empty list")
        
        # Find the node with valueToFind
        current = self._head
        while current is not None:
            if current.value == valueToFind:
                break
            current = current.next
        
        if current is None:
            raise ValueError(f"Value {valueToFind} not found in list")
        
        value = current.value
        
        # Remove the node
        if current == self._head and current == self._tail:
            # One-item list
            self._head = None
            self._tail = None
        elif current == self._head:
            # First node
            self._head = current.next
            self._head.prev = None
        elif current == self._tail:
            # Last node
            self._tail = current.prev
            self._tail.next = None
        else:
            # Middle node
            current.prev.next = current.next
            current.next.prev = current.prev
        
        self._count -= 1
        return value
    
    
    def find(self, valueToFind):
        """
        Find the first occurrence of valueToFind in the list.
        Returns True if found, False otherwise.
        """
        if self.isEmpty():
            return False
        
        current = self._head
        while current is not None:
            if current.value == valueToFind:
                return True
            current = current.next
        
        return False

    def __iter__(self):
        """Iterate through values from head to tail without exposing nodes."""
        current = self._head
        while current is not None:
            yield current.value
            current = current.next
