import DSALinkedList
import DSALinkedList_Queue
import DSALinkedList_Stack
import numpy as np

class DSAGraphNode:

    def __init__(self, label, value=None):
        self.label = str(label)
        self.value = value
        self._adjacency = DSALinkedList()
        self._visited = False

    def __eq__(self, other):
        if isinstance(other, DSAGraphNode):
            return self.label == other.label
        return self.label == str(other)

    def getLabel(self):
        return self.label

    def getValue(self):
        return self.value

    def getAdjacent(self):
        return self._adjacency

    def addEdge(self, other_node):
        if not self._adjacency.find(other_node):
            self._adjacency.insertLast(other_node)

    def setVisited(self):
        self._visited = True

    def clearVisited(self):
        self._visited = False

    def getVisited(self):
        return self._visited

    def toString(self):
        return f"{self.label}" if self.value is None else f"{self.label}({self.value})"


class DSAGraph:

    def __init__(self, directed=False):
        self._vertices = DSALinkedList()
        self._directed = directed
        self._vertex_count = 0
        self._edge_count = 0


    def _sort_labels_list(self, labels_list):
        unsorted_ll = DSALinkedList()
        for lbl in labels_list:
            unsorted_ll.insertLast(lbl)
        sorted_ll = DSALinkedList()
        while unsorted_ll.getCount() > 0:
            # find min label in unsorted
            first = True
            min_label = None
            for lbl in unsorted_ll:
                if first:
                    min_label = lbl
                    first = False
                else:
                    if lbl < min_label:
                        min_label = lbl
            # move one instance of min_label to sorted
            unsorted_ll.remove(min_label)
            sorted_ll.insertLast(min_label)
        return sorted_ll

    def _get_node(self, label):
        return self._vertices.peek(label)

    def _ensure_vertex(self, label, value=None):
        if not self.hasVertex(label):
            self.addVertex(label, value)
        return self._get_node(label)

    def getVertexCount(self):
        return self._vertex_count

    def getEdgeCount(self):
        return self._edge_count

    def hasVertex(self, label):
        return self._vertices.find(label)

    def addVertex(self, label, value=None):
        if self.hasVertex(label):
            raise ValueError(f"Vertex '{label}' already exists")
        node = DSAGraphNode(label, value)
        self._vertices.insertLast(node)
        self._vertex_count += 1

    def getVertex(self, label):
        try:
            return self._get_node(label)
        except ValueError as e:
            raise ValueError(f"Vertex not found: '{label}'") from e

    def isAdjacent(self, label1, label2):
        if not (self.hasVertex(label1) and self.hasVertex(label2)):
            return False
        n1 = self._get_node(label1)
        n2 = self._get_node(label2)
        # scan adjacency list of n1
        for adj in n1.getAdjacent():
            if adj == n2:
                return True
        return False

    def addEdge(self, label1, label2):
        if label1 == label2:
            raise ValueError("No self-loops supported")
        n1 = self._ensure_vertex(label1)
        n2 = self._ensure_vertex(label2)

        if n1.getAdjacent().find(n2):
            return  # already connected; idempotent

        n1.addEdge(n2)
        if not self._directed:
            n2.addEdge(n1)
        self._edge_count += 1

    def removeEdge(self, label1, label2):
        if not (self.hasVertex(label1) and self.hasVertex(label2)):
            return
        n1 = self._get_node(label1)
        n2 = self._get_node(label2)
        if n1.getAdjacent().find(n2):
            n1.getAdjacent().remove(n2)
            if not self._directed and n2.getAdjacent().find(n1):
                n2.getAdjacent().remove(n1)
            self._edge_count = max(0, self._edge_count - 1)

    def removeVertex(self, label):
        if not self.hasVertex(label):
            return
        target = self._get_node(label)
        # Remove incoming references
        for node in self._vertices:
            if node is target:
                continue
            if node.getAdjacent().find(target):
                node.getAdjacent().remove(target)
                if not self._directed:
                    # For undirected graphs, removing incoming implies an edge removal
                    self._edge_count = max(0, self._edge_count - 1)
        # Remove the vertex itself
        self._vertices.remove(target)
        self._vertex_count = max(0, self._vertex_count - 1)

    def getAdjacent(self, label):
        try:
            node = self._get_node(label)
        except ValueError as e:
            raise ValueError(f"Cannot get adjacency list; vertex not found: '{label}'") from e
        return node.getAdjacent()

    def getAdjacentCount(self, label):
        node = self._get_node(label)
        return sum(1 for _ in node.getAdjacent())

    def displayAsList(self):
        if self.getVertexCount() == 0:
            print("Empty graph")
            return
            
        kind = "Directed" if self._directed else "Undirected"
        print(f"{kind} Graph: |V|={self._vertex_count}, |E|={self._edge_count}")
        
        # Iterate over the NumPy array of vertices
        for node in self._vertices:
            neighbors_str = ""
            adjacent_nodes = node.getAdjacent()
            
            if adjacent_nodes is not None:
                for adj in adjacent_nodes:
                    neighbors_str += adj.label + ", "
            
            if neighbors_str != "":
                neighbors_str = neighbors_str[:-2]
                
            print(f"{node.label}: [{neighbors_str}]")

    def displayAsMatrix(self):
        if self.getVertexCount() == 0:
            print("Empty graph")
            return
        
        nodes = self._vertices
        size = self._vertex_count
        
        labels = np.empty(size, dtype=object)
        for i in range(size):
            labels[i] = nodes[i].label
            
        matrix = np.zeros((size, size), dtype=int)
        
        for i in range(size):
            n = nodes[i]
            for adj in n.getAdjacent():
                j = self._find_label_index(labels, adj.label)
                if j != -1: # Check if found
                    matrix[i, j] = 1
                            
        # Print header row
        header_str = "\t" # Start with a tab for the empty corner
        for label in labels:
            header_str += label + "\t"
        print(header_str)
        
        # Print each matrix row
        for i in range(size):
            row_str = labels[i] + "\t" # Start with the row label
            for j in range(size):
                row_str += str(matrix[i, j]) + "\t"
            print(row_str)

    def _find_label_index(self, labels_array, target_label):
        """
        Helper function to find the index of a label in a NumPy array.
        """
        for i in range(labels_array.shape[0]):
            if labels_array[i] == target_label:
                return i
        return -1 # Indicates not found

    def breadthFirstSearch(self):
        T = DSALinkedList_Queue()
        Q = DSALinkedList_Queue()
        for node in self._vertices:
            node.clearVisited()
        labels = DSALinkedList()
        for n in self._vertices:
            labels.insertLast(n.label)
        start = None
        if labels.getCount() > 0:
            sorted_labels = self._sort_labels_list(labels)
            first_label = None
            for l in sorted_labels:
                first_label = l
                break
            if first_label is not None:
                for n in self._vertices:
                    if n.label == first_label:
                        start = n
                        break
        if start is not None:
            start.setVisited()
            Q.enqueue(start)
            while not Q.is_empty():
                v = Q.dequeue()
                neigh_labels = DSALinkedList()
                for n in v.getAdjacent():
                    neigh_labels.insertLast(n.label)
                ordered_neigh_labels = self._sort_labels_list(neigh_labels) if neigh_labels.getCount() > 0 else DSALinkedList()
                for lbl in ordered_neigh_labels:
                    # find neighbor by label
                    w = None
                    for n in v.getAdjacent():
                        if n.label == lbl:
                            w = n
                            break
                    if w is None:
                        continue
                    if not w.getVisited():
                        T.enqueue(v)
                        T.enqueue(w)
                        w.setVisited()
                        Q.enqueue(w)
        return T

    def depthFirstSearch(self):
        T = DSALinkedList_Queue()
        S = DSALinkedList_Stack()
        # clear visited
        for node in self._vertices:
            node.clearVisited()
        labels = DSALinkedList()
        for n in self._vertices:
            labels.insertLast(n.label)
        start = None
        if labels.getCount() > 0:
            sorted_labels = self._sort_labels_list(labels)
            first_label = None
            for l in sorted_labels:
                first_label = l
                break
            if first_label is not None:
                for n in self._vertices:
                    if n.label == first_label:
                        start = n
                        break
        if start is not None:
            start.setVisited()
            S.push(start)
            while not S.is_empty():
                v = S.top()
                progressed = False
                neigh_labels = DSALinkedList()
                for n in v.getAdjacent():
                    neigh_labels.insertLast(n.label)
                ordered_neigh_labels = self._sort_labels_list(neigh_labels) if neigh_labels.getCount() > 0 else DSALinkedList()
                for lbl in ordered_neigh_labels:
                    w = None
                    for n in v.getAdjacent():
                        if n.label == lbl:
                            w = n
                            break
                    if w is None:
                        continue
                    if not w.getVisited():
                        T.enqueue(v)
                        T.enqueue(w)
                        w.setVisited()
                        S.push(w)
                        progressed = True
                        break
                if not progressed:
                    S.pop()
        return T


