import csv
import os
from DSAHashTable import DSAHashTable

def load_names_from_csv(filename, hash_table):
    loaded_count = 0
    duplicate_count = 0
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            
            for row_num, row in enumerate(csv_reader, 1):
                if len(row) >= 2:
                    key_str = row[0].strip()  # value to hash (column 1)
                    payload = row[1].strip()  # associated value (column 2)
                    if key_str and payload:
                        if hash_table.hasKey(key_str):
                            # Duplicate key: overwrite payload and count it
                            hash_table.put(key_str, payload)
                            duplicate_count += 1
                        else:
                            hash_table.put(key_str, payload)
                            loaded_count += 1
    
    except Exception as e:
        print(f"Error reading file: {e}")
        return False
    
    print(f"Unique names loaded: {loaded_count}")
    print(f"Duplicate names found: {duplicate_count}")    
    return True

def save_hash_table_to_csv(hash_table, output_filename):    
    try:
        with open(output_filename, 'w', newline='', encoding='utf-8') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(['Key', 'Value'])
            
            for key, value in hash_table.items():
                csv_writer.writerow([key, value])
            
            return True
        
    except Exception as e:
        print(f"Error saving file: {e}")
        return False

def main():
    # Create hash table
    print("Creating hash table...")
    hash_table = DSAHashTable(capacity=1000, probing_mode="linear")
    hash_table.set_debug(True)
    
    # Load names from CSV
    csv_filename = "RandomNames7000.csv"
    if not load_names_from_csv(csv_filename, hash_table):
        print("Failed to load CSV file")
        return
    
    # Save hash table to CSV
    output_filename = "hash_table_output.csv"
    if save_hash_table_to_csv(hash_table, output_filename):
        print(f"\nHash table successfully saved to {output_filename}")
    
    # Test some lookups by key (column 1 values)
    test_keys = ["14495655", "14224671", "14431660", "14492026"]
    for k in test_keys:
        if hash_table.hasKey(k):
            print(f"Found key '{k}': {hash_table.get(k)}")
        else:
            print(f"Key '{k}' not found in hash table")

if __name__ == "__main__":
    main()
