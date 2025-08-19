def towers_of_hanoi(n, source, destination, middle, level=1):
    """
    Solves the Towers of Hanoi problem and returns the total number of moves.
    """
    # Set the indentation based on the current recursion level.
    indent = "    " * (level - 1)

    # The base case for the recursion: moving 1 disk is 1 move.
    if n == 1:
        print(f"{indent}Recursion Level={level}")
        print(f"{indent}Moving Disk 1 from {source} to {destination}")
        print(f"{indent}n=1, src={source}, dest={destination}")
        return 1

    total_moves = 0

    # 1. Move n-1 disks from the source to the middle.
    total_moves += towers_of_hanoi(n - 1, source, middle, destination, level + 1)

    # 2. Move the nth (largest) disk from the source to the destination rod.
    print(f"{indent}Recursion Level={level}")
    print(f"{indent}Moving Disk {n} from {source} to {destination}")
    print(f"{indent}n={n}, src={source}, dest={destination}")
    total_moves += 1

    # 3. Move the n-1 disks from the middle rod to the destination rod.
    total_moves += towers_of_hanoi(n - 1, middle, destination, source, level + 1)

    # Return the accumulated moves for this level and its children.
    return total_moves


# --- Driver Code ---
if __name__ == "__main__":
    # Set the number of disks and the names for the rods.
    num_disks = 3
    source_peg = '1'
    destination_peg = '3'
    middle_peg = '2'

    # Initial call to the function, which now returns the total moves.
    move_count = towers_of_hanoi(num_disks, source_peg, destination_peg, middle_peg)

    # Print the final count using the variable.
    print(f"... # There are {move_count} moves for this problem.")