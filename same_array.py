def same(arr_a, arr_b):
    if len(arr_a) != len(arr_b):
        return False

    sorted_arr_a = [sorted(pair) for pair in arr_a]
    sorted_arr_b = [sorted(pair) for pair in arr_b]

    set_arr1 = set(tuple(pair) for pair in sorted_arr_a)
    set_arr2 = set(tuple(pair) for pair in sorted_arr_b)

    return set_arr1 == set_arr2