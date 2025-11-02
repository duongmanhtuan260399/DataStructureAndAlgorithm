#!/usr/bin/env python3
"""
Hospital Management System - Main Application
Module 1: DSAWeightedGraph Implementation
Module 2: Patient Management System

This application demonstrates the use of DSAWeightedGraph for hospital
navigation and management, and hash-based patient lookup system,
following MVC architecture.

Features:
- Shortest path finding using A* algorithm
- Reachable departments using BFS
- Cycle detection using DFS
- Hospital floor plan visualization
- Department information management
- Hash-based patient lookup with O(1) operations
- Patient record management with collision handling
- Performance testing and load factor management

Author: Manh Tuan Duong
Date: 22/10/2025
"""

import sys
import os

# Add the current directory to Python path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from controller.HospitalController import HospitalController
from controller.PatientController import PatientController

def display_main_menu():
    """Display the main application menu."""
    print("\nHOSPITAL MANAGEMENT SYSTEM")
    print("=" * 60)
    print("1. Hospital Navigation (Module 1)")
    print("2. Patient Management System (Module 2)")
    print("3. Exit")
    print("=" * 60)

def get_main_choice():
    """Get user's main menu choice."""
    try:
        choice = input("Enter your choice (1-3): ").strip()
        return int(choice)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

def run_hospital_navigation():
    """Run the hospital navigation system (Module 1)."""
    try:
        print("\nStarting Hospital Navigation System...")
        hospital_app = HospitalController("config/hospital_config.json")
        hospital_app.run()
    except FileNotFoundError as e:
        print(f"Configuration file not found: {e}")
        print("Please ensure 'config/hospital_config.json' exists in the current directory.")
    except Exception as e:
        print(f"Error in hospital navigation: {e}")

def run_patient_management():
    """Run the patient management system (Module 2)."""
    try:
        print("\nStarting Patient Management System...")
        patient_app = PatientController("config/patient_config.json")
        patient_app.run_patient_management()
    except Exception as e:
        print(f"Error in patient management system: {e}")

def main():
    """
    Main function to run the Hospital Management System.
    """
    print("WELCOME TO HOSPITAL MANAGEMENT SYSTEM")
    print("=" * 60)
    
    running = True
    while running:
        try:
            display_main_menu()
            choice = get_main_choice()
            
            if choice is None:
                continue
            
            if choice == 1:
                run_hospital_navigation()
            elif choice == 2:
                run_patient_management()
            elif choice == 3:
                running = False
            else:
                print("Invalid choice. Please select 1-3.")
            if running:
                input("\nPress Enter to continue...")
                
        except KeyboardInterrupt:
            print("\n\nApplication interrupted by user.")
            running = False
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
