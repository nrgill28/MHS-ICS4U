# Imports
from statistics import mean

from U5T3.ngill3_utils import pp_table
from U6T1.ngill3_U6T1 import bubble_sort, insertion_sort, quick_sort
import random
from datetime import datetime

# The min and max for values in a list
MIN_VALUE = -1000
MAX_VALUE = 1000

# The min and max for the number of values in each list
MIN_AMOUNT = 2
MAX_AMOUNT = 100

# The number of iterations to do
ITERATIONS = 1000

# Generate some test data
print("Generating test data...")
data = [
    [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(random.randint(MIN_AMOUNT, MAX_AMOUNT))]
    for _ in range(ITERATIONS)
]

# Test bubble sort
print("Testing bubble sort...")
bubble_times = []
for test in data:
    bubble_start = datetime.now()
    bubble_sort(test)
    bubble_end = datetime.now()
    bubble_times.append((bubble_end - bubble_start).total_seconds())

# Test insertion sort
print("Testing insertion sort...")
insertion_times = []
for test in data:
    insertion_start = datetime.now()
    insertion_sort(test)
    insertion_end = datetime.now()
    insertion_times.append((insertion_end - insertion_start).total_seconds())

# Test quick sort
print("Testing quick sort...")
quick_times = []
for test in data:
    quick_start = datetime.now()
    quick_sort(test)
    quick_end = datetime.now()
    quick_times.append((quick_end - quick_start).total_seconds())


# Now that we're done testing, we can now display the data.
table_data = [
    ["Sort Method", "Iterations", "Total Time", "Avg Time Per Iteration"],
    ["Bubble Sort", ITERATIONS, sum(bubble_times) * 1000, (sum(bubble_times) / ITERATIONS) * 1000 * 1000],
    ["Insertion Sort", ITERATIONS, sum(insertion_times) * 1000, (sum(insertion_times) / ITERATIONS) * 1000 * 1000],
    ["Quick Sort", ITERATIONS, sum(quick_times) * 1000, (sum(quick_times) / ITERATIONS) * 1000 * 1000],
]
formatting = [None, None, "%.2f ms", "%.0f μs"]
pp_table(table_data, formatting)
