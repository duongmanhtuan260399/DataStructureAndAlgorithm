import numpy as np


class DSAStack:
    """
    A class representing a Stack data structure.

    This implementation uses a fixed-size NumPy array to store elements
    and an integer count to track the number of items.
    """
    DEFAULT_CAPACITY = 100

    def __init__(self, capacity=None):
        """
        Initializes the stack.

        Args:
            capacity (int, optional): The maximum number of elements the stack
                                      can hold. Defaults to 100.
        """
        if capacity is None:
            self._capacity = self.DEFAULT_CAPACITY
        elif not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Capacity must be a positive integer.")
        else:
            self._capacity = capacity

        # Create a NumPy array that can hold any Python object.
        self._stack = np.empty(self._capacity, dtype=object)

        # Use an integer to track the number of elements.
        # A value of 0 implies the stack is empty.
        self._count = 0

    def get_capacity(self):
        return self._capacity

    def get_count(self):
        """Returns the number of items currently in the stack."""
        return self._count

    def is_empty(self):
        """
        Checks if the stack is empty.

        Returns:
            bool: True if the stack has no elements, False otherwise.
        """
        return self._count == 0

    def is_full(self):
        """
        Checks if the stack is full.

        Returns:
            bool: True if the stack has reached its capacity, False otherwise.
        """
        return self._count == self._capacity

    def push(self, value):
        """
        Adds an item to the top of the stack.

        Args:
            value: The item to be added.

        Raises:
            ValueError: If the stack is full (stack overflow).
        """
        if self.is_full():
            raise ValueError("Stack Overflow: Cannot push to a full stack.")

        # Add the new value at the current count index.
        self._stack[self._count] = value
        # Increment the count.
        self._count += 1

    def pop(self):
        """
        Removes and returns the item from the top of the stack.

        Returns:
            The item at the top of the stack.

        Raises:
            IndexError: If the stack is empty (stack underflow).
        """
        if self.is_empty():
            raise IndexError("Stack Underflow: Cannot pop from an empty stack.")

        # Get the top item before decrementing the count.
        top_item = self.top()
        # Decrementing the count effectively "removes" the top item.
        self._count -= 1
        return top_item

    def top(self):
        """
        Returns the item at the top of the stack without removing it.

        Returns:
            The item at the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot get top from an empty stack.")

        # The top element is at the index 'count - 1'.
        return self._stack[self._count - 1]

    def __len__(self):
        """Allows using the built-in len() function on the stack."""
        return self._count

    def __str__(self):
        """Provides a user-friendly string representation of the stack."""
        if self.is_empty():
            return "[]"

        # Displays the stack from top to bottom for intuitive representation.
        items = [str(self._stack[i]) for i in range(self._count - 1, -1, -1)]
        return f"[{', '.join(items)}]"