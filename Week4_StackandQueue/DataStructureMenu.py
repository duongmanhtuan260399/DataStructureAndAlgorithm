from DSAStack import DSAStack
from DSAQueue import ShufflingQueue, CircularQueue


def display_stack_menu():
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Check if empty")
    print("5. Check if full")
    print("6. Get current count")
    print("7. Get capacity")
    print("8. Display stack")
    print("9. Back to main menu")
    print("0. Exit")


def display_queue_menu():
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Check if empty")
    print("5. Check if full")
    print("6. Get current count")
    print("7. Get capacity")
    print("8. Display queue")
    print("9. Back to main menu")
    print("0. Exit")


def handle_stack_operations(stack):
    while True:
        display_stack_menu()
        try:
            choice = input("\nEnter your choice (0-9): ").strip()
            
            if choice == '0':
                exit()
            elif choice == '1':
                value = input("Enter value to push: ").strip()
                try:
                    stack.push(value)
                    print(f"Successfully pushed '{value}' to stack")
                except ValueError as e:
                    print(f"Error: {e}")
                    
            elif choice == '2':
                try:
                    value = stack.pop()
                    print(f"Popped: {value}")
                except IndexError as e:
                    print(f"Error: {e}")
            elif choice == '3':
                try:
                    value = stack.top()
                    print(f"Top element: {value}")
                except IndexError as e:
                    print(f"Error: {e}")     
            elif choice == '4':
                print(f"Stack is empty: {stack.is_empty()}")
                
            elif choice == '5':
                print(f"Stack is full: {stack.is_full()}")
                
            elif choice == '6':
                print(f"Current count: {stack.get_count()}")
                
            elif choice == '7':
                print(f"Capacity: {stack.get_capacity()}")
                
            elif choice == '8':
                print(f"Stack contents: {stack}")
                
            elif choice == '9':
                break
            else:
                print("Invalid choice. Please enter a number between 0-9.")
        except KeyboardInterrupt:
            exit()
        except Exception as e:
            print(f"An error occurred: {e}")


def handle_queue_operations(queue):
    """Handle queue operations based on user input."""
    while True:
        display_queue_menu()
        try:
            choice = input("\nEnter your choice (0-9): ").strip()
            
            if choice == '0':
                exit()
            elif choice == '1':
                value = input("Enter value to enqueue: ").strip()
                
                try:
                    queue.enqueue(value)
                    print(f"Successfully enqueued '{value}' to queue")
                except ValueError as e:
                    print(f"Error: {e}")  
            elif choice == '2':
                try:
                    value = queue.dequeue()
                    print(f"Dequeued: {value}")
                except IndexError as e:
                    print(f"Error: {e}")
            elif choice == '3':
                try:
                    value = queue.peek()
                    print(f"Front element: {value}")
                except IndexError as e:
                    print(f"Error: {e}")
            elif choice == '4':
                print(f"Queue is empty: {queue.is_empty()}")
                
            elif choice == '5':
                print(f"Queue is full: {queue.is_full()}")
                
            elif choice == '6':
                print(f"Current count: {queue.get_count()}")
                
            elif choice == '7':
                print(f"Capacity: {queue.get_capacity()}")
                
            elif choice == '8':
                print(f"Queue contents: {queue}")
                
            elif choice == '9':
                break
            else:
                print("Invalid choice. Please enter a number between 0-9.")
                
        except KeyboardInterrupt:
            exit()
        except Exception as e:
            print(f"An error occurred: {e}")


def main():    
    while True:
        print("\nWhich data structure would you like to create?")
        print("1. Stack")
        print("2. Queue")
        print("0. Exit")
        
        try:
            choice = input("\nEnter your choice (0-2): ").strip()
            
            if choice == '0':
                break
            elif choice == '1':
                try:
                    capacity = int(input("Enter capacity (press Enter for default 100): ") or "100")
                    if capacity <= 0:
                        print("Capacity must be positive. Using default capacity of 100.")
                        capacity = 100
                    stack = DSAStack(capacity)
                    print(f"Stack created with capacity {capacity}")
                    handle_stack_operations(stack)
                    
                except ValueError:
                    print("Invalid capacity. Using default capacity of 100.")
                    stack = DSAStack()
                    handle_stack_operations(stack)
                    
            elif choice == '2':
                print("\nWhich type of queue would you like to create?")
                print("1. Shuffling Queue")
                print("2. Circular Queue")
                print("3. Back to main menu")
                
                try:
                    queue_choice = int(input("Enter your choice (1-3): ").strip())
                    
                    if queue_choice == 3:
                        continue
                    elif queue_choice in [1, 2]:
                        try:
                            capacity = int(input("Enter capacity (press Enter for default 100): ") or "100")
                            if capacity <= 0:
                                print("Capacity must be positive. Using default capacity of 100.")
                                capacity = 100
                            
                            if queue_choice == 1:
                                queue = ShufflingQueue(capacity)
                                print(f"Shuffling Queue created with capacity {capacity}")
                            else:
                                queue = CircularQueue(capacity)
                                print(f"Circular Queue created with capacity {capacity}")
                            
                            handle_queue_operations(queue)
                            
                        except ValueError:
                            print("Invalid capacity. Using default capacity of 100.")
                            if queue_choice == 1:
                                queue = ShufflingQueue()
                                print("Shuffling Queue created with default capacity")
                            else:
                                queue = CircularQueue()
                                print("Circular Queue created with default capacity")
                            handle_queue_operations(queue)
                    else:
                        print("Invalid choice. Please enter 1, 2, or 3.")
                except ValueError:
                    print("Invalid choice. Please enter 1, 2, or 3.")
            else:
                print("Invalid choice. Please enter 0, 1, or 2.")
                
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
