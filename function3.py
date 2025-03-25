

def longest_subsequence(array: list[int]) -> list[int]:  # This function is recursive
    """
    Some examples

    >>> longest_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80])
    [10, 22, 33, 41, 60, 80]
    >>> longest_subsequence([4, 8, 7, 5, 1, 12, 2, 3, 9])
    [1, 2, 3, 9]
    >>> longest_subsequence([28, 26, 12, 23, 35, 39])
    [12, 23, 35, 39]
    >>> longest_subsequence([9, 8, 7, 6, 5, 7])
    [5, 7]
    >>> longest_subsequence([1, 1, 1])
    [1, 1, 1]
    >>> longest_subsequence([])
    []
    """

    '''
    Preconditions
    '''
    assert(isinstance(array,list)), "The input must be a array list"
    assert(all(isinstance(x,int) for x in array)), "Every element in the array must be an int"

    array_length = len(array)
    # If the array contains only one element, we return it (it's the stop condition of
    # recursion)
    if array_length <= 1:
        return array
        # Else
    pivot = array[0]
    is_found = False
    i = 1
    longest_subseq: list[int] = []
    while not is_found and i < array_length:
        '''
        Loop variants
        '''
        assert(all(array[k]>=pivot) for k in range(1,i) ), "Loop Variant: Element before i should be greater than pivot until smaller one is found"

        if array[i] < pivot:
            is_found = True
            temp_array = array[i:]
            temp_array = longest_subsequence(temp_array)

            '''
            Loop Variant
            '''
            assert(all(temp_array[j]<= temp_array[j+1]) for j in range(len(temp_array)-1)), "Loop Variant: The subsequence must be non-decreasing"

            if len(temp_array) > len(longest_subseq):
                longest_subseq = temp_array
        else:
            i += 1

    temp_array = [element for element in array[1:] if element >= pivot]
    temp_array = [pivot, *longest_subsequence(temp_array)]
    if len(temp_array) > len(longest_subseq):
        '''
        Postcondition
        '''
        assert all(temp_array[j] <= temp_array[j+1] for j in range(len(temp_array) - 1)), "Postcondition: returned subsequence must be non-decreasing"
        return temp_array
    else:
        '''
        Postcondition
        '''
        assert all(longest_subseq[j] <= longest_subseq[j+1] for j in range(len(longest_subseq) - 1)), "Postcondition: returned subsequence must be non-decreasing"
        return longest_subseq


if __name__ == "__main__":
    # Exercise the function with a few test cases
    print(longest_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80]))
    print(longest_subsequence([4, 8, 7, 5, 1, 12, 2, 3, 9]))
    print(longest_subsequence([28, 26, 12, 23, 35, 39]))
    print(longest_subsequence([9, 8, 7, 6, 5, 7]))
    print(longest_subsequence([1, 1, 1]))
    print(longest_subsequence([]))
