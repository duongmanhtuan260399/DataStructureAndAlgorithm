import numpy as np
from abc import ABC, abstractmethod


class DSAQueue(ABC):
    """
    Abstract base class representing a Queue data structure.

    This class defines the interface that all queue implementations must follow.
    """

    # Default capacity if none is provided by the user.
    DEFAULT_CAPACITY = 100

    def __init__(self, capacity=None):
        """
        Initializes the queue.

        Args:
            capacity (int, optional): The maximum number of elements the queue
                                      can hold. Defaults to 100.
        """
        if capacity is None:
            self._capacity = self.DEFAULT_CAPACITY
        elif not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Capacity must be a positive integer.")
        else:
            self._capacity = capacity

        # Create a NumPy array that can hold any Python object.
        self._queue = np.empty(self._capacity, dtype=object)

        # Use an integer to track the number of elements.
        # A value of 0 implies the queue is empty.
        self._count = 0

    def get_capacity(self):
        """Returns the maximum capacity of the queue."""
        return self._capacity

    def get_count(self):
        """Returns the number of items currently in the queue."""
        return self._count

    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns:
            bool: True if the queue has no elements, False otherwise.
        """
        return self._count == 0

    def is_full(self):
        """
        Checks if the queue is full.

        Returns:
            bool: True if the queue has reached its capacity, False otherwise.
        """
        return self._count == self._capacity

    def enqueue(self, value):
        """
        Adds an item to the rear of the queue.

        Args:
            value: The item to be added.

        Raises:
            ValueError: If the queue is full.
        """
        if self.is_full():
            raise ValueError("Queue Overflow: Cannot enqueue to a full queue.")

        # Get the rear position from the subclass
        rear_pos = self._get_rear_position()
        
        # Add the new value at the rear position
        self._queue[rear_pos] = value
        
        # Increment the count
        self._count += 1

    def peek(self):
        """
        Returns the item at the front of the queue without removing it.

        Returns:
            The item at the front of the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot peek at an empty queue.")

        # Get the front position from the subclass
        front_pos = self._get_front_position()
        
        # Return the front element
        return self._queue[front_pos]

    @abstractmethod
    def _get_front_position(self):
        """
        Returns the current front position in the queue.
        
        Returns:
            int: The index of the front element.
        """
        pass

    @abstractmethod
    def _get_rear_position(self):
        """
        Returns the current rear position in the queue.
        
        Returns:
            int: The index where the next element should be added.
        """
        pass

    @abstractmethod
    def dequeue(self):
        """
        Removes and returns the item from the front of the queue.

        Returns:
            The item at the front of the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        pass

    def __len__(self):
        """Allows using the built-in len() function on the queue."""
        return self._count

    @abstractmethod
    def __str__(self):
        """Provides a user-friendly string representation of the queue."""
        pass


class ShufflingQueue(DSAQueue):
    """
    A Queue implementation using a shuffling array.

    This implementation uses a fixed-size NumPy array. When an item is
    dequeued from the front, all subsequent items are shifted one position
    to the left. This approach is simple but inefficient for large queues.
    """

    def _get_front_position(self):
        """Returns the front position (always index 0 for shuffling queue)."""
        return 0

    def _get_rear_position(self):
        """Returns the rear position (current count for shuffling queue)."""
        return self._count

    def dequeue(self):
        """
        Removes and returns the item from the front of the queue.

        This method shifts all remaining elements to the left.

        Returns:
            The item at the front of the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Queue Underflow: Cannot dequeue from an empty queue.")

        # The front item is always at index 0.
        front_item = self._queue[0]

        # Shuffle all elements from index 1 to the end, one position to the left.
        for i in range(self._count - 1):
            self._queue[i] = self._queue[i + 1]

        # Decrement the count to "remove" the last element.
        self._count -= 1

        return front_item

    def __str__(self):
        """Provides a user-friendly string representation of the queue."""
        if self.is_empty():
            return "[]"

        # Displays the queue from front to rear.
        items = []
        for i in range(self._count):
            item = self._queue[i]
            if isinstance(item, (int, float)):
                # Convert to string without decimal if it's a whole number
                if item == int(item):
                    items.append(str(int(item)))
                else:
                    items.append(str(item))
            else:
                items.append(str(item))
        return f"[{' '.join(items)}]"


class CircularQueue(DSAQueue):
    """
    A Queue implementation using a circular array.

    This implementation uses a fixed-size NumPy array with front and rear pointers
    that wrap around the array. This approach is more efficient than shuffling
    for large queues as enqueue and dequeue operations are O(1).
    """

    def __init__(self, capacity=None):
        """
        Initializes the circular queue.

        Args:
            capacity (int, optional): The maximum number of elements the queue
                                      can hold. Defaults to 100.
        """
        super().__init__(capacity)
        
        # Front and rear pointers for the circular queue
        self._front = 0  # Index of the front element
        self._rear = -1  # Index of the rear element (starts at -1 for empty queue)

    def _get_front_position(self):
        """Returns the current front position."""
        return self._front

    def _get_rear_position(self):
        """Returns the next rear position (wraps around if needed)."""
        # Calculate the next rear position
        next_rear = (self._rear + 1) % self._capacity
        
        # Update the rear pointer
        self._rear = next_rear
        
        return next_rear

    def dequeue(self):
        """
        Removes and returns the item from the front of the queue.

        Returns:
            The item at the front of the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Queue Underflow: Cannot dequeue from an empty queue.")

        # Get the front item
        front_item = self._queue[self._front]
        
        # Move front pointer to next position (wrap around if needed)
        self._front = (self._front + 1) % self._capacity
        
        # Decrement the count
        self._count -= 1
        
        # If queue becomes empty, reset pointers
        if self.is_empty():
            self._front = 0
            self._rear = -1

        return front_item

    def __str__(self):
        """Provides a user-friendly string representation of the queue."""
        if self.is_empty():
            return "[]"

        # Build the string representation by traversing from front to rear
        items = []
        current = self._front
        
        for i in range(self._count):
            item = self._queue[current]
            if isinstance(item, (int, float)):
                # Convert to string without decimal if it's a whole number
                if item == int(item):
                    items.append(str(int(item)))
                else:
                    items.append(str(item))
            else:
                items.append(str(item))
            current = (current + 1) % self._capacity
            
        return f"[{' '.join(items)}]"

