import json
from DataStructures.DSAWeightedGraph import DSAWeightedGraph, AStarPath
from DataStructures.DSALinkedList import DSALinkedList

class HospitalModel:
    """
    Model class for Hospital Management System.
    Manages the hospital graph structure and data operations.
    """
    
    def __init__(self, config_file="hospital_config.json"):
        """
        Initialize the hospital model with configuration file.
        
        Args:
            config_file (str): Path to JSON configuration file
        """
        self.config_file = config_file
        self.graph = DSAWeightedGraph()
        self.load_hospital_data(config_file)
    
    def load_hospital_data(self, config_file):
        """
        Load hospital departments and corridors from JSON configuration file.
        """
        try:
            with open(self.config_file, 'r') as file:
                data = json.load(file)
            
            # Add all departments as vertices
            for dept in data:
                department_name = dept["department"]
                
                # Add vertex
                self.graph.addVertex(department_name)
            
            # Add corridors as weighted edges
            for dept in data:
                department_name = dept["department"]
                corridors = dept.get("corridors", [])
                
                for corridor in corridors:
                    target_dept = corridor["department"]
                    weight = corridor["weight"]
                    
                    # Add weighted edge (undirected)
                    self.graph.addWeightedEdge(department_name, target_dept, weight)
            
            print(f"Loaded {self.graph.getVertexCount()} departments with {self.graph.getEdgeCount()} corridors")
            
        except FileNotFoundError:
            print(f"Error: Configuration file '{self.config_file}' not found")
            raise
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON in configuration file '{self.config_file}'")
            raise
        except Exception as e:
            print(f"Error loading hospital data: {e}")
            raise
    
    def get_departments(self):
        """
        Get list of all departments.
        
        Returns:
            DSALinkedList: The graph's vertices (departments)
        """
        return self.graph._vertices
    
    def get_graph(self):
        """
        Get the hospital graph.
        
        Returns:
            DSAWeightedGraph: The hospital graph
        """
        return self.graph
    
    def find_shortest_path(self, start_dept, end_dept):
        """
        Find shortest path between two departments using A* algorithm.
        
        Args:
            start_dept (str): Starting department name
            end_dept (str): Ending department name
            
        Returns:
            AStarPath: Object containing path and cost, or None if no path found
        """
        try:
            return self.graph.aStarPathfinding(start_dept, end_dept)
        except ValueError as e:
            print(f"Error finding path: {e}")
            return None
    
    def get_reachable_departments(self, start_dept):
        """
        Get all departments reachable from a starting department using BFS.
        
        Args:
            start_dept (str): Starting department name
            
        Returns:
            DSALinkedList: List of levels containing reachable departments
        """
        try:
            return self.graph.breadthFirstSearch(start_dept)
        except ValueError as e:
            print(f"Error getting reachable departments: {e}")
            return None
    
    def detect_cycles(self, start_dept):
        """
        Detect cycles in the hospital graph using DFS.
        
        Args:
            start_dept (str): Starting department name
            
        Returns:
            DSALinkedList: List containing one cycle (if found), or empty list if no cycles
        """
        try:
            cycle = self.graph.depthFirstSearch(start_dept)
            
            # Wrap the single cycle in a list for consistent handling
            cycles_list = DSALinkedList()
            if not cycle.isEmpty():
                cycles_list.insertLast(cycle)
            
            return cycles_list
        except ValueError as e:
            print(f"Error detecting cycles: {e}")
            return DSALinkedList()  # Return empty list instead of None
    
    def get_department_info(self, dept_name):
        """
        Get information about a specific department.
        
        Args:
            dept_name (str): Department name
            
        Returns:
            dict: Department information or None if not found
        """
        try:
            node = self.graph.getVertex(dept_name)
            return {
                "name": node.label
            }
        except ValueError:
            return None
    
    def get_adjacent_departments(self, dept_name):
        """
        Get departments adjacent to a given department.
        
        Args:
            dept_name (str): Department name
            
        Returns:
            DSALinkedList: List of adjacent department names
        """
        try:
            adjacent = self.graph.getAdjacent(dept_name)
            adjacent_names = DSALinkedList()
            for edge in adjacent:
                adjacent_names.insertLast(edge.getDestination().label)
            return adjacent_names
        except ValueError:
            return DSALinkedList()
    
    def get_corridor_time(self, dept1, dept2):
        """
        Get walking time between two departments.
        
        Args:
            dept1 (str): First department name
            dept2 (str): Second department name
            
        Returns:
            float: Walking time in minutes, or None if no direct connection
        """
        try:
            return self.graph.getEdgeWeight(dept1, dept2)
        except ValueError:
            return None
    
