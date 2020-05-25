from typing import List, Any, Callable

"""
This file just has the algorithms. Open the tests file for where they're used.
"""


def linear_search(lst: List[Any], item: Any) -> bool:
    for i in lst:
        if i == item:
            return True
    return False


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


def bubble_sort(lst: List[Any], sort_method: Callable[[Any], int] = lambda x: x) -> List[Any]:
    ret = lst.copy()
    for num in range(len(ret) - 1, 0, -1):
        for i in range(num):
            if sort_method(ret[i]) > sort_method(ret[i + 1]):
                foo = ret[i]
                ret[i] = ret[i + 1]
                ret[i + 1] = foo
    return ret


def insertion_sort(lst: List[Any], sort_method: Callable[[Any], int] = lambda x: x) -> List[Any]:
    ret = lst.copy()
    for i in range(1, len(ret)):
        item = ret[i]
        j = i - 1
        while j >= 0 and sort_method(item) < sort_method(ret[j]):
            ret[j + 1] = ret[j]
            j -= 1
        ret[j + 1] = item
    return ret


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


if __name__ == "__main__":
    print("Don't run this file directly! Run the other one instead!")
