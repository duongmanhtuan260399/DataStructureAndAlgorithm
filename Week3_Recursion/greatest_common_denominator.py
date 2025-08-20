import sys
import timeit
import matplotlib.pyplot as plt
import random
from functools import partial


# Recursive GCD (Euclidean algorithm)
def gcd_recursive(a, b):
    if a<0 or b<0:
        raise ValueError('a and b must be non-negative')
    return a if b == 0 else gcd_recursive(b, a % b)


# Iterative GCD (Euclidean algorithm)
def gcd_iterative(a, b):
    if a<0 or b<0:
        raise ValueError('a and b must be non-negative')
    while b != 0:
        a, b = b, a % b
    return a


def measure_time(func, *args, **kwargs):
    start = timeit.default_timer()
    func(*args, **kwargs)
    end = timeit.default_timer()
    return end - start


def compare_gcd_functions(func1, func2, label1, label2, input_pairs):
    times1 = []
    times2 = []

    a_vals = [pair[0] for pair in input_pairs]
    b_vals = [pair[1] for pair in input_pairs]

    for a, b in input_pairs:
        times1.append(measure_time(func1, a, b))
        times2.append(measure_time(func2, a, b))

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(projection='3d')

    # Plot iterative results in blue
    ax.scatter(a_vals, b_vals, times1, c='blue', label=label1, alpha=0.7)

    # Plot recursive results in red
    ax.scatter(a_vals, b_vals, times2, c='red', label=label2, alpha=0.7)

    # Set labels and title
    ax.set_xlabel('Number a')
    ax.set_ylabel('Number b')
    ax.set_zlabel('Time (seconds)')
    ax.set_title('Comparison of GCD Computation Time')
    # Add a legend to tell the methods apart
    ax.legend()
    # To display the plot in an interactive window, you would use:
    plt.show()

def run_comparison():
    random.seed(42)
    input_pairs = [(random.randint(100, 10 ** 7), random.randint(100, 10 ** 7)) for _ in range(100)]
    compare_gcd_functions(gcd_recursive, gcd_iterative,
                          "Recursive GCD", "Iterative GCD",
                          input_pairs)

def run_single():
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
        print("Greatest Common Denominator Recursive: ", gcd_recursive(a, b))
        print("Greatest Common Denominator Iterative: ", gcd_iterative(a, b))
    except ValueError as e:
        print(e)
        run_single()



if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    run_single()