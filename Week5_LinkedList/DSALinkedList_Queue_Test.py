"""
Test file for DSALinkedList_Queue implementation.
"""

from DSALinkedList_Queue import DSAQueue


def test_queue_operations():
    """Test all queue operations."""
    print("=== Testing DSALinkedList Queue Implementation ===")
    
    # Create empty queue
    queue = DSAQueue()
    print(f"1. Empty queue: {queue.is_empty()}")
    print(f"   Count: {queue.get_count()}")
    print(f"   String representation: {queue}")
    
    # Test enqueue operations
    print("\n2. Testing enqueue operations:")
    queue.enqueue("First")
    print(f"   After enqueuing 'First': {queue}")
    print(f"   Front element: {queue.peek()}")
    
    queue.enqueue("Second")
    print(f"   After enqueuing 'Second': {queue}")
    print(f"   Front element: {queue.peek()}")
    
    queue.enqueue("Third")
    print(f"   After enqueuing 'Third': {queue}")
    print(f"   Front element: {queue.peek()}")
    print(f"   Count: {queue.get_count()}")
    
    # Test dequeue operations
    print("\n3. Testing dequeue operations:")
    dequeued = queue.dequeue()
    print(f"   Dequeued: {dequeued}")
    print(f"   Queue after dequeue: {queue}")
    print(f"   Front element: {queue.peek()}")
    
    dequeued = queue.dequeue()
    print(f"   Dequeued: {dequeued}")
    print(f"   Queue after dequeue: {queue}")
    print(f"   Front element: {queue.peek()}")
    
    dequeued = queue.dequeue()
    print(f"   Dequeued: {dequeued}")
    print(f"   Queue after dequeue: {queue}")
    print(f"   Empty: {queue.is_empty()}")
    
    # Test error handling
    print("\n4. Testing error handling:")
    try:
        queue.dequeue()
    except IndexError as e:
        print(f"   Expected error on dequeue from empty queue: {e}")
    
    try:
        queue.peek()
    except IndexError as e:
        print(f"   Expected error on peek from empty queue: {e}")
    
    print("\n5. Testing FIFO behavior:")
    # Enqueue multiple elements
    for i in range(5):
        queue.enqueue(f"Item_{i}")
    print(f"   Queue after enqueuing 5 items: {queue}")
    
    # Dequeue all elements (should come out in same order)
    print("   Dequeuing all elements (FIFO order):")
    while not queue.is_empty():
        print(f"     Dequeued: {queue.dequeue()}")
    
    print(f"   Final empty queue: {queue}")


if __name__ == "__main__":
    test_queue_operations()
