import unittest
import numpy as np
from abc import ABC
from DSAQueue import DSAQueue, ShufflingQueue, CircularQueue


class BaseQueueTest(unittest.TestCase, ABC):
    """
    Base test class containing common tests for both queue implementations.
    This class should not be run directly - it's meant to be inherited from.
    """
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        # This will be overridden by subclasses
        self.queue_class = None
        self.default_queue = None
        self.small_queue = None
        self.large_queue = None

    def create_queue(self, capacity=None):
        """Helper method to create a queue of the appropriate type."""
        if self.queue_class is None:
            raise NotImplementedError("Subclasses must set queue_class")
        return self.queue_class(capacity)

    # ==================== INITIALIZATION TESTS ====================

    def test_default_initialization(self):
        """Test queue creation with default capacity."""
        queue = self.create_queue()
        self.assertEqual(queue.get_capacity(), 100)
        self.assertEqual(queue.get_count(), 0)
        self.assertTrue(queue.is_empty())
        self.assertFalse(queue.is_full())

    def test_custom_initialization(self):
        """Test queue creation with custom capacity."""
        queue = self.create_queue(capacity=50)
        self.assertEqual(queue.get_capacity(), 50)
        self.assertEqual(queue.get_count(), 0)
        self.assertTrue(queue.is_empty())
        self.assertFalse(queue.is_full())

    def test_initialization_with_none(self):
        """Test queue creation with None capacity (should use default)."""
        queue = self.create_queue(capacity=None)
        self.assertEqual(queue.get_capacity(), 100)
        self.assertEqual(queue.get_count(), 0)

    def test_invalid_initialization_zero_capacity(self):
        """Test that zero capacity raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.create_queue(capacity=0)
        self.assertIn("positive integer", str(context.exception))

    def test_invalid_initialization_negative_capacity(self):
        """Test that negative capacity raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.create_queue(capacity=-5)
        self.assertIn("positive integer", str(context.exception))

    def test_invalid_initialization_string_capacity(self):
        """Test that string capacity raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.create_queue(capacity="10")
        self.assertIn("positive integer", str(context.exception))

    def test_invalid_initialization_float_capacity(self):
        """Test that float capacity raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.create_queue(capacity=10.5)
        self.assertIn("positive integer", str(context.exception))

    # ==================== COUNT TESTS ====================

    def test_get_count_empty_queue(self):
        """Test get_count on empty queue."""
        self.assertEqual(self.default_queue.get_count(), 0)
        self.assertEqual(self.small_queue.get_count(), 0)
        self.assertEqual(self.large_queue.get_count(), 0)

    def test_get_count_after_operations(self):
        """Test get_count after various operations."""
        queue = self.create_queue(capacity=5)
        
        # After enqueue
        queue.enqueue(1)
        self.assertEqual(queue.get_count(), 1)
        
        queue.enqueue(2)
        self.assertEqual(queue.get_count(), 2)
        
        # After dequeue
        queue.dequeue()
        self.assertEqual(queue.get_count(), 1)
        
        queue.dequeue()
        self.assertEqual(queue.get_count(), 0)

    # ==================== EMPTY AND FULL TESTS ====================

    def test_is_empty_new_queue(self):
        """Test is_empty on newly created queue."""
        self.assertTrue(self.default_queue.is_empty())
        self.assertTrue(self.small_queue.is_empty())
        self.assertTrue(self.large_queue.is_empty())

    def test_is_empty_after_enqueue_dequeue(self):
        """Test is_empty after enqueue and dequeue operations."""
        queue = self.create_queue(capacity=2)
        
        # Initially empty
        self.assertTrue(queue.is_empty())
        
        # After enqueue
        queue.enqueue(1)
        self.assertFalse(queue.is_empty())
        
        # After dequeue
        queue.dequeue()
        self.assertTrue(queue.is_empty())

    def test_is_full_new_queue(self):
        """Test is_full on newly created queue."""
        self.assertFalse(self.default_queue.is_full())
        self.assertFalse(self.small_queue.is_full())
        self.assertFalse(self.large_queue.is_full())

    def test_is_full_at_capacity(self):
        """Test is_full when queue reaches capacity."""
        queue = self.create_queue(capacity=3)
        
        # Not full initially
        self.assertFalse(queue.is_full())
        
        # Fill the queue
        queue.enqueue(1)
        self.assertFalse(queue.is_full())
        
        queue.enqueue(2)
        self.assertFalse(queue.is_full())
        
        queue.enqueue(3)
        self.assertTrue(queue.is_full())

    def test_is_full_after_dequeue(self):
        """Test is_full after dequeuing from full queue."""
        queue = self.create_queue(capacity=2)
        
        # Fill the queue
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertTrue(queue.is_full())
        
        # Dequeue one item
        queue.dequeue()
        self.assertFalse(queue.is_full())

    # ==================== ENQUEUE TESTS ====================

    def test_enqueue_single_item(self):
        """Test enqueuing a single item."""
        queue = self.create_queue(capacity=5)
        queue.enqueue(42)
        
        self.assertEqual(queue.get_count(), 1)
        self.assertFalse(queue.is_empty())
        self.assertEqual(queue.peek(), 42)

    def test_enqueue_multiple_items(self):
        """Test enqueuing multiple items."""
        queue = self.create_queue(capacity=5)
        
        items = [1, "hello", 3.14, True, None]
        for i, item in enumerate(items):
            queue.enqueue(item)
            self.assertEqual(queue.get_count(), i + 1)
            # Front should always be the first item enqueued
            self.assertEqual(queue.peek(), items[0])

    def test_enqueue_different_data_types(self):
        """Test enqueuing different data types."""
        queue = self.create_queue(capacity=10)
        
        # Test various data types
        test_items = [
            42,                    # int
            "hello world",         # str
            3.14159,              # float
            True,                 # bool
            None,                 # None
            [1, 2, 3],           # list
            {"key": "value"},     # dict
            (1, 2, 3),           # tuple
            set([1, 2, 3]),      # set
            lambda x: x + 1       # function
        ]
        
        for item in test_items:
            queue.enqueue(item)
            # Front should always be the first item enqueued
            self.assertEqual(queue.peek(), test_items[0])

    def test_enqueue_overflow(self):
        """Test enqueuing to a full queue raises ValueError."""
        queue = self.create_queue(capacity=2)
        
        # Fill the queue
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertTrue(queue.is_full())
        
        # Try to enqueue to full queue
        with self.assertRaises(ValueError) as context:
            queue.enqueue(3)
        self.assertIn("Queue Overflow", str(context.exception))

    def test_enqueue_overflow_large_queue(self):
        """Test overflow on large queue."""
        queue = self.create_queue(capacity=1000)
        
        # Fill the queue
        for i in range(1000):
            queue.enqueue(i)
        
        self.assertTrue(queue.is_full())
        
        # Try to enqueue to full queue
        with self.assertRaises(ValueError) as context:
            queue.enqueue(1001)
        self.assertIn("Queue Overflow", str(context.exception))

    # ==================== DEQUEUE TESTS ====================

    def test_dequeue_single_item(self):
        """Test dequeuing a single item."""
        queue = self.create_queue(capacity=5)
        queue.enqueue(42)
        
        dequeued = queue.dequeue()
        self.assertEqual(dequeued, 42)
        self.assertEqual(queue.get_count(), 0)
        self.assertTrue(queue.is_empty())

    def test_dequeue_multiple_items(self):
        """Test dequeuing multiple items in FIFO order."""
        queue = self.create_queue(capacity=5)
        
        # Enqueue items
        items = [1, 2, 3, 4, 5]
        for item in items:
            queue.enqueue(item)
        
        # Dequeue items (should be in same order as enqueued)
        for i, item in enumerate(items):
            dequeued = queue.dequeue()
            self.assertEqual(dequeued, item)
            self.assertEqual(queue.get_count(), len(items) - i - 1)

    def test_dequeue_underflow(self):
        """Test dequeuing from empty queue raises IndexError."""
        queue = self.create_queue(capacity=5)
        
        self.assertTrue(queue.is_empty())
        
        with self.assertRaises(IndexError) as context:
            queue.dequeue()
        self.assertIn("Queue Underflow", str(context.exception))

    def test_dequeue_underflow_after_operations(self):
        """Test dequeuing from empty queue after enqueue/dequeue operations."""
        queue = self.create_queue(capacity=2)
        
        # Enqueue and dequeue to empty
        queue.enqueue(1)
        queue.dequeue()
        
        # Try to dequeue from empty queue
        with self.assertRaises(IndexError) as context:
            queue.dequeue()
        self.assertIn("Queue Underflow", str(context.exception))

    # ==================== PEEK TESTS ====================

    def test_peek_single_item(self):
        """Test peek method with single item."""
        queue = self.create_queue(capacity=5)
        queue.enqueue(42)
        
        front_item = queue.peek()
        self.assertEqual(front_item, 42)
        # Ensure peek() doesn't remove the item
        self.assertEqual(queue.get_count(), 1)

    def test_peek_multiple_items(self):
        """Test peek method with multiple items."""
        queue = self.create_queue(capacity=5)
        
        # Enqueue items
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        
        # Peek should always return the front (first enqueued)
        self.assertEqual(queue.peek(), 1)
        
        # After dequeue, peek should return next item
        queue.dequeue()
        self.assertEqual(queue.peek(), 2)
        
        queue.dequeue()
        self.assertEqual(queue.peek(), 3)

    def test_peek_empty_queue(self):
        """Test peek method on empty queue raises IndexError."""
        queue = self.create_queue(capacity=5)
        
        self.assertTrue(queue.is_empty())
        
        with self.assertRaises(IndexError) as context:
            queue.peek()
        self.assertIn("Cannot peek at an empty queue", str(context.exception))

    def test_peek_empty_queue_after_operations(self):
        """Test peek method on empty queue after operations."""
        queue = self.create_queue(capacity=2)
        
        # Enqueue and dequeue to empty
        queue.enqueue(1)
        queue.dequeue()
        
        # Try to peek at empty queue
        with self.assertRaises(IndexError) as context:
            queue.peek()
        self.assertIn("Cannot peek at an empty queue", str(context.exception))

    # ==================== LENGTH TESTS ====================

    def test_len_empty_queue(self):
        """Test len() on empty queue."""
        self.assertEqual(len(self.default_queue), 0)
        self.assertEqual(len(self.small_queue), 0)
        self.assertEqual(len(self.large_queue), 0)

    def test_len_after_operations(self):
        """Test len() after various operations."""
        queue = self.create_queue(capacity=5)
        
        # Initially empty
        self.assertEqual(len(queue), 0)
        
        # After enqueue
        queue.enqueue(1)
        self.assertEqual(len(queue), 1)
        
        queue.enqueue(2)
        self.assertEqual(len(queue), 2)
        
        # After dequeue
        queue.dequeue()
        self.assertEqual(len(queue), 1)
        
        queue.dequeue()
        self.assertEqual(len(queue), 0)

    def test_len_equals_get_count(self):
        """Test that len() returns the same as get_count()."""
        queue = self.create_queue(capacity=5)
        
        self.assertEqual(len(queue), queue.get_count())
        
        queue.enqueue(1)
        self.assertEqual(len(queue), queue.get_count())
        
        queue.enqueue(2)
        self.assertEqual(len(queue), queue.get_count())
        
        queue.dequeue()
        self.assertEqual(len(queue), queue.get_count())

    # ==================== STRING REPRESENTATION TESTS ====================

    def test_str_empty_queue(self):
        """Test string representation of empty queue."""
        self.assertEqual(str(self.default_queue), "[]")
        self.assertEqual(str(self.small_queue), "[]")
        self.assertEqual(str(self.large_queue), "[]")

    def test_str_single_item(self):
        """Test string representation with single item."""
        queue = self.create_queue(capacity=5)
        queue.enqueue(42)
        
        self.assertEqual(str(queue), "[42]")

    def test_str_multiple_items(self):
        """Test string representation with multiple items."""
        queue = self.create_queue(capacity=5)
        
        # Enqueue items
        queue.enqueue(1)
        queue.enqueue("two")
        queue.enqueue(3.0)
        
        # Should show front to rear (FIFO order)
        expected = "[1, two, 3.0]"
        self.assertEqual(str(queue), expected)

    def test_str_different_data_types(self):
        """Test string representation with different data types."""
        queue = self.create_queue(capacity=5)
        
        queue.enqueue(42)
        queue.enqueue("hello")
        queue.enqueue([1, 2, 3])
        queue.enqueue({"key": "value"})
        
        expected = "[42, hello, [1, 2, 3], {'key': 'value'}]"
        self.assertEqual(str(queue), expected)

    def test_str_after_operations(self):
        """Test string representation after enqueue/dequeue operations."""
        queue = self.create_queue(capacity=5)
        
        # Initially empty
        self.assertEqual(str(queue), "[]")
        
        # After enqueue
        queue.enqueue(1)
        self.assertEqual(str(queue), "[1]")
        
        queue.enqueue(2)
        self.assertEqual(str(queue), "[1, 2]")
        
        # After dequeue
        queue.dequeue()
        self.assertEqual(str(queue), "[2]")
        
        queue.dequeue()
        self.assertEqual(str(queue), "[]")

    # ==================== FIFO BEHAVIOR TESTS ====================

    def test_fifo_behavior(self):
        """Test that queue follows First-In-First-Out behavior."""
        queue = self.create_queue(capacity=5)
        
        # Enqueue items
        queue.enqueue("first")
        queue.enqueue("second")
        queue.enqueue("third")
        
        # Dequeue should return items in order of enqueue
        self.assertEqual(queue.dequeue(), "first")
        self.assertEqual(queue.dequeue(), "second")
        self.assertEqual(queue.dequeue(), "third")

    def test_fifo_with_mixed_operations(self):
        """Test FIFO behavior with mixed enqueue/dequeue operations."""
        queue = self.create_queue(capacity=5)
        
        # Enqueue some items
        queue.enqueue("A")
        queue.enqueue("B")
        
        # Dequeue one
        self.assertEqual(queue.dequeue(), "A")
        
        # Enqueue more
        queue.enqueue("C")
        queue.enqueue("D")
        
        # Dequeue remaining
        self.assertEqual(queue.dequeue(), "B")
        self.assertEqual(queue.dequeue(), "C")
        self.assertEqual(queue.dequeue(), "D")

    def test_fifo_order_preservation(self):
        """Test that FIFO order is preserved through multiple operations."""
        queue = self.create_queue(capacity=10)
        
        # Enqueue items
        for i in range(5):
            queue.enqueue(f"item_{i}")
        
        # Verify order through peek and dequeue
        for i in range(5):
            self.assertEqual(queue.peek(), f"item_{i}")
            self.assertEqual(queue.dequeue(), f"item_{i}")

    # ==================== INTEGRATION TESTS ====================

    def test_complete_queue_operations(self):
        """Test a complete sequence of queue operations."""
        queue = self.create_queue(capacity=5)
        
        # Initial state
        self.assertTrue(queue.is_empty())
        self.assertFalse(queue.is_full())
        self.assertEqual(queue.get_count(), 0)
        self.assertEqual(len(queue), 0)
        self.assertEqual(str(queue), "[]")
        
        # Enqueue operations
        queue.enqueue("first")
        self.assertFalse(queue.is_empty())
        self.assertFalse(queue.is_full())
        self.assertEqual(queue.get_count(), 1)
        self.assertEqual(queue.peek(), "first")
        
        queue.enqueue("second")
        queue.enqueue("third")
        self.assertEqual(queue.get_count(), 3)
        self.assertEqual(queue.peek(), "first")
        self.assertEqual(str(queue), "[first, second, third]")
        
        # Dequeue operations
        self.assertEqual(queue.dequeue(), "first")
        self.assertEqual(queue.get_count(), 2)
        self.assertEqual(queue.peek(), "second")
        
        self.assertEqual(queue.dequeue(), "second")
        self.assertEqual(queue.dequeue(), "third")
        
        # Final state
        self.assertTrue(queue.is_empty())
        self.assertEqual(queue.get_count(), 0)
        self.assertEqual(str(queue), "[]")

    def test_queue_with_numpy_arrays(self):
        """Test queue operations with NumPy arrays."""
        queue = self.create_queue(capacity=3)
        
        # Enqueue NumPy arrays
        arr1 = np.array([1, 2, 3])
        arr2 = np.array([[1, 2], [3, 4]])
        arr3 = np.array([1.5, 2.5, 3.5])
        
        queue.enqueue(arr1)
        queue.enqueue(arr2)
        queue.enqueue(arr3)
        
        # Check operations
        self.assertTrue(queue.is_full())
        self.assertEqual(queue.get_count(), 3)
        
        # Dequeue and verify
        self.assertTrue(np.array_equal(queue.dequeue(), arr1))
        self.assertTrue(np.array_equal(queue.dequeue(), arr2))
        self.assertTrue(np.array_equal(queue.dequeue(), arr3))

    def test_queue_with_objects(self):
        """Test queue operations with custom objects."""
        class TestObject:
            def __init__(self, value):
                self.value = value
            
            def __str__(self):
                return f"TestObject({self.value})"
            
            def __eq__(self, other):
                return isinstance(other, TestObject) and self.value == other.value
        
        queue = self.create_queue(capacity=3)
        
        obj1 = TestObject(1)
        obj2 = TestObject("hello")
        obj3 = TestObject(3.14)
        
        queue.enqueue(obj1)
        queue.enqueue(obj2)
        queue.enqueue(obj3)
        
        # Check operations
        self.assertEqual(queue.get_count(), 3)
        self.assertEqual(queue.peek(), obj1)
        
        # Dequeue and verify
        self.assertEqual(queue.dequeue(), obj1)
        self.assertEqual(queue.dequeue(), obj2)
        self.assertEqual(queue.dequeue(), obj3)

    # ==================== EDGE CASE TESTS ====================

    def test_capacity_one_queue(self):
        """Test queue with capacity of 1."""
        queue = self.create_queue(capacity=1)
        
        # Initially empty
        self.assertTrue(queue.is_empty())
        self.assertFalse(queue.is_full())
        
        # Enqueue one item
        queue.enqueue(42)
        self.assertFalse(queue.is_empty())
        self.assertTrue(queue.is_full())
        self.assertEqual(queue.peek(), 42)
        
        # Try to enqueue another (should fail)
        with self.assertRaises(ValueError):
            queue.enqueue(43)
        
        # Dequeue the item
        self.assertEqual(queue.dequeue(), 42)
        self.assertTrue(queue.is_empty())
        self.assertFalse(queue.is_full())

    def test_large_capacity_queue(self):
        """Test queue with very large capacity."""
        queue = self.create_queue(capacity=10000)
        
        # Enqueue many items
        for i in range(10000):
            queue.enqueue(i)
        
        self.assertTrue(queue.is_full())
        self.assertEqual(queue.get_count(), 10000)
        
        # Dequeue all items
        for i in range(10000):
            self.assertEqual(queue.dequeue(), i)
        
        self.assertTrue(queue.is_empty())

    def test_queue_with_duplicate_items(self):
        """Test queue operations with duplicate items."""
        queue = self.create_queue(capacity=5)
        
        # Enqueue duplicate items
        queue.enqueue(1)
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(2)
        queue.enqueue(1)
        
        # Verify FIFO order
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 1)

    def test_queue_with_none_values(self):
        """Test queue operations with None values."""
        queue = self.create_queue(capacity=3)
        
        # Enqueue None values
        queue.enqueue(None)
        queue.enqueue(42)
        queue.enqueue(None)
        
        # Verify operations
        self.assertEqual(queue.get_count(), 3)
        self.assertIsNone(queue.peek())
        
        # Dequeue and verify
        self.assertIsNone(queue.dequeue())
        self.assertEqual(queue.dequeue(), 42)
        self.assertIsNone(queue.dequeue())

    def test_repeated_enqueue_dequeue(self):
        """Test repeated enqueue/dequeue operations."""
        queue = self.create_queue(capacity=3)
        
        # First cycle
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)
        
        # Second cycle
        queue.enqueue(4)
        queue.enqueue(5)
        queue.enqueue(6)
        
        self.assertEqual(queue.dequeue(), 4)
        self.assertEqual(queue.dequeue(), 5)
        self.assertEqual(queue.dequeue(), 6)
        
        # Verify queue is empty
        self.assertTrue(queue.is_empty())


class ShufflingQueueTest(BaseQueueTest):
    """Test suite specifically for ShufflingQueue implementation."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.queue_class = ShufflingQueue
        self.default_queue = ShufflingQueue()
        self.small_queue = ShufflingQueue(capacity=3)
        self.large_queue = ShufflingQueue(capacity=1000)

    def test_shuffling_behavior(self):
        """Test that dequeuing properly shuffles remaining elements."""
        queue = self.create_queue(capacity=5)
        
        # Enqueue items
        queue.enqueue("A")
        queue.enqueue("B")
        queue.enqueue("C")
        queue.enqueue("D")
        
        # Dequeue first item
        self.assertEqual(queue.dequeue(), "A")
        
        # Verify remaining items are shuffled left
        self.assertEqual(str(queue), "[B, C, D]")
        self.assertEqual(queue.peek(), "B")
        
        # Dequeue another
        self.assertEqual(queue.dequeue(), "B")
        self.assertEqual(str(queue), "[C, D]")
        self.assertEqual(queue.peek(), "C")


class CircularQueueTest(BaseQueueTest):
    """Test suite specifically for CircularQueue implementation."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.queue_class = CircularQueue
        self.default_queue = CircularQueue()
        self.small_queue = CircularQueue(capacity=3)
        self.large_queue = CircularQueue(capacity=1000)

    def test_circular_wrapping(self):
        """Test that the circular queue properly wraps around the array."""
        queue = self.create_queue(capacity=3)
        
        # Fill the queue
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        
        # Dequeue one item to make space
        self.assertEqual(queue.dequeue(), 1)
        
        # Enqueue another item (should wrap around)
        queue.enqueue(4)
        
        # Verify the queue state
        self.assertEqual(str(queue), "[2, 3, 4]")
        self.assertEqual(queue.get_count(), 3)
        self.assertTrue(queue.is_full())
        
        # Dequeue all items
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)
        self.assertEqual(queue.dequeue(), 4)
        
        self.assertTrue(queue.is_empty())

    def test_circular_wrapping_multiple_cycles(self):
        """Test multiple cycles of wrapping around the array."""
        queue = self.create_queue(capacity=3)
        
        # First cycle
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        
        # Dequeue all
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)
        
        # Second cycle
        queue.enqueue(4)
        queue.enqueue(5)
        queue.enqueue(6)
        
        # Dequeue all
        self.assertEqual(queue.dequeue(), 4)
        self.assertEqual(queue.dequeue(), 5)
        self.assertEqual(queue.dequeue(), 6)
        
        # Third cycle
        queue.enqueue(7)
        queue.enqueue(8)
        queue.enqueue(9)
        
        # Dequeue all
        self.assertEqual(queue.dequeue(), 7)
        self.assertEqual(queue.dequeue(), 8)
        self.assertEqual(queue.dequeue(), 9)

    def test_circular_partial_fill_and_empty(self):
        """Test circular queue with partial filling and emptying."""
        queue = self.create_queue(capacity=5)
        
        # Fill partially
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        
        # Dequeue some
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        
        # Add more
        queue.enqueue(4)
        queue.enqueue(5)
        queue.enqueue(6)
        
        # Verify state
        self.assertEqual(str(queue), "[3, 4, 5, 6]")
        self.assertEqual(queue.get_count(), 4)
        
        # Dequeue all
        self.assertEqual(queue.dequeue(), 3)
        self.assertEqual(queue.dequeue(), 4)
        self.assertEqual(queue.dequeue(), 5)
        self.assertEqual(queue.dequeue(), 6)

    def test_circular_pointer_reset_on_empty(self):
        """Test that pointers are reset when queue becomes empty."""
        queue = self.create_queue(capacity=3)
        
        # Fill and partially empty
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        
        # Dequeue all
        queue.dequeue()
        queue.dequeue()
        queue.dequeue()
        
        # Verify queue is empty and pointers are reset
        self.assertTrue(queue.is_empty())
        self.assertEqual(queue._front, 0)
        self.assertEqual(queue._rear, -1)
        
        # Add new items
        queue.enqueue(4)
        queue.enqueue(5)
        
        # Verify they're added correctly
        self.assertEqual(str(queue), "[4, 5]")
        self.assertEqual(queue.peek(), 4)

    def test_circular_edge_wrapping(self):
        """Test edge cases of circular wrapping."""
        queue = self.create_queue(capacity=2)
        
        # Fill queue
        queue.enqueue(1)
        queue.enqueue(2)
        
        # Dequeue one
        self.assertEqual(queue.dequeue(), 1)
        
        # Add one more (should wrap)
        queue.enqueue(3)
        
        # Verify
        self.assertEqual(str(queue), "[2, 3]")
        self.assertEqual(queue.peek(), 2)
        
        # Dequeue both
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)
        
        # Should be empty with reset pointers
        self.assertTrue(queue.is_empty())
        self.assertEqual(queue._front, 0)
        self.assertEqual(queue._rear, -1)


if __name__ == '__main__':
    # Run the tests
    unittest.main(verbosity=2) 