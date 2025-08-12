import timeit
import sys
import matplotlib.pyplot as plt
import common

def factorial_recursive(n):
    if n<0:
        raise ValueError("number cannot be negative")
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    if n<0:
        raise ValueError("number cannot be negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def run_comparison():
    n_values = list(range(100, 2000, 200))
    common.compare_functions(factorial_recursive, factorial_iterative,
                             "Recursive Factorial", "Iterative Factorial",
                             n_values)

def run_single():
    try:
        n = int(input("Type a number: "))
        print("Factorial Recursive:", factorial_recursive(n))
        print("Factorial Iterative:", factorial_iterative(n))
        return
    except ValueError:
        print("Invalid input")
        run_single()


if __name__ == "__main__":
    # Increase recursion and integer digit limits for large n
    sys.setrecursionlimit(10000)
    sys.set_int_max_str_digits(100000)

    run_single()

