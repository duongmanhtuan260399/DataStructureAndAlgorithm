from .DSALinkedList import DSALinkedList
from .DSALinkedList_Queue import DSAQueue
from .DSALinkedList_Stack import DSAStack
from .DSAHeap import DSAHeap
from .DSAHeapMin import DSAHeapMin
from .DSAHashTable import DSAHashTable

class DSAGraphEdge:
    def __init__(self, destination_node, weight):
        self.destination = destination_node
        self.weight = weight
    
    def __eq__(self, other):
        if isinstance(other, DSAGraphEdge):
            return self.destination == other.destination
        return self.destination == other
    
    def __str__(self):
        return f"->{self.destination.label}({self.weight})"
    
    def getDestination(self):
        return self.destination
    
    def getWeight(self):
        return self.weight


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
    
    def addWeightedEdge(self, other_node, weight):
        """Add a weighted edge to another node."""
        if not self._adjacency.find(DSAGraphEdge(other_node, weight)):
            edge = DSAGraphEdge(other_node, weight)
            self._adjacency.insertLast(edge)
    
    def removeEdge(self, other_node):
        """Remove edge to another node."""
        for edge in self._adjacency:
            if edge.getDestination() == other_node:
                self._adjacency.remove(edge)
                break
    
    def getEdgeWeight(self, other_node):
        """Get the weight of edge to another node, or None if no edge exists."""
        for edge in self._adjacency:
            if edge.getDestination() == other_node:
                return edge.getWeight()
        return None
    
    def setVisited(self):
        self._visited = True
    
    def clearVisited(self):
        self._visited = False
    
    def getVisited(self):
        return self._visited
    
    def toString(self):
        return f"{self.label}" if self.value is None else f"{self.label}({self.value})"


class DSAWeightedGraph:
    """
    Weighted undirected graph implementation using adjacency list.
    Supports dynamic insertion of nodes and weighted edges.
    Ensures undirected symmetry (u↔v with same weight).
    """
    
    def __init__(self):
        self._vertices = DSALinkedList()
        self._vertex_count = 0
        self._edge_count = 0
    
    def _get_node(self, label):
        """Get node by label, raise ValueError if not found."""
        for node in self._vertices:
            if node.label == label:
                return node
        raise ValueError(f"Vertex '{label}' not found")
    
    def _ensure_vertex(self, label, value=None):
        """Get existing vertex or create new one."""
        try:
            return self._get_node(label)
        except ValueError:
            self.addVertex(label, value)
            return self._get_node(label)
    
    def getVertexCount(self):
        return self._vertex_count
    
    def getEdgeCount(self):
        return self._edge_count
    
    def hasVertex(self, label):
        """Check if vertex exists."""
        try:
            self._get_node(label)
            return True
        except ValueError:
            return False
    
    def addVertex(self, label, value=None):
        """Add a new vertex."""
        if self.hasVertex(label):
            raise ValueError(f"Vertex '{label}' already exists")
        node = DSAGraphNode(label, value)
        self._vertices.insertLast(node)
        self._vertex_count += 1
    
    def getVertex(self, label):
        """Get vertex by label."""
        return self._get_node(label)
    
    def isAdjacent(self, label1, label2):
        """Check if two vertices are connected."""
        if not (self.hasVertex(label1) and self.hasVertex(label2)):
            return False
        n1 = self._get_node(label1)
        n2 = self._get_node(label2)
        
        # Check if n1 has edge to n2
        for edge in n1.getAdjacent():
            if edge.getDestination() == n2:
                return True
        return False
    
    def addWeightedEdge(self, label1, label2, weight):
        """Add weighted edge between two vertices (undirected)."""
        if label1 == label2:
            raise ValueError("No self-loops supported")
        
        n1 = self._ensure_vertex(label1)
        n2 = self._ensure_vertex(label2)
        
        # Check if edge already exists
        if self.isAdjacent(label1, label2):
            return  # Already connected
        
        # Add edge in both directions (undirected)
        n1.addWeightedEdge(n2, weight)
        n2.addWeightedEdge(n1, weight)
        self._edge_count += 1
    
    def getEdgeWeight(self, label1, label2):
        """Get weight of edge between two vertices."""
        if not self.isAdjacent(label1, label2):
            return None
        n1 = self._get_node(label1)
        n2 = self._get_node(label2)
        return n1.getEdgeWeight(n2)
    
    def removeEdge(self, label1, label2):
        """Remove edge between two vertices."""
        if not (self.hasVertex(label1) and self.hasVertex(label2)):
            return
        
        n1 = self._get_node(label1)
        n2 = self._get_node(label2)
        
        if self.isAdjacent(label1, label2):
            n1.removeEdge(n2)
            n2.removeEdge(n1)
            self._edge_count = max(0, self._edge_count - 1)
    
    def removeVertex(self, label):
        """Remove vertex and all its edges."""
        if not self.hasVertex(label):
            return
        
        target = self._get_node(label)
        
        # Remove all edges to this vertex
        for node in self._vertices:
            if node == target:
                continue
            if self.isAdjacent(node.label, label):
                self.removeEdge(node.label, label)
        
        # Remove the vertex
        self._vertices.remove(target)
        self._vertex_count = max(0, self._vertex_count - 1)
    
    def getAdjacent(self, label):
        """Get adjacency list for a vertex."""
        node = self._get_node(label)
        return node.getAdjacent()
    
    def getAdjList(self, label):
        """Get adjacency list for a vertex (alias for getAdjacent for compatibility)."""
        return self.getAdjacent(label)
    
    def getAdjacentCount(self, label):
        """Get number of adjacent vertices."""
        node = self._get_node(label)
        return sum(1 for _ in node.getAdjacent())
    
    def clearVisited(self):
        """Clear visited flag for all vertices."""
        for node in self._vertices:
            node.clearVisited()
    
    def displayAsList(self):
        """Display graph as adjacency list with weights."""
        if self.getVertexCount() == 0:
            print("Empty graph")
            return
        
        print(f"Weighted Undirected Graph: |V|={self._vertex_count}, |E|={self._edge_count}")
        for node in self._vertices:
            edges = DSALinkedList()
            for edge in node.getAdjacent():
                edges.insertLast(f"{edge.getDestination().label}({edge.getWeight()})")
            
            # Build the output string
            if edges.isEmpty():
                print(f"{node.label}: []")
            else:
                output_parts = DSALinkedList()
                for edge_str in edges:
                    output_parts.insertLast(edge_str)
                
                # Convert to comma-separated string
                result = ""
                first = True
                for edge_str in output_parts:
                    if not first:
                        result += ", "
                    result += edge_str
                    first = False
                print(f"{node.label}: [{result}]")
    
    def displayAsMatrix(self):
        """Display graph as adjacency matrix with weights."""
        if self.getVertexCount() == 0:
            print("Empty graph")
            return
        
        # Convert vertices to DSALinkedList and build labels list
        nodes = DSALinkedList()
        labels = DSALinkedList()
        index_of = DSAHashTable()
        
        # Build nodes list and labels list
        for node in self._vertices:
            nodes.insertLast(node)
            labels.insertLast(node.label)
        
        # Build index mapping using DSAHashTable
        index = 0
        for label in labels:
            index_of.put(label, index)
            index += 1
        
        size = nodes.getCount()
        
        # Initialize matrix with 0s using DSALinkedList
        matrix = DSALinkedList()
        for i in range(size):
            row = DSALinkedList()
            for j in range(size):
                row.insertLast(0)
            matrix.insertLast(row)
        
        # Fill matrix with weights
        row_index = 0
        for node in nodes:
            for edge in node.getAdjacent():
                col_index = index_of.get(edge.getDestination().label)
                # Get the row and update the value
                row = matrix.peekAt(row_index)
                row.removeAt(col_index)
                row.insertAt(col_index, edge.getWeight())
            row_index += 1
        
        # Display matrix
        # Build header
        header_parts = DSALinkedList()
        header_parts.insertLast(" ")
        for label in labels:
            header_parts.insertLast(label)
        
        # Print header
        header_str = ""
        first = True
        for part in header_parts:
            if not first:
                header_str += "\t"
            header_str += part
            first = False
        print(header_str)
        
        # Print matrix rows
        row_index = 0
        for row in matrix:
            # Build row output
            row_parts = DSALinkedList()
            row_parts.insertLast(labels.peekAt(row_index))
            for val in row:
                row_parts.insertLast(str(val))
            
            # Print row
            row_str = ""
            first = True
            for part in row_parts:
                if not first:
                    row_str += "\t"
                row_str += part
                first = False
            print(row_str)
            row_index += 1
    
    def breadthFirstSearch(self, source_label):
        """
        Breadth-First Search starting from source department.
        Returns reachable departments grouped by traversal level (distance from source).
        """
        if not self.hasVertex(source_label):
            raise ValueError(f"Source vertex '{source_label}' not found")
        
        # Clear all visited flags
        self.clearVisited()
        
        # Initialize BFS
        queue = DSAQueue()
        source_node = self._get_node(source_label)
        source_node.setVisited()
        queue.enqueue(source_node)
        
        # Store levels using DSALinkedList
        levels = DSALinkedList()
        current_level = DSALinkedList()
        current_level.insertLast(source_node)
        levels.insertLast(current_level)
        
        while not queue.is_empty():
            current_level = DSALinkedList()
            level_size = queue.get_count()
            
            # Process all nodes at current level
            for _ in range(level_size):
                current_node = queue.dequeue()
                
                # Add unvisited neighbors to next level
                for edge in current_node.getAdjacent():
                    neighbor = edge.getDestination()
                    if not neighbor.getVisited():
                        neighbor.setVisited()
                        current_level.insertLast(neighbor)
                        queue.enqueue(neighbor)
            
            # Add level if it has nodes
            if not current_level.isEmpty():
                levels.insertLast(current_level)
        
        return levels
    
    def depthFirstSearch(self, start):
        """
        Perform depth-first search to find a cycle that includes the starting vertex.
        
        Args:
            start: The label of the vertex to start the search from.
            
        Returns:
            DSALinkedList: An array of nodes that form a cycle including the start vertex, or empty list if no cycle found.
        """
        if not self.hasVertex(start):
            raise ValueError(f"Source vertex '{start}' not found in the graph.")
        
        # Clear all visited flags
        self.clearVisited()
        
        # Track the current path
        self._dfs_path = DSALinkedList()
        
        # Start DFS from the given start node
        result = self._dfs_visit(start, start)
        
        # Clean up
        self.clearVisited()
        self._dfs_path = None
        
        return result
    
    def _dfs_visit(self, current_label, start_label, parent_label=None):
        # Add current node to path
        self._dfs_path.insertLast(current_label)
        
        # Get adjacent nodes
        adj_edges = self.getAdjList(current_label)
        if adj_edges is not None:
            for edge in adj_edges:
                neighbor_label = edge.getDestination().label
                
                # Skip the parent node to avoid going back
                if neighbor_label == parent_label:
                    continue
                
                # Check if we've found a cycle (neighbor is already in current path)
                if self._isInPath(self._dfs_path, neighbor_label):
                    # Found a cycle! Extract the cycle from the path
                    cycle = DSALinkedList()
                    
                    # Find the position of the neighbor in the path and build cycle
                    cycle_started = False
                    for node_label in self._dfs_path:
                        if node_label == neighbor_label:
                            cycle_started = True
                        if cycle_started:
                            cycle.insertLast(node_label)
                    
                    # Add the current node to complete the cycle (only if not already added)
                    if cycle.isEmpty() or cycle.peekLast() != current_label:
                        cycle.insertLast(current_label)
                    
                    # Only return if it's a valid cycle (at least 3 nodes) AND includes the start vertex
                    if (cycle.getCount() >= 3 and 
                        self._isInPath(cycle, start_label)):
                        # Remove current node from path before returning
                        self._dfs_path.removeLast()
                        return cycle
                
                # If neighbor not in current path, continue DFS
                if not self._isInPath(self._dfs_path, neighbor_label):
                    result = self._dfs_visit(neighbor_label, start_label, current_label)
                    if not result.isEmpty():
                        # Found a cycle, return it
                        self._dfs_path.removeLast()
                        return result
        
        # No cycle found from this node, backtrack
        self._dfs_path.removeLast()
        return DSALinkedList()  # Empty list means no cycle found

    def _markVisited(self, visited_list, node):
        """Mark a node as visited by adding it to the visited list."""
        if not self._isVisited(visited_list, node):
            visited_list.insertLast(node)
    
    def _isVisited(self, visited_list, node):
        """Check if a node has been visited."""
        return visited_list.find(node) is not None
    
    def _isInPath(self, path_list, node):
        """Check if a node is currently in the DFS path."""
        return path_list.find(node)
    
    def _containsCycle(self, cycles, newCycle):
        """Check if a cycle already exists in the cycles list."""
        # Avoid duplicates by comparing values (same members)
        current = cycles._head
        while current is not None:
            existing = current.value
            if self._sameCycle(existing, newCycle):
                return True
            current = current.next
        return False

    def _sameCycle(self, c1, c2):
        """Check if two cycles are the same (contain the same nodes)."""
        if c1.getCount() != c2.getCount():
            return False
        for v in c1:
            if not c2.find(v):
                return False
        return True
    
    def aStarPathfinding(self, start_label, goal_label):
        """
        A* pathfinding algorithm implementation.
        
        Args:
            start_label: Label of the starting vertex
            goal_label: Label of the destination vertex
            
        Returns:
            AStarPath: Object containing the path (as DSALinkedList) and total cost
        """
        if not self.hasVertex(start_label):
            raise ValueError(f"Start vertex '{start_label}' not found")
        if not self.hasVertex(goal_label):
            raise ValueError(f"Goal vertex '{goal_label}' not found")
        
        if start_label == goal_label:
            # Same start and goal
            path = DSALinkedList()
            path.insertLast(start_label)
            return AStarPath(path, 0)
        
        # Clear visited flags
        self.clearVisited()
        
        # Initialize open and closed sets
        open_set = DSAHeapMin()  # Min-heap priority queue for A* nodes
        closed_set = DSAHashTable()  # Hash table for visited nodes
        open_set_nodes = DSAHashTable()  # Track nodes in open set for efficient lookup
        
        # Get start and goal nodes
        start_node = self._get_node(start_label)
        goal_node = self._get_node(goal_label)
        
        # Create initial A* node
        start_astar = AStarNode(start_node, 0, self._heuristic(start_node, goal_node))
        # Use f_cost directly for min-heap behavior
        open_set.add(start_astar.f_cost, start_astar)
        open_set_nodes.put(start_node.label, start_astar)
        
        # A* main loop
        while not open_set.isEmpty():
            # Get node with lowest f_cost
            current_astar = open_set.remove()
            current_node = current_astar.node
            
            # Remove from open set tracking
            open_set_nodes.remove(current_node.label)
            
            # Check if we reached the goal
            if current_node == goal_node:
                # Reconstruct path
                path = DSALinkedList()
                total_cost = current_astar.g_cost
                
                # Build path from goal to start
                while current_astar is not None:
                    path.insertFirst(current_astar.node.label)
                    current_astar = current_astar.parent
                
                return AStarPath(path, total_cost)
            
            # Add to closed set
            closed_set.put(current_node.label, current_astar)
            current_node.setVisited()
            
            # Explore neighbors
            for edge in current_node.getAdjacent():
                neighbor = edge.getDestination()
                edge_weight = edge.getWeight()
                
                # Skip if already visited or in closed set
                if neighbor.getVisited() or closed_set.hasKey(neighbor.label):
                    continue
                
                # Calculate costs
                tentative_g_cost = current_astar.g_cost + edge_weight
                h_cost = self._heuristic(neighbor, goal_node)
                f_cost = tentative_g_cost + h_cost
                
                # Check if this neighbor is already in open set
                if open_set_nodes.hasKey(neighbor.label):
                    neighbor_astar = open_set_nodes.get(neighbor.label)
                    if tentative_g_cost < neighbor_astar.g_cost:
                        # Found better path to this neighbor
                        neighbor_astar.g_cost = tentative_g_cost
                        neighbor_astar.f_cost = tentative_g_cost + h_cost
                        neighbor_astar.parent = current_astar
                        # Re-heapify the heap
                        open_set.heapify()
                else:
                    # New node, add to open set
                    new_astar = AStarNode(neighbor, tentative_g_cost, h_cost, current_astar)
                    open_set.add(new_astar.f_cost, new_astar)
                    open_set_nodes.put(neighbor.label, new_astar)
        
        # No path found
        return AStarPath(DSALinkedList(), float('inf'))
    
    def _heuristic(self, current_node, goal_node):
        """
        Heuristic function for A* algorithm.
        Uses a more conservative heuristic that ensures admissibility.
        """
        # If there's a direct connection, use that edge weight
        if self.isAdjacent(current_node.label, goal_node.label):
            return self.getEdgeWeight(current_node.label, goal_node.label)
        
        # For nodes without direct connection, use a conservative heuristic
        # that estimates the minimum possible cost to reach the goal
        # This ensures the heuristic is admissible (never overestimates)
        return 0  # Conservative heuristic - always underestimate
    
    def _findInOpenSet(self, open_set, target_node):
        """
        Find an AStarNode in the open set that corresponds to the target node.
        Returns None if not found.
        """
        # Since we can't directly search the heap, we'll need to rebuild it
        # This is not the most efficient, but works with our DSAHeap implementation
        temp_entries = DSALinkedList()
        found_node = None
        
        # Extract all entries from heap
        while not open_set.isEmpty():
            entry = open_set.remove()
            if entry.node == target_node:
                found_node = entry
            temp_entries.insertLast(entry)
        
        # Rebuild the heap
        for entry in temp_entries:
            open_set.add(-entry.f_cost, entry)
        
        return found_node


class AStarNode:
    """Helper class for A* pathfinding algorithm."""
    
    def __init__(self, node, g_cost=0, h_cost=0, parent=None):
        self.node = node
        self.g_cost = g_cost  # Cost from start to this node
        self.h_cost = h_cost  # Heuristic cost from this node to goal
        self.f_cost = g_cost + h_cost  # Total cost
        self.parent = parent
    
    def __lt__(self, other):
        """For priority queue comparison."""
        return self.f_cost < other.f_cost
    
    def __eq__(self, other):
        """For equality comparison."""
        if isinstance(other, AStarNode):
            return self.node == other.node
        return self.node == other
    
    def __str__(self):
        return f"AStarNode({self.node.label}, f={self.f_cost}, g={self.g_cost}, h={self.h_cost})"


class AStarPath:
    """Container for A* pathfinding results."""
    
    def __init__(self, path=None, cost=0):
        self.path = path if path is not None else DSALinkedList()
        self.cost = cost
    
    def getPath(self):
        return self.path
    
    def getCost(self):
        return self.cost