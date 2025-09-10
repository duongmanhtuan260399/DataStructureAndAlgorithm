"""
Test file for DSALinkedList_Stack implementation.
"""

from DSALinkedList_Stack import DSAStack


def test_stack_operations():
    """Test all stack operations."""
    print("=== Testing DSALinkedList Stack Implementation ===")
    
    # Create empty stack
    stack = DSAStack()
    print(f"1. Empty stack: {stack.is_empty()}")
    print(f"   Count: {stack.get_count()}")
    print(f"   String representation: {stack}")
    
    # Test push operations
    print("\n2. Testing push operations:")
    stack.push("First")
    print(f"   After pushing 'First': {stack}")
    print(f"   Top element: {stack.top()}")
    
    stack.push("Second")
    print(f"   After pushing 'Second': {stack}")
    print(f"   Top element: {stack.top()}")
    
    stack.push("Third")
    print(f"   After pushing 'Third': {stack}")
    print(f"   Top element: {stack.top()}")
    print(f"   Count: {stack.get_count()}")
    
    # Test pop operations
    print("\n3. Testing pop operations:")
    popped = stack.pop()
    print(f"   Popped: {popped}")
    print(f"   Stack after pop: {stack}")
    print(f"   Top element: {stack.top()}")
    
    popped = stack.pop()
    print(f"   Popped: {popped}")
    print(f"   Stack after pop: {stack}")
    print(f"   Top element: {stack.top()}")
    
    popped = stack.pop()
    print(f"   Popped: {popped}")
    print(f"   Stack after pop: {stack}")
    print(f"   Empty: {stack.is_empty()}")
    
    # Test error handling
    print("\n4. Testing error handling:")
    try:
        stack.pop()
    except IndexError as e:
        print(f"   Expected error on pop from empty stack: {e}")
    
    try:
        stack.top()
    except IndexError as e:
        print(f"   Expected error on top from empty stack: {e}")
    
    print("\n5. Testing LIFO behavior:")
    # Push multiple elements
    for i in range(5):
        stack.push(f"Item_{i}")
    print(f"   Stack after pushing 5 items: {stack}")
    
    # Pop all elements (should come out in reverse order)
    print("   Popping all elements (LIFO order):")
    while not stack.is_empty():
        print(f"     Popped: {stack.pop()}")
    
    print(f"   Final empty stack: {stack}")


if __name__ == "__main__":
    test_stack_operations()
