from model.HospitalModel import HospitalModel
from view.HospitalView import HospitalView
from DataStructures.DSALinkedList import DSALinkedList

class HospitalController:
    """
    Controller class for Hospital Management System.
    Handles business logic and coordinates between Model and View.
    """
    
    def __init__(self, config_file="hospital_config.json"):
        self.model = HospitalModel(config_file)
        self.view = HospitalView()
        self.running = True
    
    def run(self):
        self.view.display_welcome()
        
        while self.running:
            try:
                self.view.display_main_menu()
                choice = self.view.get_user_choice()
                
                if choice is None:
                    continue
                
                if choice == 1:
                    self.handle_shortest_path()
                elif choice == 2:
                    self.handle_reachable_departments()
                elif choice == 3:
                    self.handle_cycle_detection()
                elif choice == 4:
                    self.handle_display_map()
                elif choice == 5:
                    self.handle_display_matrix()
                elif choice == 6:
                    self.handle_department_info()
                elif choice == 7:
                    self.handle_exit()
                else:
                    self.view.display_error("Invalid choice. Please select 1-7.")
                
                if self.running:
                    self.view.display_separator()
                    input("Press Enter to continue...")
                    
            except KeyboardInterrupt:
                self.view.display_success("Application interrupted by user")
                self.running = False
            except Exception as e:
                self.view.display_error(f"Unexpected error: {e}")
    
    def handle_shortest_path(self):
        print("\nFIND SHORTEST PATH")
        print("-" * 30)
        
        # Display available departments
        departments = self.model.get_departments()
        self.view.display_departments(departments)
        
        # Get start department
        start_dept = self.view.get_department_input("Enter starting department")
        if not start_dept:
            self.view.display_error("Starting department cannot be empty")
            return
        
        # Get end department
        end_dept = self.view.get_department_input("Enter destination department")
        if not end_dept:
            self.view.display_error("Destination department cannot be empty")
            return
        
        # Find shortest path
        result = self.model.find_shortest_path(start_dept, end_dept)
        
        # Display results
        if result is None:
            self.view.display_error("No path found or error occurred")
            return
        
        path = result.getPath()
        total_cost = result.getCost()
        
        # Check if no path was found (empty path or infinite cost)
        if path.isEmpty() or total_cost == float('inf'):
            self.view.display_error("No path found between departments")
            return
        
        self.view.display_shortest_path(path, total_cost, start_dept, end_dept)
    
    def handle_reachable_departments(self):
        print("\nGET REACHABLE DEPARTMENTS")
        print("-" * 30)
        
        # Display available departments
        departments = self.model.get_departments()
        self.view.display_departments(departments)
        
        # Get start department
        start_dept = self.view.get_department_input("Enter starting department")
        if not start_dept:
            self.view.display_error("Starting department cannot be empty")
            return
        
        # Get reachable departments
        levels = self.model.get_reachable_departments(start_dept)
        
        # Display results
        self.view.display_reachable_departments(levels, start_dept)
    
    def handle_cycle_detection(self):
        print("\nCYCLE DETECTION")
        print("-" * 30)
        
        # Display available departments
        departments = self.model.get_departments()
        self.view.display_departments(departments)
        
        # Get start department
        start_dept = self.view.get_department_input("Enter starting department")
        if not start_dept:
            self.view.display_error("Starting department cannot be empty")
            return
        
        # Detect cycles
        cycles = self.model.detect_cycles(start_dept)
        
        # Display results
        self.view.display_cycles(cycles, start_dept)
    
    def handle_display_map(self):
        print("\nDISPLAY HOSPITAL MAP")
        print("-" * 30)
        
        graph = self.model.get_graph()
        self.view.display_hospital_map(graph)
    
    def handle_display_matrix(self):
        """Handle display matrix functionality."""
        print("\nDISPLAY DISTANCE MATRIX")
        print("-" * 30)
        
        graph = self.model.get_graph()
        self.view.display_distance_matrix(graph)
    
    def handle_department_info(self):
        print("\nDEPARTMENT INFORMATION")
        print("-" * 30)
        
        # Display available departments
        departments = self.model.get_departments()
        self.view.display_departments(departments)
        
        # Get department name
        dept_name = self.view.get_department_input("Enter department name")
        if not dept_name:
            self.view.display_error("Department name cannot be empty")
            return
        
        # Get department information
        dept_info = self.model.get_department_info(dept_name)
        self.view.display_department_info(dept_info, dept_name)
        
        if dept_info:
            # Get adjacent departments
            adjacent_depts = self.model.get_adjacent_departments(dept_name)
            self.view.display_adjacent_departments(adjacent_depts, dept_name)
            
            # Show corridor times to adjacent departments
            if adjacent_depts:
                print(f"\nWalking times from {dept_name}:")
                for adj_dept in adjacent_depts:
                    time = self.model.get_corridor_time(dept_name, adj_dept)
                    if time:
                        print(f"   → {adj_dept}: {time} minutes")
    
    def handle_exit(self):
        """Handle exit functionality."""
        if self.view.get_confirmation("Are you sure you want to exit?"):
            self.view.display_goodbye()
            self.running = False
        else:
            self.view.display_success("Continuing with the application")
    
