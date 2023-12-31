def find_added(st1, st2):
    arr1 = list(st1)
    arr2 = list(st2)
    for i in arr1:
        if i in arr2:
            arr2.remove(i)
    result = ''.join(sorted(arr2))
    print(result)
    return result

find_added('4455446', '447555446666')

#     return ''.join(sorted( [i * (st2.count(i) - st1.count(i)) for i in set(st2)] ))
