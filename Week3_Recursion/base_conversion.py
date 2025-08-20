import timeit
import sys
import matplotlib.pyplot as plt
import common


def decimal_to_base_recursive(n, base):
    if base < 2 or base > 16:
        raise ValueError("Base must be between 2 and 16")

    digits = "0123456789ABCDEF"

    if n < 0:
        # Handles negative numbers
        result = "-" + decimal_to_base_recursive(abs(n), base)
    elif n < base:
        # Base case for the recursion
        result = digits[n]
    else:
        # Recursive step
        result = decimal_to_base_recursive(n // base, base) + digits[n % base]

    return result


def decimal_to_base_iterative(n, base):
    if base < 2 or base > 16:
        raise ValueError("Base must be between 2 and 16")

    # Handle the n == 0 edge case separately
    if n == 0:
        final_string = "0"
    else:
        # Proceed with conversion for non-zero numbers
        is_negative = n < 0
        if is_negative:
            n = abs(n)

        digits = "0123456789ABCDEF"
        converted_string = ""

        while n > 0:
            remainder = n % base
            converted_string = digits[remainder] + converted_string
            n = n // base

        # Use a ternary to add the sign if necessary
        final_string = "-" + converted_string if is_negative else converted_string

    return final_string


def run_comparison():
    while True:
        try:
            base = int(input("Enter base (2-16) for performance comparison: "))
            if 2 <= base <= 16:
                break
            print("Base must be between 2 and 16.")
        except ValueError:
            print("Invalid base. Please enter an integer between 2 and 16.")

    n_values = list(range(500, 10000, 500))

    # Use the common helper function to compare and plot the performance.
    common.compare_functions(
        func1=lambda n: decimal_to_base_recursive(n, base),
        func2=lambda n: decimal_to_base_iterative(n, base),
        func1_label=f"Recursive Base-{base} Conversion",
        func2_label=f"Iterative Base-{base} Conversion",
        n_values=n_values
    )


def run_single():
    try:
        base = int(input("Enter base (2-16): "))
        if base < 2 or base > 16:
            print("Base must be between 2 and 16.")
            return run_single()
        a = int(input("Enter a number: "))
        print(f"Recursive Base-{base} Conversion: {decimal_to_base_recursive(a, base)}")
        print(f"Iterative Base-{base} Conversion: {decimal_to_base_iterative(a, base)}")
    except ValueError:
        print("Invalid input")
        run_single()


if __name__ == "__main__":
    # It's good practice to have a recursion limit for larger numbers,
    # though it may not be strictly necessary for the chosen range.
    sys.setrecursionlimit(10000)
    run_single()

