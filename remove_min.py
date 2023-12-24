def remove_smallest(numbers):
    #return []
    #lowest_num = min(numbers)
    lowest_index = numbers.index(min(numbers))
    numbers_copy = numbers.copy()
    numbers_copy.pop(lowest_index)
    print(numbers_copy)
    #return numbers_copy


remove_smallest([1,4,6,0])

# Solution
def remove_smallest(numbers):
    #return []
    if numbers:
        lowest_index = numbers.index(min(numbers))
        numbers_copy = numbers.copy()
        numbers_copy.pop(lowest_index)
        return numbers_copy
    else:
        return numbers