import sys
import common


def fibonacci_recursive(n):
    if n < 0:
        raise ValueError("number cannot be negative")
    return n if n <= 1 else fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fib(n):
    if n < 0:
        raise ValueError("number cannot be negative")

    # Initialize the first two numbers in the sequence
    current, next_num = 0, 1

    # Loop n times to advance to the nth number
    for _ in range(n):
        current, next_num = next_num, current + next_num

    return current

def run_comparison():
    n_values = list(range(5, 35, 5))
    common.compare_functions(fibonacci_recursive, fib,
                             "Recursive Factorial", "Iterative Factorial",
                             n_values)

def run_single():
    try:
        n = int(input("Type a number: "))
        print("Factorial Recursive:", fibonacci_recursive(n))
        print("Factorial Iterative:", fib(n))
        return
    except ValueError as e:
        print(e)
        run_single()



if __name__ == '__main__':
    # Increase recursion and integer digit limits for large n
    sys.setrecursionlimit(10000)
    sys.set_int_max_str_digits(100000)
    run_single()
