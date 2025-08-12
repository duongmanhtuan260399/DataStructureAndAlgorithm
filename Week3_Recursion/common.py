import timeit
import sys
import matplotlib.pyplot as plt

def measure_time(func, *args, **kwargs):
    start = timeit.default_timer()
    func(*args, **kwargs)
    end = timeit.default_timer()
    return end - start

def compare_functions(func1, func2, func1_label, func2_label, n_values):
    times1 = []
    times2 = []

    for n in n_values:
        try:
            times1.append(measure_time(func1, n))
        except RecursionError:
            times1.append(None)  # mark failure for func1

        try:
            times2.append(measure_time(func2, n))
        except RecursionError:
            times2.append(None)  # mark failure for func2

    plt.figure(figsize=(8, 5))
    plt.plot(n_values, times1, marker='o', label=func1_label)
    plt.plot(n_values, times2, marker='o', label=func2_label)
    plt.xlabel('n')
    plt.ylabel('Time (seconds)')
    plt.title(f'Performance Comparison: {func1_label} vs {func2_label}')
    plt.legend()
    plt.grid(True)
    plt.show()
