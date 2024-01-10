def find_it(seq):
    count_dict = {x: seq.count(x) for x in set(seq)}
    print(count_dict)
    
    for x in count_dict.keys():
        if count_dict[x] % 2 != 0:
            print(x)
            return x


find_it([1,2,2,3,3,3,4,3,3,3,2,2,1])


# Solution for sequences with small number of elements
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i