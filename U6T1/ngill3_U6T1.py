from typing import List, Any

"""
This file just has the algorithms. Open the tests file for where they're used.
"""


def linear_search(lst: List[int], item: int) -> bool:
    for i in lst:
        if i == item:
            return True
    return False


def binary_search(lst: List[int], item: int) -> bool:
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


def bubble_sort(lst: List[int]) -> List[int]:
    ret = lst.copy()
    for num in range(len(ret) - 1, 0, -1):
        for i in range(num):
            if ret[i] > ret[i + 1]:
                foo = ret[i]
                ret[i] = ret[i + 1]
                ret[i + 1] = foo
    return ret


def insertion_sort(lst: List[int]) -> List[int]:
    ret = lst.copy()
    for i in range(1, len(ret)):
        item = ret[i]
        j = i - 1
        while item < ret[j] and j >= 0:
            ret[j + 1] = ret[j]
            j -= 1
        ret[j + 1] = item
    return ret


def quick_sort(lst: List[int]) -> List[int]:
    below, equal, above = [], [], []
    if len(lst) > 1:
        pivot = lst[0]
        for x in lst:
            if x < pivot: below.append(x)
            elif x == pivot: equal.append(x)
            else: above.append(x)
        return quick_sort(below) + equal + quick_sort(above)
    else: return lst


if __name__ == "__main__":
    print("Don't run this file directly! Run the other one instead!")