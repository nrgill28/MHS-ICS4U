from U6T1.ngill3_U6T1 import linear_search, binary_search, bubble_sort, insertion_sort, quick_sort

"""
In this file I define a bunch of tests for the algorithms along with the correct answer.
When you run it, the only output should be "All tests completed!", or it will error out if one of the tests is wrong.
"""

# Input, Item, Output
search_tests = [
    ([1, 3, 7, 9, 11, 15], 5, False),
    ([1, 3, 7, 9, 11, 15], 3, True),
    ([1, 3, 7, 9, 11, 15], 15, True),
    ([1, 3, 7, 9, 11, 15], 900, False),
]

# Input, Output
sort_tests = [
    ([1, 7, 5, 2, 3, 10], [1, 2, 3, 5, 7, 10]),
    ([-1, 100, 5, 9, 15, 20], [-1, 5, 9, 15, 20, 100]),
]

# Test linear search
for test in search_tests:
    result = linear_search(test[0], test[1])
    assert result == test[2]

# Test binary search
for test in search_tests:
    result = binary_search(test[0], test[1])
    assert result == test[2]

# Test bubble sort
for test in sort_tests:
    assert bubble_sort(test[0]) == test[1]

# Test insertion sort
for test in sort_tests:
    assert insertion_sort(test[0]) == test[1]

# Test quick sort
for test in sort_tests:
    assert quick_sort(test[0]) == test[1]

print("All tests completed!")
