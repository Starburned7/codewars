# def solve(a,b):
#     if len(a) > len(b):
#         a_counts = {n: a.count(n) for n in set(a)}
#         b_counts = {n: b.count(n) for n in set(b)}
#         diff = dict(set(a_counts.items()) - set(b_counts.items()))
#         result = sum(diff.values())
#         print(diff)
#         print(result)
        
#     return 0

# def solve(a, b):
#     if len(a) > len(b):
#         a_counts = {n: a.count(n) for n in set(a)}
#         b_counts = {n: b.count(n) for n in set(b)}
        
#         # Consider all characters in both strings
#         all_chars = set(a) | set(b)
        
#         # Compare the counts for each character and calculate the absolute difference
#         diff = {key: abs(a_counts.get(key, 0) - b_counts.get(key, 0)) for key in all_chars}
        
#         result = sum(diff.values())
#         #print(diff)
#         #print(result)
#         print(result)
#         return result

#     return 0


def solve(a, b):
    for n in set(b):
        if a.count(n) < b.count(n):
            return 0
    return len(a) - len(b)
#solve("fbd", "aabcdefg")
# solve("aabcdefg","fbd")
#solve("xyz","yxz")
solve("abdegfg","ffdb")
#solve("aabcdefg","fbd")
