def towers_of_hanoi_indented(n, source_rod, destination_rod, auxiliary_rod, level=1):
    # Set the indentation based on the current recursion level.
    indent = "    " * (level - 1)

    # The base case for the recursion
    if n == 1:
        print(f"{indent}Recursion Level={level}")
        print(f"{indent}Moving Disk 1 from Source {source_rod} to Destination {destination_rod}")
        print(f"{indent}n=1, src={source_rod}, dest={destination_rod}")
        return

    # 1. Move n-1 disks from the source to the auxiliary rod.
    # We increase the level for the recursive call.
    towers_of_hanoi_indented(n - 1, source_rod, auxiliary_rod, destination_rod, level + 1)

    # 2. Move the nth (largest) disk from the source to the destination rod.
    # This action happens at the current recursion level.
    print(f"{indent}Recursion Level={level}")
    print(f"{indent}Moving Disk {n} from Source {source_rod} to Destination {destination_rod}")
    print(f"{indent}n={n}, src={source_rod}, dest={destination_rod}")

    # 3. Move the n-1 disks from the auxiliary rod to the destination rod.
    # We increase the level again for this recursive call.
    towers_of_hanoi_indented(n - 1, auxiliary_rod, destination_rod, source_rod, level + 1)


# --- Driver Code ---
if __name__ == "__main__":
    # Set the number of disks and the names for the rods.
    # Using numbers as strings to match the sample output.
    num_disks = 4
    source_peg = '1'
    destination_peg = '3'
    auxiliary_peg = '2'

    # Initial call to the function starts at level 1.
    towers_of_hanoi_indented(num_disks, source_peg, destination_peg, auxiliary_peg)

    print("... # There are 7 moves for this problem.")