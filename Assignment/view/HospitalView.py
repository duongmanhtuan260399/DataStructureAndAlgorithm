from DataStructures.DSALinkedList import DSALinkedList

class HospitalView:
    """
    View class for Hospital Management System.
    Handles all user interface and display operations.
    """
    
    def __init__(self):
        """Initialize the hospital view."""
        pass
    
    def display_welcome(self):
        """Display welcome message."""
        print("=" * 60)
        print("HOSPITAL MANAGEMENT SYSTEM")
        print("=" * 60)
        print("Efficient navigation for patient transfers and equipment movement")
        print("=" * 60)
    
    def display_main_menu(self):
        """Display main menu options."""
        print("\nMAIN MENU")
        print("-" * 30)
        print("1. Find Shortest Path")
        print("2. Get Reachable Departments")
        print("3. Detect Cycles")
        print("4. Display Hospital Map")
        print("5. Display Distance Matrix")
        print("6. Department Information")
        print("7. Exit")
        print("-" * 30)
    
    def get_user_choice(self):
        """Get user menu choice."""
        try:
            choice = input("Enter your choice (1-7): ").strip()
            return int(choice)
        except ValueError:
            print("Invalid input. Please enter a number.")
            return None
    
    def get_department_input(self, prompt):
        """Get department name from user."""
        return input(f"{prompt}: ").strip()
    
    def display_departments(self, departments):
        """Display list of departments."""
        print("\nAvailable Departments:")
        print("-" * 40)
        i = 1
        for node in departments:
            print(f"{i:2d}. {node.label}")
            i += 1
        print("-" * 40)
    
    def display_shortest_path(self, path, total_cost, start_dept, end_dept):
        """Display shortest path results."""
        print(f"\nSHORTEST PATH: {start_dept} → {end_dept}")
        print("=" * 50)
        
        if path is None or total_cost is None:
            print("No path found between departments")
            return
        
        # Check if no path was found (empty path or infinite cost)
        if hasattr(path, 'isEmpty') and path.isEmpty():
            print("No path found between departments")
            return
        
        if total_cost == float('inf'):
            print("No path found between departments")
            return
        
        # Build path string using DSA-compliant iteration
        path_string = ""
        path_count = 0
        is_first = True
        
        for node in path:
            if is_first:
                path_string = str(node)
                is_first = False
            else:
                path_string += f" → {node}"
            path_count += 1
        
        print(f"Path: {path_string}")
        print(f"Total Walking Time: {total_cost} minutes")
        print(f"Number of Corridors: {path_count - 1}")
        
        # Display step-by-step directions using DSA-compliant iteration
        print("\nStep-by-Step Directions:")
        step_num = 1
        prev_node = None
        
        for node in path:
            if prev_node is not None:
                print(f"   {step_num}. From {prev_node} to {node}")
                step_num += 1
            prev_node = node
    
    def display_reachable_departments(self, levels, start_dept):
        """Display reachable departments by level."""
        print(f"\nREACHABLE DEPARTMENTS FROM: {start_dept}")
        print("=" * 50)
        
        if levels is None:
            print("Error getting reachable departments")
            return
        
        if levels.isEmpty():
            print("No reachable departments found")
            return
        
        level_num = 0
        for level in levels:
            if not level.isEmpty():
                print(f"\nLevel {level_num} (Walking time: {level_num} corridors away):")
                # Build department list string using DSA-compliant iteration
                dept_string = ""
                is_first = True
                
                for node in level:
                    if is_first:
                        dept_string = node.label
                        is_first = False
                    else:
                        dept_string += f", {node.label}"
                
                print(f"   Departments: {dept_string}")
                level_num += 1
    
    def display_cycles(self, cycles, start_dept):
        """Display detected cycles."""
        print(f"\nCYCLE DETECTION FROM: {start_dept}")
        print("=" * 50)
        
        if cycles is None:
            print("No cycles detected in the hospital graph")
            return
        
        if cycles.isEmpty():
            print(f"No cycles found that include '{start_dept}'")
            return
        
        print(f"{cycles.getCount()} cycle(s) found that include '{start_dept}':")
        
        cycle_num = 1
        for cycle in cycles:
            # Build cycle string using DSA-compliant iteration
            cycle_string = ""
            first_node = None
            is_first = True
            
            for node in cycle:
                if is_first:
                    first_node = node
                    cycle_string = str(node)
                    is_first = False
                else:
                    cycle_string += f" → {node}"
            
            if first_node:
                cycle_string += f" → {first_node}"
            
            print(f"   Cycle {cycle_num}: {cycle_string}")
            cycle_num += 1
    
    def display_hospital_map(self, graph):
        """Display hospital map."""
        print("\nHOSPITAL FLOOR PLAN")
        print("=" * 50)
        graph.displayAsList()
    
    def display_distance_matrix(self, graph):
        """Display distance matrix."""
        print("\nHOSPITAL DISTANCE MATRIX")
        print("=" * 50)
        graph.displayAsMatrix()
    
    def display_department_info(self, dept_info, dept_name):
        """Display department information."""
        print(f"\nDEPARTMENT INFORMATION: {dept_name}")
        print("=" * 50)
        
        if dept_info is None:
            print("Department not found")
            return
        
        print(f"Name: {dept_info['name']}")
    
    def display_adjacent_departments(self, adjacent_depts, dept_name):
        """Display adjacent departments."""
        print(f"\nADJACENT DEPARTMENTS TO: {dept_name}")
        print("=" * 50)
        
        if isinstance(adjacent_depts, DSALinkedList):
            if adjacent_depts.isEmpty():
                print("No adjacent departments found")
                return
            
            print("Connected departments:")
            i = 1
            for dept in adjacent_depts:
                print(f"   {i}. {dept}")
                i += 1
        else:
            # Handle regular list for backward compatibility
            if not adjacent_depts:
                print("No adjacent departments found")
                return
            
            print("Connected departments:")
            i = 1
            for dept in adjacent_depts:
                print(f"   {i}. {dept}")
                i += 1
    
    
    def display_error(self, message):
        """Display error message."""
        print(f"Error: {message}")
    
    def display_success(self, message):
        """Display success message."""
        print(f"Success: {message}")
    
    def display_separator(self):
        """Display separator line."""
        print("\n" + "=" * 60)
    
    def get_confirmation(self, message):
        """Get user confirmation."""
        response = input(f"{message} (y/n): ").strip().lower()
        return response in ['y', 'yes']
    
    def display_goodbye(self):
        """Display goodbye message."""
        print("\n" + "=" * 60)
        print("Thank you for using Hospital Management System!")
        print("Stay healthy and safe!")
        print("=" * 60)
