import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from Week7_Graph.DSAGraph import DSAGraph


def display_main_menu():
    print("--- Graph ---")
    print("1) Add node")
    print("2) Delete node")
    print("3) Add edge")
    print("4) Delete edge")
    print("5) displayAsList")
    print("6) displayAsMatrix")
    print("7) Breadth First Search")
    print("8) Depth First Search")
    print("0) Exit")


def prompt_label(prompt_text="Enter label: "):
    return input(prompt_text).strip()


def prompt_label_value():
    lbl = input("Enter label: ").strip()
    val = input("Enter value (optional, press Enter to skip): ").strip()
    if val == "":
        val = None
    return lbl, val


def handle_add_node(g: DSAGraph):
    try:
        label, value = prompt_label_value()
        g.addVertex(label, value)
        print(f"Inserted vertex label={label}, value={value}")
    except Exception as e:
        print(f"Error: {e}")


def handle_delete_node(g: DSAGraph):
    try:
        label = prompt_label("Enter label to delete: ")
        if g.hasVertex(label):
            g.removeVertex(label)
            print(f"Deleted vertex '{label}'")
        else:
            print(f"Vertex not found: '{label}'")
    except Exception as e:
        print(f"Error: {e}")


def handle_add_edge(g: DSAGraph):
    try:
        a = prompt_label("Enter first label: ")
        b = prompt_label("Enter second label: ")
        g.addEdge(a, b)
        print(f"Added edge {a} - {b}{'' if not g._directed else ' (directed)'}")
    except Exception as e:
        print(f"Error: {e}")


def handle_delete_edge(g: DSAGraph):
    try:
        a = prompt_label("Enter first label: ")
        b = prompt_label("Enter second label: ")
        g.removeEdge(a, b)
        print(f"Deleted edge {a} - {b}{'' if not g._directed else ' (directed)'}")
    except Exception as e:
        print(f"Error: {e}")


def handle_display_as_list(g: DSAGraph):
    try:
        g.displayAsList()
    except Exception as e:
        print(f"Error: {e}")


def handle_display_as_matrix(g: DSAGraph):
    try:
        g.displayAsMatrix()
    except Exception as e:
        print(f"Error: {e}")


def _drain_pair_queue_to_lines(T):
    lines = []
    while not T.is_empty():
        try:
            v = T.dequeue()
            w = T.dequeue()
            lines.append(f"{v.getLabel()} -> {w.getLabel()}")
        except Exception:
            break
    return lines


def handle_bfs(g: DSAGraph):
    try:
        T = g.breadthFirstSearch()
        lines = _drain_pair_queue_to_lines(T)
        if len(lines) == 0:
            print("No traversal edges (graph may be empty or single vertex)")
        else:
            print("BFS discovery edges:")
            for ln in lines:
                print(ln)
    except Exception as e:
        print(f"Error: {e}")


def handle_dfs(g: DSAGraph):
    try:
        T = g.depthFirstSearch()
        lines = _drain_pair_queue_to_lines(T)
        if len(lines) == 0:
            print("No traversal edges (graph may be empty or single vertex)")
        else:
            print("DFS discovery edges:")
            for ln in lines:
                print(ln)
    except Exception as e:
        print(f"Error: {e}")


def main():
    # Choose directed vs undirected
    directed = False
    while True:
        print("\nChoose graph type:")
        print("1. Undirected")
        print("2. Directed")
        choice = input("Enter 1 or 2: ").strip()
        if choice == '1':
            directed = False
            break
        elif choice == '2':
            directed = True
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    g = DSAGraph(directed=directed)

    while True:
        display_main_menu()
        try:
            choice = input("\nEnter your choice (0-8): ").strip()
            if choice == '0':
                break
            elif choice == '1':
                handle_add_node(g)
            elif choice == '2':
                handle_delete_node(g)
            elif choice == '3':
                handle_add_edge(g)
            elif choice == '4':
                handle_delete_edge(g)
            elif choice == '5':
                handle_display_as_list(g)
            elif choice == '6':
                handle_display_as_matrix(g)
            elif choice == '7':
                handle_bfs(g)
            elif choice == '8':
                handle_dfs(g)
            else:
                print("Invalid choice. Please enter 0-8.")
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()


