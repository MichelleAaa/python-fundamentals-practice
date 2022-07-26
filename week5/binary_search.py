def binary_search(the_list, target):
    lower_bound = 0
    upper_bound = len(the_list) - 1

    while lower_bound <= upper_bound:
        # The pivot value is between the upper and lower bounds. // means only the integer remains with floor division. (not the decimals)
        pivot = (lower_bound + upper_bound) // 2
        pivot_value = the_list[pivot]

# if the pivot value equals the target value
        if pivot_value == target:
            return pivot
            # if pivot is greater than the target, then we can discard the upper half of the search interval. We do this by changing the upper bound's value to the search's pivot minus one, which removes the upper half, so next time the upper bound is the previous pivot -1
        if pivot_value > target:
            upper_bound = pivot - 1
        else:
            # This would be when the pivot value is less than the target, then we set the lower bound to pivot plus one, raising the lower bound of the search interval for the next round.
            lower_bound = pivot + 1
# this causes the search range to be cut each time, as the upper or lower bounds shift.

# this means no index was found matching a value.
    return -1

test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(test_list, 10))
print(binary_search(test_list, 4))
print(binary_search(test_list, 33))