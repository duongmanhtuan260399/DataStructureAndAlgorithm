from DSALinkedList import DSALinkedList


def display_main_operations_menu():
    print("\n--- Linked List Operations ---")
    print("1. Insert")
    print("2. Remove")
    print("3. Peek")
    print("4. Find")
    print("6. Get Count")
    print("7. Display")
    print("8. Back to main menu")
    print("0. Exit")


def display_insert_menu():
    print("\n--- Insert Operations ---")
    print("1. Insert First")
    print("2. Insert Last")
    print("3. Insert Before")
    print("4. Back to operations menu")
    print("0. Exit")


def display_remove_menu():
    print("\n--- Remove Operations ---")
    print("1. Remove First")
    print("2. Remove Last")
    print("3. Remove Value")
    print("4. Back to operations menu")
    print("0. Exit")


def display_peek_menu():
    print("\n--- Peek Operations ---")
    print("1. Peek First")
    print("2. Peek Last")
    print("3. Peek Value")
    print("4. Back to operations menu")
    print("0. Exit")


def display_display_menu():
    print("\n--- Display Operations ---")
    print("1. Display Forward")
    print("2. Display Backward")
    print("3. Back to operations menu")
    print("0. Exit")


def handle_insert_operations(linked_list):
    display_insert_menu()
    try:
        choice = input("\nEnter your choice (0-4): ").strip()
        
        if choice == '0':
            exit()
        elif choice == '1':
            # Insert First
            value = input("Enter value to insert at the beginning: ").strip()
            if value:
                try:
                    linked_list.insertFirst(value)
                    print(f"Successfully inserted '{value}' at the beginning")
                except Exception as e:
                    print(f"Error: {e}")
            else:
                print("Error: Value cannot be empty")
                
        elif choice == '2':
            # Insert Last
            value = input("Enter value to insert at the end: ").strip()
            if value:
                try:
                    linked_list.insertLast(value)
                    print(f"Successfully inserted '{value}' at the end")
                except Exception as e:
                    print(f"Error: {e}")
            else:
                print("Error: Value cannot be empty")
                
        elif choice == '3':
            # Insert Before
            if linked_list.isEmpty():
                print("Error: Cannot insert before in an empty list")
            else:
                value_to_find = input("Enter the value to find: ").strip()
                if value_to_find:
                    # First check if the value exists in the list
                    if linked_list.find(value_to_find):
                        new_value = input("Enter the new value to insert before it: ").strip()
                        if new_value:
                            try:
                                linked_list.insertBefore(value_to_find, new_value)
                                print(f"Successfully inserted '{new_value}' before '{value_to_find}'")
                            except ValueError as e:
                                print(f"Error: {e}")
                        else:
                            print("Error: New value cannot be empty")
                    else:
                        print(f"Error: Value '{value_to_find}' not found in the list")
                else:
                    print("Error: Value to find cannot be empty")
                    
        elif choice == '4':
            # Back to operations menu - do nothing, will return to main menu
            pass
        else:
            print("Invalid choice. Please enter a number between 0-4.")
            
    except KeyboardInterrupt:
        exit()
    except Exception as e:
        print(f"An error occurred: {e}")


def handle_remove_operations(linked_list):
    display_remove_menu()
    try:
        choice = input("\nEnter your choice (0-4): ").strip()
        
        if choice == '0':
            exit()
        elif choice == '1':
            # Remove First
            try:
                value = linked_list.removeFirst()
                print(f"Removed first element: {value}")
            except ValueError as e:
                print(f"Error: {e}")
                
        elif choice == '2':
            # Remove Last
            try:
                value = linked_list.removeLast()
                print(f"Removed last element: {value}")
            except ValueError as e:
                print(f"Error: {e}")
                
        elif choice == '3':
            # Remove Value
            if linked_list.isEmpty():
                print("Error: Cannot remove from an empty list")
            else:
                value_to_remove = input("Enter the value to remove: ").strip()
                if value_to_remove:
                    try:
                        removed_value = linked_list.remove(value_to_remove)
                        print(f"Removed element: {removed_value}")
                    except ValueError as e:
                        print(f"Error: {e}")
                else:
                    print("Error: Value cannot be empty")
                    
        elif choice == '4':
            # Back to operations menu - do nothing, will return to main menu
            pass
        else:
            print("Invalid choice. Please enter a number between 0-4.")
            
    except KeyboardInterrupt:
        exit()
    except Exception as e:
        print(f"An error occurred: {e}")


def handle_peek_operations(linked_list):
    display_peek_menu()
    try:
        choice = input("\nEnter your choice (0-4): ").strip()
        
        if choice == '0':
            exit()
        elif choice == '1':
            # Peek First
            try:
                value = linked_list.peekFirst()
                print(f"First element: {value}")
            except ValueError as e:
                print(f"Error: {e}")
                
        elif choice == '2':
            # Peek Last
            try:
                value = linked_list.peekLast()
                print(f"Last element: {value}")
            except ValueError as e:
                print(f"Error: {e}")
                
        elif choice == '3':
            # Peek Value
            if linked_list.isEmpty():
                print("Error: Cannot peek in an empty list")
            else:
                value_to_peek = input("Enter the value to peek: ").strip()
                if value_to_peek:
                    try:
                        value = linked_list.peek(value_to_peek)
                        print(f"Found value: {value}")
                    except ValueError as e:
                        print(f"Error: {e}")
                else:
                    print("Error: Value cannot be empty")
                    
        elif choice == '4':
            # Back to operations menu - do nothing, will return to main menu
            pass
        else:
            print("Invalid choice. Please enter a number between 0-4.")
            
    except KeyboardInterrupt:
        exit()
    except Exception as e:
        print(f"An error occurred: {e}")


def handle_display_operations(linked_list):
    display_display_menu()
    try:
        choice = input("\nEnter your choice (0-3): ").strip()
        
        if choice == '0':
            exit()
        elif choice == '1':
            # Display Forward
            print("List contents (forward):")
            linked_list.display()
            
        elif choice == '2':
            # Display Backward
            print("List contents (backward):")
            linked_list.displayReverse()
            
        elif choice == '3':
            # Back to operations menu - do nothing, will return to main menu
            pass
        else:
            print("Invalid choice. Please enter a number between 0-3.")
            
    except KeyboardInterrupt:
        exit()
    except Exception as e:
        print(f"An error occurred: {e}")


def handle_linked_list_operations(linked_list):
    while True:
        display_main_operations_menu()
        try:
            choice = input("\nEnter your choice (0-8): ").strip()
            
            if choice == '0':
                exit()
            elif choice == '1':
                # Insert operations
                handle_insert_operations(linked_list)
            elif choice == '2':
                # Remove operations
                handle_remove_operations(linked_list)
            elif choice == '3':
                # Peek operations
                handle_peek_operations(linked_list)
            elif choice == '4':
                # Find Value
                if linked_list.isEmpty():
                    print("List is empty - no values to find")
                else:
                    value_to_find = input("Enter the value to find: ").strip()
                    if value_to_find:
                        found = linked_list.find(value_to_find)
                        if found:
                            print(f"Value '{value_to_find}' found in the list")
                        else:
                            print(f"Value '{value_to_find}' not found in the list")
                    else:
                        print("Error: Value cannot be empty")
            elif choice == '6':
                # Get Count
                count = linked_list.getCount()
                print(f"Current count: {count}")
            elif choice == '7':
                # Display operations
                handle_display_operations(linked_list)
            elif choice == '8':
                # Back to main menu
                break
            else:
                print("Invalid choice. Please enter a number between 0-8.")
                
        except KeyboardInterrupt:
            exit()
        except Exception as e:
            print(f"An error occurred: {e}")


def main():    
    while True:
        print("\n" + "-"*50)
        print("LINKED LIST MENU")
        print("-"*50)
        print("1. Create a LinkedList")
        print("0. Exit")
        
        try:
            choice = input("\nEnter your choice (0-1): ").strip()
            
            if choice == '0':
                break
            elif choice == '1':
                # Create Empty Linked List
                linked_list = DSALinkedList()
                print("An empty linked list has been created successfully!")
                handle_linked_list_operations(linked_list)
            else:
                print("Invalid choice. Please enter 0 or 1.")
                
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
