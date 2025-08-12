import sys
import common
def fibonacci_recursive(n):
    if n < 0:
        raise ValueError("number cannot be negative")
    elif n == 0:
        return 0  # Base case: The 0th Fibonacci number is 0
    elif n == 1:
        return 1  # Base case: The 1st Fibonacci number is 1
    else:
        # Recursive step: Sum of the two preceding Fibonacci numbers
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fib (n):
    if n < 0:
        raise ValueError("number cannot be negative")
    if n == 0:
        return 0
    else:
        x = 0
        y = 1
        for i in range(1,n):
            z = (x + y)
            x = y
            y = z
        return y

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
