# Imports
from statistics import mean

from U5T3.ngill3_utils import pp_table
from U6T1.ngill3_U6T1 import bubble_sort, insertion_sort, quick_sort, linear_search, binary_search
import random
from datetime import datetime

# The min and max for values in a list
MIN_VALUE = -1000
MAX_VALUE = 1000

# The min and max for the number of values in each list
MIN_AMOUNT = 2
MAX_AMOUNT = 100

# The number of iterations to do.
# Iterations is the number of tests, batch size is how many times the same test is repeated.
# This is so it can be averaged.
ITERATIONS = 100
BATCH_SIZE = 100


def stopwatch(what):
    start = datetime.now()
    for i in range(BATCH_SIZE): what()
    end = datetime.now()
    return (end - start).total_seconds() / BATCH_SIZE


bench_start = datetime.now()

# Generate some test data
print("Generating test data...")
data = [
    [[random.randint(MIN_VALUE, MAX_VALUE) for _ in range(random.randint(MIN_AMOUNT, MAX_AMOUNT))],
     random.randint(MIN_VALUE, MAX_VALUE)]
    for _ in range(ITERATIONS)
]

# Test linear search
print("Testing linear search...")
linear_times = [stopwatch(lambda: linear_search(test[0], test[1])) for test in data]

# Test binary search
print("Testing binary search...")
binary_times = [stopwatch(lambda: binary_search(test[0], test[1])) for test in data]

# Test bubble sort
print("Testing bubble sort...")
bubble_times = [stopwatch(lambda: bubble_sort(test[0])) for test in data]

# Test insertion sort
print("Testing insertion sort...")
insertion_times = [stopwatch(lambda: insertion_sort(test[0])) for test in data]

# Test quick sort
print("Testing quick sort...")
quick_times = [stopwatch(lambda: quick_sort(test[0])) for test in data]

bench_end = datetime.now()

# Now that we're done testing, we can now display the data.
algo_times = {"Linear Search": linear_times, "Binary Search": binary_times, "Bubble Sort": bubble_times,
              "Insertion Sort": insertion_times, "Quick Sort": quick_times}
table_data = [
    [algo, ITERATIONS * BATCH_SIZE, sum(times) * 1000, (sum(times) / ITERATIONS) * 1000000]
    for algo, times in algo_times.items()
]
table_data.insert(0, ["Algorithm", "Iterations", "Total Time", "Avg Time Per Iteration"])
formatting = [None, None, "%.2f ms", "%.0f μs"]
pp_table(table_data, formatting)
print(f"Total time: {(bench_end - bench_start).total_seconds():.3f} s")
