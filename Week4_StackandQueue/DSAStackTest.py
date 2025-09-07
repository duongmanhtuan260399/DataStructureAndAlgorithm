import unittest
import numpy as np
from DSAStack import DSAStack


class DSAStackTest(unittest.TestCase):
    """
    Test suite for the DSAStack class.
    
    This test suite covers:
    - Initialization with various parameters
    - All public methods
    - Edge cases and error conditions
    - Stack operations (push, pop, top)
    - Stack state checking (empty, full, count)
    - String representation
    - Length functionality
    """

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.default_stack = DSAStack()
        self.small_stack = DSAStack(capacity=3)
        self.large_stack = DSAStack(capacity=1000)

    def tearDown(self):
        """Clean up after each test method."""
        pass

    # ==================== INITIALIZATION TESTS ====================

    def test_default_initialization(self):
        """Test stack creation with default capacity."""
        stack = DSAStack()
        self.assertEqual(stack.get_capacity(), 100)
        self.assertEqual(stack.get_count(), 0)
        self.assertTrue(stack.is_empty())
        self.assertFalse(stack.is_full())

    def test_custom_initialization(self):
        """Test stack creation with custom capacity."""
        stack = DSAStack(capacity=50)
        self.assertEqual(stack.get_capacity(), 50)
        self.assertEqual(stack.get_count(), 0)
        self.assertTrue(stack.is_empty())
        self.assertFalse(stack.is_full())

    def test_initialization_with_none(self):
        """Test stack creation with None capacity (should use default)."""
        stack = DSAStack(capacity=None)
        self.assertEqual(stack.get_capacity(), 100)
        self.assertEqual(stack.get_count(), 0)

    def test_invalid_initialization_zero_capacity(self):
        """Test that zero capacity raises ValueError."""
        with self.assertRaises(ValueError) as context:
            DSAStack(capacity=0)
        self.assertIn("positive integer", str(context.exception))

    def test_invalid_initialization_negative_capacity(self):
        """Test that negative capacity raises ValueError."""
        with self.assertRaises(ValueError) as context:
            DSAStack(capacity=-5)
        self.assertIn("positive integer", str(context.exception))

    def test_invalid_initialization_string_capacity(self):
        """Test that string capacity raises ValueError."""
        with self.assertRaises(ValueError) as context:
            DSAStack(capacity="10")
        self.assertIn("positive integer", str(context.exception))

    def test_invalid_initialization_float_capacity(self):
        """Test that float capacity raises ValueError."""
        with self.assertRaises(ValueError) as context:
            DSAStack(capacity=10.5)
        self.assertIn("positive integer", str(context.exception))

    # ==================== CAPACITY AND COUNT TESTS ====================

    def test_get_capacity(self):
        """Test get_capacity method."""
        self.assertEqual(self.default_stack.get_capacity(), 100)
        self.assertEqual(self.small_stack.get_capacity(), 3)
        self.assertEqual(self.large_stack.get_capacity(), 1000)

    def test_get_count_empty_stack(self):
        """Test get_count on empty stack."""
        self.assertEqual(self.default_stack.get_count(), 0)
        self.assertEqual(self.small_stack.get_count(), 0)
        self.assertEqual(self.large_stack.get_count(), 0)

    def test_get_count_after_operations(self):
        """Test get_count after various operations."""
        stack = DSAStack(capacity=5)
        
        # After push
        stack.push(1)
        self.assertEqual(stack.get_count(), 1)
        
        stack.push(2)
        self.assertEqual(stack.get_count(), 2)
        
        # After pop
        stack.pop()
        self.assertEqual(stack.get_count(), 1)
        
        stack.pop()
        self.assertEqual(stack.get_count(), 0)

    # ==================== EMPTY AND FULL TESTS ====================

    def test_is_empty_new_stack(self):
        """Test is_empty on newly created stack."""
        self.assertTrue(self.default_stack.is_empty())
        self.assertTrue(self.small_stack.is_empty())
        self.assertTrue(self.large_stack.is_empty())

    def test_is_empty_after_push_pop(self):
        """Test is_empty after push and pop operations."""
        stack = DSAStack(capacity=2)
        
        # Initially empty
        self.assertTrue(stack.is_empty())
        
        # After push
        stack.push(1)
        self.assertFalse(stack.is_empty())
        
        # After pop
        stack.pop()
        self.assertTrue(stack.is_empty())

    def test_is_full_new_stack(self):
        """Test is_full on newly created stack."""
        self.assertFalse(self.default_stack.is_full())
        self.assertFalse(self.small_stack.is_full())
        self.assertFalse(self.large_stack.is_full())

    def test_is_full_at_capacity(self):
        """Test is_full when stack reaches capacity."""
        stack = DSAStack(capacity=3)
        
        # Not full initially
        self.assertFalse(stack.is_full())
        
        # Fill the stack
        stack.push(1)
        self.assertFalse(stack.is_full())
        
        stack.push(2)
        self.assertFalse(stack.is_full())
        
        stack.push(3)
        self.assertTrue(stack.is_full())

    def test_is_full_after_pop(self):
        """Test is_full after popping from full stack."""
        stack = DSAStack(capacity=2)
        
        # Fill the stack
        stack.push(1)
        stack.push(2)
        self.assertTrue(stack.is_full())
        
        # Pop one item
        stack.pop()
        self.assertFalse(stack.is_full())

    # ==================== PUSH TESTS ====================

    def test_push_single_item(self):
        """Test pushing a single item."""
        stack = DSAStack(capacity=5)
        stack.push(42)
        
        self.assertEqual(stack.get_count(), 1)
        self.assertFalse(stack.is_empty())
        self.assertEqual(stack.top(), 42)

    def test_push_multiple_items(self):
        """Test pushing multiple items."""
        stack = DSAStack(capacity=5)
        
        items = [1, "hello", 3.14, True, None]
        for i, item in enumerate(items):
            stack.push(item)
            self.assertEqual(stack.get_count(), i + 1)
            self.assertEqual(stack.top(), item)

    def test_push_different_data_types(self):
        """Test pushing different data types."""
        stack = DSAStack(capacity=10)
        
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
            stack.push(item)
            self.assertEqual(stack.top(), item)

    def test_push_overflow(self):
        """Test pushing to a full stack raises ValueError."""
        stack = DSAStack(capacity=2)
        
        # Fill the stack
        stack.push(1)
        stack.push(2)
        self.assertTrue(stack.is_full())
        
        # Try to push to full stack
        with self.assertRaises(ValueError) as context:
            stack.push(3)
        self.assertIn("Stack Overflow", str(context.exception))

    def test_push_overflow_large_stack(self):
        """Test overflow on large stack."""
        stack = DSAStack(capacity=1000)
        
        # Fill the stack
        for i in range(1000):
            stack.push(i)
        
        self.assertTrue(stack.is_full())
        
        # Try to push to full stack
        with self.assertRaises(ValueError) as context:
            stack.push(1001)
        self.assertIn("Stack Overflow", str(context.exception))

    # ==================== POP TESTS ====================

    def test_pop_single_item(self):
        """Test popping a single item."""
        stack = DSAStack(capacity=5)
        stack.push(42)
        
        popped = stack.pop()
        self.assertEqual(popped, 42)
        self.assertEqual(stack.get_count(), 0)
        self.assertTrue(stack.is_empty())

    def test_pop_multiple_items(self):
        """Test popping multiple items in LIFO order."""
        stack = DSAStack(capacity=5)
        
        # Push items
        items = [1, 2, 3, 4, 5]
        for item in items:
            stack.push(item)
        
        # Pop items (should be in reverse order)
        for i in range(len(items) - 1, -1, -1):
            popped = stack.pop()
            self.assertEqual(popped, items[i])
            self.assertEqual(stack.get_count(), i)

    def test_pop_underflow(self):
        """Test popping from empty stack raises IndexError."""
        stack = DSAStack(capacity=5)
        
        self.assertTrue(stack.is_empty())
        
        with self.assertRaises(IndexError) as context:
            stack.pop()
        self.assertIn("Stack Underflow", str(context.exception))

    def test_pop_underflow_after_operations(self):
        """Test popping from empty stack after push/pop operations."""
        stack = DSAStack(capacity=2)
        
        # Push and pop to empty
        stack.push(1)
        stack.pop()
        
        # Try to pop from empty stack
        with self.assertRaises(IndexError) as context:
            stack.pop()
        self.assertIn("Stack Underflow", str(context.exception))

    # ==================== TOP TESTS ====================

    def test_top_single_item(self):
        """Test top method with single item."""
        stack = DSAStack(capacity=5)
        stack.push(42)
        
        top_item = stack.top()
        self.assertEqual(top_item, 42)
        # Ensure top() doesn't remove the item
        self.assertEqual(stack.get_count(), 1)

    def test_top_multiple_items(self):
        """Test top method with multiple items."""
        stack = DSAStack(capacity=5)
        
        items = [1, 2, 3]
        for item in items:
            stack.push(item)
            self.assertEqual(stack.top(), item)

    def test_top_after_pop(self):
        """Test top method after pop operations."""
        stack = DSAStack(capacity=5)
        
        # Push multiple items
        stack.push(1)
        stack.push(2)
        stack.push(3)
        
        # Check top after each pop
        self.assertEqual(stack.top(), 3)
        stack.pop()
        
        self.assertEqual(stack.top(), 2)
        stack.pop()
        
        self.assertEqual(stack.top(), 1)

    def test_top_empty_stack(self):
        """Test top method on empty stack raises IndexError."""
        stack = DSAStack(capacity=5)
        
        self.assertTrue(stack.is_empty())
        
        with self.assertRaises(IndexError) as context:
            stack.top()
        self.assertIn("Cannot get top from an empty stack", str(context.exception))

    def test_top_empty_stack_after_operations(self):
        """Test top method on empty stack after operations."""
        stack = DSAStack(capacity=2)
        
        # Push and pop to empty
        stack.push(1)
        stack.pop()
        
        # Try to get top from empty stack
        with self.assertRaises(IndexError) as context:
            stack.top()
        self.assertIn("Cannot get top from an empty stack", str(context.exception))

    # ==================== LENGTH TESTS ====================

    def test_len_empty_stack(self):
        """Test len() on empty stack."""
        self.assertEqual(len(self.default_stack), 0)
        self.assertEqual(len(self.small_stack), 0)
        self.assertEqual(len(self.large_stack), 0)

    def test_len_after_operations(self):
        """Test len() after various operations."""
        stack = DSAStack(capacity=5)
        
        # Initially empty
        self.assertEqual(len(stack), 0)
        
        # After push
        stack.push(1)
        self.assertEqual(len(stack), 1)
        
        stack.push(2)
        self.assertEqual(len(stack), 2)
        
        # After pop
        stack.pop()
        self.assertEqual(len(stack), 1)
        
        stack.pop()
        self.assertEqual(len(stack), 0)

    def test_len_equals_get_count(self):
        """Test that len() returns the same as get_count()."""
        stack = DSAStack(capacity=5)
        
        self.assertEqual(len(stack), stack.get_count())
        
        stack.push(1)
        self.assertEqual(len(stack), stack.get_count())
        
        stack.push(2)
        self.assertEqual(len(stack), stack.get_count())
        
        stack.pop()
        self.assertEqual(len(stack), stack.get_count())

    # ==================== STRING REPRESENTATION TESTS ====================

    def test_str_empty_stack(self):
        """Test string representation of empty stack."""
        self.assertEqual(str(self.default_stack), "[]")
        self.assertEqual(str(self.small_stack), "[]")
        self.assertEqual(str(self.large_stack), "[]")

    def test_str_single_item(self):
        """Test string representation with single item."""
        stack = DSAStack(capacity=5)
        stack.push(42)
        
        self.assertEqual(str(stack), "[42]")

    def test_str_multiple_items(self):
        """Test string representation with multiple items."""
        stack = DSAStack(capacity=5)
        
        # Push items
        stack.push(1)
        stack.push("two")
        stack.push(3.0)
        
        # Should show top to bottom (LIFO order)
        expected = "[3.0, two, 1]"
        self.assertEqual(str(stack), expected)

    def test_str_different_data_types(self):
        """Test string representation with different data types."""
        stack = DSAStack(capacity=5)
        
        stack.push(42)
        stack.push("hello")
        stack.push([1, 2, 3])
        stack.push({"key": "value"})
        
        expected = "[{'key': 'value'}, [1, 2, 3], hello, 42]"
        self.assertEqual(str(stack), expected)

    def test_str_after_operations(self):
        """Test string representation after push/pop operations."""
        stack = DSAStack(capacity=5)
        
        # Initially empty
        self.assertEqual(str(stack), "[]")
        
        # After push
        stack.push(1)
        self.assertEqual(str(stack), "[1]")
        
        stack.push(2)
        self.assertEqual(str(stack), "[2, 1]")
        
        # After pop
        stack.pop()
        self.assertEqual(str(stack), "[1]")
        
        stack.pop()
        self.assertEqual(str(stack), "[]")

    # ==================== INTEGRATION TESTS ====================

    def test_complete_stack_operations(self):
        """Test a complete sequence of stack operations."""
        stack = DSAStack(capacity=5)
        
        # Initial state
        self.assertTrue(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.get_count(), 0)
        self.assertEqual(len(stack), 0)
        self.assertEqual(str(stack), "[]")
        
        # Push operations
        stack.push("first")
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.get_count(), 1)
        self.assertEqual(stack.top(), "first")
        
        stack.push("second")
        stack.push("third")
        self.assertEqual(stack.get_count(), 3)
        self.assertEqual(stack.top(), "third")
        self.assertEqual(str(stack), "[third, second, first]")
        
        # Pop operations
        self.assertEqual(stack.pop(), "third")
        self.assertEqual(stack.get_count(), 2)
        self.assertEqual(stack.top(), "second")
        
        self.assertEqual(stack.pop(), "second")
        self.assertEqual(stack.pop(), "first")
        
        # Final state
        self.assertTrue(stack.is_empty())
        self.assertEqual(stack.get_count(), 0)
        self.assertEqual(str(stack), "[]")

    def test_stack_with_numpy_arrays(self):
        """Test stack operations with NumPy arrays."""
        stack = DSAStack(capacity=3)
        
        # Push NumPy arrays
        arr1 = np.array([1, 2, 3])
        arr2 = np.array([[1, 2], [3, 4]])
        arr3 = np.array([1.5, 2.5, 3.5])
        
        stack.push(arr1)
        stack.push(arr2)
        stack.push(arr3)
        
        # Check operations
        self.assertTrue(stack.is_full())
        self.assertEqual(stack.get_count(), 3)
        
        # Pop and verify
        self.assertTrue(np.array_equal(stack.pop(), arr3))
        self.assertTrue(np.array_equal(stack.pop(), arr2))
        self.assertTrue(np.array_equal(stack.pop(), arr1))

    def test_stack_with_objects(self):
        """Test stack operations with custom objects."""
        class TestObject:
            def __init__(self, value):
                self.value = value
            
            def __str__(self):
                return f"TestObject({self.value})"
            
            def __eq__(self, other):
                return isinstance(other, TestObject) and self.value == other.value
        
        stack = DSAStack(capacity=3)
        
        obj1 = TestObject(1)
        obj2 = TestObject("hello")
        obj3 = TestObject(3.14)
        
        stack.push(obj1)
        stack.push(obj2)
        stack.push(obj3)
        
        # Check operations
        self.assertEqual(stack.get_count(), 3)
        self.assertEqual(stack.top(), obj3)
        
        # Pop and verify
        self.assertEqual(stack.pop(), obj3)
        self.assertEqual(stack.pop(), obj2)
        self.assertEqual(stack.pop(), obj1)

    # ==================== EDGE CASE TESTS ====================

    def test_capacity_one_stack(self):
        """Test stack with capacity of 1."""
        stack = DSAStack(capacity=1)
        
        # Initially empty
        self.assertTrue(stack.is_empty())
        self.assertFalse(stack.is_full())
        
        # Push one item
        stack.push(42)
        self.assertFalse(stack.is_empty())
        self.assertTrue(stack.is_full())
        self.assertEqual(stack.top(), 42)
        
        # Try to push another (should fail)
        with self.assertRaises(ValueError):
            stack.push(43)
        
        # Pop the item
        self.assertEqual(stack.pop(), 42)
        self.assertTrue(stack.is_empty())
        self.assertFalse(stack.is_full())

    def test_large_capacity_stack(self):
        """Test stack with very large capacity."""
        stack = DSAStack(capacity=10000)
        
        # Push many items
        for i in range(10000):
            stack.push(i)
        
        self.assertTrue(stack.is_full())
        self.assertEqual(stack.get_count(), 10000)
        
        # Pop all items
        for i in range(9999, -1, -1):
            self.assertEqual(stack.pop(), i)
        
        self.assertTrue(stack.is_empty())

    def test_stack_with_duplicate_items(self):
        """Test stack operations with duplicate items."""
        stack = DSAStack(capacity=5)
        
        # Push duplicate items
        stack.push(1)
        stack.push(1)
        stack.push(2)
        stack.push(2)
        stack.push(1)
        
        # Verify LIFO order
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.pop(), 1)

    def test_stack_with_none_values(self):
        """Test stack operations with None values."""
        stack = DSAStack(capacity=3)
        
        # Push None values
        stack.push(None)
        stack.push(42)
        stack.push(None)
        
        # Verify operations
        self.assertEqual(stack.get_count(), 3)
        self.assertIsNone(stack.top())
        
        # Pop and verify
        self.assertIsNone(stack.pop())
        self.assertEqual(stack.pop(), 42)
        self.assertIsNone(stack.pop())


if __name__ == '__main__':
    # Run the tests
    unittest.main(verbosity=2) 