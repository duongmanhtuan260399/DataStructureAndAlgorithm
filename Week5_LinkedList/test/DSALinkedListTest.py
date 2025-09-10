"""
Unit tests for DSALinkedList implementation.
Tests all methods including edge cases for empty, one-item, and multi-item lists.
"""

import unittest
from DSALinkedList import DSALinkedList


class TestDSALinkedList(unittest.TestCase):
    """Test cases for DSALinkedList class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.linked_list = DSALinkedList()
    
    def test_empty_list_initialization(self):
        """Test that a new linked list is properly initialized as empty."""
        self.assertTrue(self.linked_list.isEmpty())
        self.assertEqual(self.linked_list.getCount(), 0)
    
    def test_insert_first_empty_list(self):
        """Test insertFirst() on an empty list (Case a)."""
        self.linked_list.insertFirst(10)
        
        self.assertFalse(self.linked_list.isEmpty())
        self.assertEqual(self.linked_list.getCount(), 1)
        self.assertEqual(self.linked_list.peekFirst(), 10)
        self.assertEqual(self.linked_list.peekLast(), 10)
    
    def test_insert_first_one_item_list(self):
        """Test insertFirst() on a one-item list (Case b)."""
        # First insert to create one-item list
        self.linked_list.insertFirst(20)
        
        # Insert at first position
        self.linked_list.insertFirst(10)
        
        self.assertEqual(self.linked_list.getCount(), 2)
        self.assertEqual(self.linked_list.peekFirst(), 10)
        self.assertEqual(self.linked_list.peekLast(), 20)
    
    def test_insert_first_multi_item_list(self):
        """Test insertFirst() on a multi-item list (Case c)."""
        # Create multi-item list
        self.linked_list.insertFirst(30)
        self.linked_list.insertFirst(20)
        
        # Insert at first position
        self.linked_list.insertFirst(10)
        
        self.assertEqual(self.linked_list.getCount(), 3)
        self.assertEqual(self.linked_list.peekFirst(), 10)
        self.assertEqual(self.linked_list.peekLast(), 30)
    
    def test_insert_last_empty_list(self):
        """Test insertLast() on an empty list."""
        self.linked_list.insertLast(10)
        
        self.assertFalse(self.linked_list.isEmpty())
        self.assertEqual(self.linked_list.getCount(), 1)
        self.assertEqual(self.linked_list.peekFirst(), 10)
        self.assertEqual(self.linked_list.peekLast(), 10)
    
    def test_insert_last_non_empty_list(self):
        """Test insertLast() on a non-empty list."""
        self.linked_list.insertFirst(10)
        self.linked_list.insertLast(20)
        
        self.assertEqual(self.linked_list.getCount(), 2)
        self.assertEqual(self.linked_list.peekFirst(), 10)
        self.assertEqual(self.linked_list.peekLast(), 20)
    
    def test_remove_first_empty_list(self):
        """Test removeFirst() on an empty list (Case a) - should raise exception."""
        with self.assertRaises(ValueError):
            self.linked_list.removeFirst()
    
    def test_remove_first_one_item_list(self):
        """Test removeFirst() on a one-item list (Case b) - special case."""
        self.linked_list.insertFirst(10)
        
        value = self.linked_list.removeFirst()
        
        self.assertEqual(value, 10)
        self.assertTrue(self.linked_list.isEmpty())
        self.assertEqual(self.linked_list.getCount(), 0)
    
    def test_remove_first_multi_item_list(self):
        """Test removeFirst() on a multi-item list (Case c)."""
        self.linked_list.insertFirst(30)
        self.linked_list.insertFirst(20)
        self.linked_list.insertFirst(10)
        
        value = self.linked_list.removeFirst()
        
        self.assertEqual(value, 10)
        self.assertEqual(self.linked_list.getCount(), 2)
        self.assertEqual(self.linked_list.peekFirst(), 20)
        self.assertEqual(self.linked_list.peekLast(), 30)
    
    def test_remove_last_empty_list(self):
        """Test removeLast() on an empty list - should raise exception."""
        with self.assertRaises(ValueError):
            self.linked_list.removeLast()
    
    def test_remove_last_one_item_list(self):
        """Test removeLast() on a one-item list."""
        self.linked_list.insertFirst(10)
        
        value = self.linked_list.removeLast()
        
        self.assertEqual(value, 10)
        self.assertTrue(self.linked_list.isEmpty())
        self.assertEqual(self.linked_list.getCount(), 0)
    
    def test_remove_last_multi_item_list(self):
        """Test removeLast() on a multi-item list."""
        self.linked_list.insertFirst(30)
        self.linked_list.insertFirst(20)
        self.linked_list.insertFirst(10)
        
        value = self.linked_list.removeLast()
        
        self.assertEqual(value, 30)
        self.assertEqual(self.linked_list.getCount(), 2)
        self.assertEqual(self.linked_list.peekFirst(), 10)
        self.assertEqual(self.linked_list.peekLast(), 20)
    
    def test_peek_first_empty_list(self):
        """Test peekFirst() on an empty list - should raise exception."""
        with self.assertRaises(ValueError):
            self.linked_list.peekFirst()
    
    def test_peek_first_non_empty_list(self):
        """Test peekFirst() on a non-empty list."""
        self.linked_list.insertFirst(20)
        self.linked_list.insertFirst(10)
        
        value = self.linked_list.peekFirst()
        
        self.assertEqual(value, 10)
        # Ensure the list is not modified
        self.assertEqual(self.linked_list.getCount(), 2)
    
    def test_peek_last_empty_list(self):
        """Test peekLast() on an empty list - should raise exception."""
        with self.assertRaises(ValueError):
            self.linked_list.peekLast()
    
    def test_peek_last_non_empty_list(self):
        """Test peekLast() on a non-empty list."""
        self.linked_list.insertFirst(20)
        self.linked_list.insertFirst(10)
        
        value = self.linked_list.peekLast()
        
        self.assertEqual(value, 20)
        # Ensure the list is not modified
        self.assertEqual(self.linked_list.getCount(), 2)
    
    def test_get_count(self):
        """Test getCount() method with various operations."""
        # Initially empty
        self.assertEqual(self.linked_list.getCount(), 0)
        
        # Add elements
        self.linked_list.insertFirst(10)
        self.assertEqual(self.linked_list.getCount(), 1)
        
        self.linked_list.insertLast(20)
        self.assertEqual(self.linked_list.getCount(), 2)
        
        # Remove elements
        self.linked_list.removeFirst()
        self.assertEqual(self.linked_list.getCount(), 1)
        
        self.linked_list.removeLast()
        self.assertEqual(self.linked_list.getCount(), 0)
    
    def test_is_empty(self):
        """Test isEmpty() method with various operations."""
        # Initially empty
        self.assertTrue(self.linked_list.isEmpty())
        
        # Add element
        self.linked_list.insertFirst(10)
        self.assertFalse(self.linked_list.isEmpty())
        
        # Remove element
        self.linked_list.removeFirst()
        self.assertTrue(self.linked_list.isEmpty())
    
    def test_mixed_operations(self):
        """Test a sequence of mixed operations to ensure list integrity."""
        # Insert at first and last
        self.linked_list.insertFirst(10)
        self.linked_list.insertLast(30)
        self.linked_list.insertFirst(5)
        
        # Check state
        self.assertEqual(self.linked_list.getCount(), 3)
        self.assertEqual(self.linked_list.peekFirst(), 5)
        self.assertEqual(self.linked_list.peekLast(), 30)
        
        # Remove from first and last
        first_value = self.linked_list.removeFirst()
        last_value = self.linked_list.removeLast()
        
        self.assertEqual(first_value, 5)
        self.assertEqual(last_value, 30)
        self.assertEqual(self.linked_list.getCount(), 1)
        self.assertEqual(self.linked_list.peekFirst(), 10)
        self.assertEqual(self.linked_list.peekLast(), 10)
    
    def test_display_methods(self):
        """Test display() and displayReverse() methods."""
        # Test with empty list
        self.linked_list.display()  # Should print "List is empty"
        self.linked_list.displayReverse()  # Should print "List is empty"
        
        # Test with non-empty list
        self.linked_list.insertFirst(30)
        self.linked_list.insertFirst(20)
        self.linked_list.insertFirst(10)
        
        # These methods print to stdout, so we just ensure they don't raise exceptions
        self.linked_list.display()  # Should print "10 -> 20 -> 30"
        self.linked_list.displayReverse()  # Should print "30 -> 20 -> 10"
    
    def test_large_list_operations(self):
        """Test operations on a larger list to ensure scalability."""
        # Insert 100 elements
        for i in range(100):
            self.linked_list.insertLast(i)
        
        self.assertEqual(self.linked_list.getCount(), 100)
        self.assertEqual(self.linked_list.peekFirst(), 0)
        self.assertEqual(self.linked_list.peekLast(), 99)
        
        # Remove first 50 elements
        for i in range(50):
            value = self.linked_list.removeFirst()
            self.assertEqual(value, i)
        
        self.assertEqual(self.linked_list.getCount(), 50)
        self.assertEqual(self.linked_list.peekFirst(), 50)
        self.assertEqual(self.linked_list.peekLast(), 99)
        
        # Remove last 25 elements
        for i in range(25):
            value = self.linked_list.removeLast()
            self.assertEqual(value, 99 - i)
        
        self.assertEqual(self.linked_list.getCount(), 25)
        self.assertEqual(self.linked_list.peekFirst(), 50)
        self.assertEqual(self.linked_list.peekLast(), 74)
    
    def test_insert_before_empty_list(self):
        """Test insertBefore() on an empty list - should raise exception."""
        with self.assertRaises(ValueError):
            self.linked_list.insertBefore(10, 5)
    
    def test_insert_before_value_not_found(self):
        """Test insertBefore() when valueToFind is not in the list."""
        self.linked_list.insertFirst(10)
        self.linked_list.insertFirst(20)
        
        with self.assertRaises(ValueError):
            self.linked_list.insertBefore(30, 5)
    
    def test_insert_before_first_node(self):
        """Test insertBefore() when inserting before the first node."""
        self.linked_list.insertFirst(20)
        self.linked_list.insertFirst(10)
        
        self.linked_list.insertBefore(10, 5)
        
        self.assertEqual(self.linked_list.getCount(), 3)
        self.assertEqual(self.linked_list.peekFirst(), 5)
        self.assertEqual(self.linked_list.peekLast(), 20)
    
    def test_insert_before_middle_node(self):
        """Test insertBefore() when inserting before a middle node."""
        self.linked_list.insertFirst(30)
        self.linked_list.insertFirst(20)
        self.linked_list.insertFirst(10)
        
        self.linked_list.insertBefore(20, 15)
        
        self.assertEqual(self.linked_list.getCount(), 4)
        self.assertEqual(self.linked_list.peekFirst(), 10)
        self.assertEqual(self.linked_list.peekLast(), 30)
        # Verify the order: 10 -> 15 -> 20 -> 30
        values = []
        current = self.linked_list._head
        while current:
            values.append(current.value)
            current = current.next
        self.assertEqual(values, [10, 15, 20, 30])
    
    def test_insert_before_last_node(self):
        """Test insertBefore() when inserting before the last node."""
        self.linked_list.insertFirst(30)
        self.linked_list.insertFirst(20)
        self.linked_list.insertFirst(10)
        
        self.linked_list.insertBefore(30, 25)
        
        self.assertEqual(self.linked_list.getCount(), 4)
        self.assertEqual(self.linked_list.peekFirst(), 10)
        self.assertEqual(self.linked_list.peekLast(), 30)
        # Verify the order: 10 -> 20 -> 25 -> 30
        values = []
        current = self.linked_list._head
        while current:
            values.append(current.value)
            current = current.next
        self.assertEqual(values, [10, 20, 25, 30])
    
    def test_remove_value_empty_list(self):
        """Test remove() on an empty list - should raise exception."""
        with self.assertRaises(ValueError):
            self.linked_list.remove(10)
    
    def test_remove_value_not_found(self):
        """Test remove() when valueToFind is not in the list."""
        self.linked_list.insertFirst(10)
        self.linked_list.insertFirst(20)
        
        with self.assertRaises(ValueError):
            self.linked_list.remove(30)
    
    def test_remove_value_first_node(self):
        """Test remove() when removing the first node."""
        self.linked_list.insertFirst(30)
        self.linked_list.insertFirst(20)
        self.linked_list.insertFirst(10)
        
        value = self.linked_list.remove(10)
        
        self.assertEqual(value, 10)
        self.assertEqual(self.linked_list.getCount(), 2)
        self.assertEqual(self.linked_list.peekFirst(), 20)
        self.assertEqual(self.linked_list.peekLast(), 30)
    
    def test_remove_value_middle_node(self):
        """Test remove() when removing a middle node."""
        self.linked_list.insertFirst(30)
        self.linked_list.insertFirst(20)
        self.linked_list.insertFirst(10)
        
        value = self.linked_list.remove(20)
        
        self.assertEqual(value, 20)
        self.assertEqual(self.linked_list.getCount(), 2)
        self.assertEqual(self.linked_list.peekFirst(), 10)
        self.assertEqual(self.linked_list.peekLast(), 30)
    
    def test_remove_value_last_node(self):
        """Test remove() when removing the last node."""
        self.linked_list.insertFirst(30)
        self.linked_list.insertFirst(20)
        self.linked_list.insertFirst(10)
        
        value = self.linked_list.remove(30)
        
        self.assertEqual(value, 30)
        self.assertEqual(self.linked_list.getCount(), 2)
        self.assertEqual(self.linked_list.peekFirst(), 10)
        self.assertEqual(self.linked_list.peekLast(), 20)
    
    def test_remove_value_single_node(self):
        """Test remove() when removing from a single-node list."""
        self.linked_list.insertFirst(10)
        
        value = self.linked_list.remove(10)
        
        self.assertEqual(value, 10)
        self.assertTrue(self.linked_list.isEmpty())
        self.assertEqual(self.linked_list.getCount(), 0)
    
    def test_peek_value_empty_list(self):
        """Test peek() on an empty list - should raise exception."""
        with self.assertRaises(ValueError):
            self.linked_list.peek(10)
    
    def test_peek_value_not_found(self):
        """Test peek() when valueToFind is not in the list."""
        self.linked_list.insertFirst(10)
        self.linked_list.insertFirst(20)
        
        with self.assertRaises(ValueError):
            self.linked_list.peek(30)
    
    def test_peek_value_found(self):
        """Test peek() when valueToFind is found."""
        self.linked_list.insertFirst(30)
        self.linked_list.insertFirst(20)
        self.linked_list.insertFirst(10)
        
        value = self.linked_list.peek(20)
        
        self.assertEqual(value, 20)
        # Ensure the list is not modified
        self.assertEqual(self.linked_list.getCount(), 3)
        self.assertEqual(self.linked_list.peekFirst(), 10)
        self.assertEqual(self.linked_list.peekLast(), 30)
    
    def test_find_empty_list(self):
        """Test find() on an empty list."""
        result = self.linked_list.find(10)
        self.assertFalse(result)
    
    def test_find_value_not_found(self):
        """Test find() when valueToFind is not in the list."""
        self.linked_list.insertFirst(10)
        self.linked_list.insertFirst(20)
        
        result = self.linked_list.find(30)
        self.assertFalse(result)
    
    def test_find_value_found(self):
        """Test find() when valueToFind is found."""
        self.linked_list.insertFirst(30)
        self.linked_list.insertFirst(20)
        self.linked_list.insertFirst(10)
        
        result = self.linked_list.find(20)
        self.assertTrue(result)
        
        # Test finding first and last values
        self.assertTrue(self.linked_list.find(10))
        self.assertTrue(self.linked_list.find(30))
    
    def test_complex_operations_with_new_methods(self):
        """Test complex sequences using all methods together."""
        # Start with some values
        self.linked_list.insertFirst(50)
        self.linked_list.insertFirst(30)
        self.linked_list.insertFirst(10)
        
        # Insert before middle value
        self.linked_list.insertBefore(30, 20)
        
        # Insert before last value
        self.linked_list.insertBefore(50, 40)
        
        # Check state: 10 -> 20 -> 30 -> 40 -> 50
        self.assertEqual(self.linked_list.getCount(), 5)
        self.assertEqual(self.linked_list.peekFirst(), 10)
        self.assertEqual(self.linked_list.peekLast(), 50)
        
        # Test find operations
        self.assertTrue(self.linked_list.find(20))
        self.assertTrue(self.linked_list.find(40))
        self.assertFalse(self.linked_list.find(60))
        
        # Test peek operations
        self.assertEqual(self.linked_list.peek(20), 20)
        self.assertEqual(self.linked_list.peek(40), 40)
        
        # Remove middle value
        removed_value = self.linked_list.remove(30)
        self.assertEqual(removed_value, 30)
        self.assertEqual(self.linked_list.getCount(), 4)
        
        # Verify final state: 10 -> 20 -> 40 -> 50
        values = []
        current = self.linked_list._head
        while current:
            values.append(current.value)
            current = current.next
        self.assertEqual(values, [10, 20, 40, 50])


def run_tests():
    """Run all unit tests."""
    unittest.main(verbosity=2)


if __name__ == "__main__":
    run_tests()
