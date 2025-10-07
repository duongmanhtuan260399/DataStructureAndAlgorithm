import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from Week9_Heap.DSAHeap import DSAHeap  # noqa: E402


def display_main_menu():
    print("--- Heap ---")
    print("1) Add (priority, value)")
    print("2) Remove max (pop)")
    print("3) Display heap array")
    print("4) Size")
    print("5) Is empty?")
    print("0) Exit")


def _prompt_int(prompt_text="Enter integer: "):
    while True:
        s = input(prompt_text).strip()
        try:
            return int(s)
        except ValueError:
            print("Please enter a valid integer.")


def handle_add(h: DSAHeap):
    try:
        p = _prompt_int("Enter priority (int): ")
        v = input("Enter value (string, optional, press Enter for None): ").strip()
        if v == "":
            v = None
        h.add(p, v)
        print(f"Inserted ({p}, {v})")
    except Exception as e:
        print(f"Error: {e}")


def handle_remove(h: DSAHeap):
    try:
        v = h.remove()
        print(f"Removed value with highest priority: {v}")
    except Exception as e:
        print(f"Error: {e}")


def handle_display(h: DSAHeap):
    try:
        h.display()
    except Exception as e:
        print(f"Error: {e}")


def handle_size(h: DSAHeap):
    print(f"Size: {h.count}")


def handle_is_empty(h: DSAHeap):
    print("Yes" if h.count == 0 else "No")


def main():
    # optional: allow custom initial capacity
    try:
        cap_str = input("Enter initial capacity (press Enter for default 5): ").strip()
        if cap_str == "":
            heap = DSAHeap()
        else:
            heap = DSAHeap(int(cap_str))
    except Exception:
        heap = DSAHeap()

    while True:
        display_main_menu()
        try:
            choice = input("\nEnter your choice (0-5): ").strip()
            if choice == '0':
                break
            elif choice == '1':
                handle_add(heap)
            elif choice == '2':
                handle_remove(heap)
            elif choice == '3':
                handle_display(heap)
            elif choice == '4':
                handle_size(heap)
            elif choice == '5':
                handle_is_empty(heap)
            else:
                print("Invalid choice. Please enter 0-5.")
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()


