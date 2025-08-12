import timeit
import sys
import matplotlib.pyplot as plt
import common


def decimal_to_hex_recursive(n):
    if n < 0:
        return "-" + decimal_to_hex_recursive(abs(n))
    if n < 16:
        return "0123456789ABCDEF"[n]
    else:
        return decimal_to_hex_recursive(n // 16) + "0123456789ABCDEF"[n % 16]


def decimal_to_hex_iterative(n):
    if n == 0:
        return "0"

    is_negative = n < 0
    if is_negative:
        n = abs(n)

    hex_chars = "0123456789ABCDEF"
    hex_string = ""

    while n > 0:
        remainder = n % 16
        hex_string = hex_chars[remainder] + hex_string
        n = n // 16

    if is_negative:
        return "-" + hex_string
    return hex_string

def run_comparison():
    n_values = list(range(500, 10000, 500))

    # Use the common helper function to compare and plot the performance.
    common.compare_functions(
        func1=decimal_to_hex_recursive,
        func2=decimal_to_hex_iterative,
        func1_label="Recursive Hex Conversion",
        func2_label="Iterative Hex Conversion",
        n_values=n_values
    )

def run_single():
    try:
        a = int(input("Enter a number: "))
        print(f"Recrusive Hex Conversion: {decimal_to_hex_recursive(a)}")
        print(f"Iterative Hex Conversion: {decimal_to_hex_iterative(a)}")
    except ValueError:
        print("Invalid input")
        run_single()


if __name__ == "__main__":
    # It's good practice to have a recursion limit for larger numbers,
    # though it may not be strictly necessary for the chosen range.
    sys.setrecursionlimit(10000)
    run_single()

