import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from Week6_Tree.DSABinarySearchTree import DSABinarySearchTree


def display_main_menu():
    print("\n--- Binary Search Tree ---")
    print("1. Add node")
    print("2. Delete node")
    print("3. Display traversal")
    print("4. Find key")
    print("5. Min / Max / Height / Balance")
    print("0. Exit")


def display_traversal_menu():
    print("\n--- Traversal Options ---")
    print("1. Inorder")
    print("2. Preorder")
    print("3. Postorder")
    print("0. Back")


def prompt_key_value(compare_as_string):
    while True:
        key_str = input("Enter key: ").strip()
        if compare_as_string:
            key = key_str
            break
        else:
            try:
                key = int(key_str)
                break
            except ValueError:
                print("Invalid key. Please enter an integer.")
                continue
    val = input("Enter value: ").strip()
    return key, val


def handle_add_node(bst: DSABinarySearchTree, compare_as_string: bool):
    try:
        key, value = prompt_key_value(compare_as_string)
        bst.insert(key, value)
        print(f"Inserted key={key}, value={value}")
    except Exception as e:
        print(f"Error: {e}")


def handle_delete_node(bst: DSABinarySearchTree, compare_as_string: bool):
    try:
        key_str = input("Enter key to delete: ").strip()
        if compare_as_string:
            key = key_str
        else:
            key = int(key_str)
        deleted = bst.delete(key)
        print(f"Deleted key={key}, value={deleted}")
    except Exception as e:
        print(f"Error: {e}")


def handle_display_traversal(bst: DSABinarySearchTree):
    while True:
        display_traversal_menu()
        choice = input("\nEnter your choice (0-3): ").strip()
        if choice == '0':
            break
        elif choice == '1':
            seq_ll = bst.inorder()
            print("Inorder:")
            seq_ll.display()
        elif choice == '2':
            seq_ll = bst.preorder()
            print("Preorder:")
            seq_ll.display()
        elif choice == '3':
            seq_ll = bst.postorder()
            print("Postorder:")
            seq_ll.display()
        else:
            print("Invalid choice. Please enter 0-3.")

def handle_find_key(bst: DSABinarySearchTree, compare_as_string: bool):
    try:
        key_str = input("Enter key to find: ").strip()
        if compare_as_string:
            key = key_str
        else:
            key = int(key_str)
        value = bst.find(key)
        print(f"Found key={key} with value={value}")
    except Exception as e:
        print(f"Error: {e}")


def handle_stats(bst: DSABinarySearchTree):
    try:
        print(f"Min: {bst.min()}")
        print(f"Max: {bst.max()}")
        print(f"Height: {bst.height()}")
        print(f"Balance: {bst.balance()}%")
    except Exception as e:
        print(f"Error: {e}")


def main():
    # Choose key comparison mode
    compare_as_string = False
    while True:
        print("\nChoose key type for BST comparisons:")
        print("1. Integer keys")
        print("2. String keys")
        choice = input("Enter 1 or 2: ").strip()
        if choice == '1':
            compare_as_string = False
            break
        elif choice == '2':
            compare_as_string = True
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    bst = DSABinarySearchTree()
    if hasattr(bst, "init"):
        bst.init(keey_type_tring=compare_as_string)

    while True:
        display_main_menu()
        try:
            choice = input("\nEnter your choice (0-5): ").strip()
            if choice == '0':
                break
            elif choice == '1':
                handle_add_node(bst, compare_as_string)
            elif choice == '2':
                handle_delete_node(bst, compare_as_string)
            elif choice == '3':
                handle_display_traversal(bst)
            elif choice == '4':
                handle_find_key(bst, compare_as_string)
            elif choice == '5':
                handle_stats(bst)
            else:
                print("Invalid choice. Please enter 0-5.")
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()


