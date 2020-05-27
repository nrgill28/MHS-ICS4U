from typing import List, Any, Callable

try:
    from U5T3.ngill3_utils import pp_table
except ModuleNotFoundError:
    import sys
    print("This file depends on 'U5T3.ngill3_utils.py'!"
          " Try downloading the entire repo from https://github.com/nrgill28/MHS-ICS4U/"
          " and run this file from there instead.")
    sys.exit(0)

"""
This file just has the algorithms. Open the tests file for where they're used.
"""


# Extremely simple linear search algorithm. I don't think anything needs to be explained here.
def linear_search(lst: List[Any], item: Any) -> bool:
    for i in lst:
        if i == item:
            return True
    return False


# Binary search algorithm. This requires the list to be sorted in advance, but is generally quicker than linear search
def binary_search(lst: List[int], item: int) -> bool:
    sorted(lst)
    start, end = 0, len(lst) - 1
    while start <= end:
        pivot = (start + end) // 2
        i = lst[pivot]
        if i < item:
            start += 1
        elif i > item:
            end -= 1
        else:
            return True
    return False


# Bubble sort algorithm
def bubble_sort(lst: List[Any], sort_method: Callable[[Any], int] = lambda x: x, print_passes: bool = False) -> List[Any]:
    # Make a copy of the list, and a new list to hold the data at the beginning of each pass
    ret = lst.copy()
    passes = []

    # Run the algorithm
    for num in range(len(ret) - 1, 0, -1):
        passes.append(ret.copy())
        for i in range(num):
            if sort_method(ret[i]) > sort_method(ret[i + 1]):
                foo = ret[i]
                ret[i] = ret[i + 1]
                ret[i + 1] = foo

    # Once the algorithm is finished, add the last pass to the list and print it if we wanted
    passes.append(ret.copy())
    if print_passes: display_passes(passes)

    # return the sorted list
    return ret


def insertion_sort(lst: List[Any], sort_method: Callable[[Any], int] = lambda x: x, print_passes: bool = False) -> List[Any]:
    # Make a copy of the list, and a new list to hold the data at the beginning of each pass
    ret = lst.copy()
    passes = []

    # Run the algorithm
    for i in range(1, len(ret)):
        passes.append(ret.copy())
        item = ret[i]
        j = i - 1
        while j >= 0 and sort_method(item) < sort_method(ret[j]):
            ret[j + 1] = ret[j]
            j -= 1
        ret[j + 1] = item

    # Once the algorithm is finished, add the last pass to the list and print it if we wanted
    passes.append(ret.copy())
    if print_passes: display_passes(passes)

    # Return the sorted list
    return ret


# Quicksort algorithm
def quick_sort(lst: List[int], sort_method: Callable[[Any], int] = lambda x: x) -> List[Any]:
    below, equal, above = [], [], []
    if len(lst) > 1:
        pivot = sort_method(lst[0])
        for x in lst:
            cmp = sort_method(x)
            if cmp < pivot: below.append(x)
            elif cmp == pivot: equal.append(x)
            else: above.append(x)
        return quick_sort(below, sort_method) + equal + quick_sort(above, sort_method)
    else: return lst


# This method is called if you wanted to display the state of each pass when sorting with Insertion or Bubble sort.
# Basically it takes in a list of lists and prints it using my pp_table function that pretty prints a table.
def display_passes(pass_list: List[List]):
    headers = [f"Index {i}" for i in range(len(pass_list[0]))]
    headers.insert(0, "Pass")
    for i, row in enumerate(pass_list):
        pass_list[i] = [str(x) for x in row]
        pass_list[i].insert(0, str(i))
    pass_list.insert(0, headers)
    pp_table(pass_list)


# Running this file directly does nothing.
if __name__ == "__main__":
    print("Don't run this file directly! Run the other one instead!")
