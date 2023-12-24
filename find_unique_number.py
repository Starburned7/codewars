l = [ 1, 1, 1, 2, 1, 1 ]
t = [[x, l.count(x)] for x in set(l)]
print(t)

d = {x: l.count(x) for x in set(l)}
print(d)
val = min(d, key=d.get)
print(val)

# Solution
def find_uniq(arr):
    # your code here
    count_dict = {n: arr.count(n) for n in set(arr)}
    n = min(count_dict, key = count_dict.get)
    return n   # n: unique number in the array

# Best practice solution
def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b
