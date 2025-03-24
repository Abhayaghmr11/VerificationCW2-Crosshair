# This function is sourced from https://github.com/TheAlgorithms/Python/blob/master/greedy_methods/smallest_range.py
# Only changes are made to the docstring
# Contracts are added where applicable

from heapq import heappop, heappush
from sys import maxsize


def smallest_range(nums: list[list[int]]) -> list[int]:
    '''
    pre: len(nums) > 0
    pre: len(L) > 0
    pre: all(all(L[i] <= L[i+1] for i in range(len(L)-1)) for L in nums)
    post: len(__return__) == 0    
    post: __return__[0] <= __return__[1]
    '''

    assert(len(nums)>0), "Precondition: The size of the list must be greater than 1"
    assert all(len(L) > 0 for L in nums), "Precondition: No sublist may be empty."
    assert(all(all(L[i] <= L[i+1] for i in range(len(L)-1)) for L in nums)), "Precondition: Each sublist must be sorted"

    min_heap: list[tuple[int, int, int]] = []
    current_max = -maxsize - 1

    for i, items in enumerate(nums):
        heappush(min_heap, (items[0], i, 0))
        current_max = max(current_max, items[0])

    # Initialize smallest_range with large integer values
    smallest_range = [-maxsize - 1, maxsize]

    while min_heap:
        assert all(len(nums[i]) > 0 for _, i, _ in min_heap), "Invariant: No list in the heap is empty."
        assert all(current_max >= element[0] for element in min_heap), "Invariant: current_max ≥ all elements in heap."            

        current_min, list_index, element_index = heappop(min_heap)

        if current_max - current_min < smallest_range[1] - smallest_range[0]:
            smallest_range = [current_min, current_max]

        if element_index == len(nums[list_index]) - 1:
            break

        next_element = nums[list_index][element_index + 1]
        heappush(min_heap, (next_element, list_index, element_index + 1))
        current_max = max(current_max, next_element)

    assert(len(smallest_range) == 2), "Postcondition: The result should only contain two values"
    assert(smallest_range[0] <= smallest_range[1]), "Postcondition: The return list must be sorted"
    return smallest_range