from DSALinkedList_Stack import DSAStack
from DSALinkedList_Queue import DSAQueue


def display_stack_menu():
    """Display the stack operations menu."""
    print("1. Push")
    print("2. Pop")
    print("3. Peek (Top)")
    print("4. Check if empty")
    print("5. Get current count")
    print("6. Display stack")
    print("7. Back to main menu")
    print("0. Exit")


def display_queue_menu():
    """Display the queue operations menu."""
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Check if empty")
    print("5. Get current count")
    print("6. Display queue")
    print("7. Back to main menu")
    print("0. Exit")


def handle_stack_operations(stack):
    """Handle stack operations based on user input."""
    while True:
        display_stack_menu()
        try:
            choice = input("\nEnter your choice (0-7): ").strip()
            
            if choice == '0':
                exit()
            elif choice == '1':
                # Push
                value = input("Enter value to push: ").strip()
                if value:
                    try:
                        stack.push(value)
                        print(f"Successfully pushed '{value}' to stack")
                    except Exception as e:
                        print(f"Error: {e}")
                else:
                    print("Error: Value cannot be empty")
                    
            elif choice == '2':
                # Pop
                try:
                    value = stack.pop()
                    print(f"Popped: {value}")
                except IndexError as e:
                    print(f"Error: {e}")
                    
            elif choice == '3':
                # Peek (Top)
                try:
                    value = stack.top()
                    print(f"Top element: {value}")
                except IndexError as e:
                    print(f"Error: {e}")
                    
            elif choice == '4':
                # Check if empty
                print(f"Stack is empty: {stack.is_empty()}")
                
            elif choice == '5':
                # Get current count
                print(f"Current count: {stack.get_count()}")
                
            elif choice == '6':
                # Display stack
                print(f"Stack contents: {stack}")
                
            elif choice == '7':
                # Back to main menu
                break
            else:
                print("Invalid choice. Please enter a number between 0-7.")
                
        except KeyboardInterrupt:
            exit()
        except Exception as e:
            print(f"An error occurred: {e}")


def handle_queue_operations(queue):
    """Handle queue operations based on user input."""
    while True:
        display_queue_menu()
        try:
            choice = input("\nEnter your choice (0-7): ").strip()
            
            if choice == '0':
                exit()
            elif choice == '1':
                # Enqueue
                value = input("Enter value to enqueue: ").strip()
                if value:
                    try:
                        queue.enqueue(value)
                        print(f"Successfully enqueued '{value}' to queue")
                    except Exception as e:
                        print(f"Error: {e}")
                else:
                    print("Error: Value cannot be empty")
                    
            elif choice == '2':
                # Dequeue
                try:
                    value = queue.dequeue()
                    print(f"Dequeued: {value}")
                except IndexError as e:
                    print(f"Error: {e}")
                    
            elif choice == '3':
                # Peek
                try:
                    value = queue.peek()
                    print(f"Front element: {value}")
                except IndexError as e:
                    print(f"Error: {e}")
                    
            elif choice == '4':
                # Check if empty
                print(f"Queue is empty: {queue.is_empty()}")
                
            elif choice == '5':
                # Get current count
                print(f"Current count: {queue.get_count()}")
                
            elif choice == '6':
                # Display queue
                print(f"Queue contents: {queue}")
                
            elif choice == '7':
                # Back to main menu
                break
            else:
                print("Invalid choice. Please enter a number between 0-7.")
                
        except KeyboardInterrupt:
            exit()
        except Exception as e:
            print(f"An error occurred: {e}")


def main():
    """Main function to run the linked list data structure menu system."""
    print("Welcome to the Linked List Data Structure Menu!")
    
    while True:
        print("\n" + "-"*50)
        print("LINKED LIST DATA STRUCTURE MENU")
        print("-"*50)
        print("Which data structure would you like to create?")
        print("1. Stack (using DSALinkedList)")
        print("2. Queue (using DSALinkedList)")
        print("0. Exit")
        
        try:
            choice = input("\nEnter your choice (0-2): ").strip()
            
            if choice == '0':
                print("Thank you for using the Linked List Data Structure Menu!")
                break
            elif choice == '1':
                # Create Stack
                stack = DSAStack()
                print("Stack created successfully using DSALinkedList!")
                print("Note: This stack has dynamic sizing (no capacity limit)")
                handle_stack_operations(stack)
                
            elif choice == '2':
                # Create Queue
                queue = DSAQueue()
                print("Queue created successfully using DSALinkedList!")
                print("Note: This queue has dynamic sizing (no capacity limit)")
                handle_queue_operations(queue)
                
            else:
                print("Invalid choice. Please enter 0, 1, or 2.")
                
        except KeyboardInterrupt:
            print("\n\nThank you for using the Linked List Data Structure Menu!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
