def most_frequent_item_count(collection):
    if collection:
        count_dict = {n: collection.count(n) for n in set(collection)}
        n = max(count_dict.values())
        print(n)
        return n
    else:
        return 0
    


most_frequent_item_count([3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3])

# Best practice solution
def most_frequent_item_count(collection):
    if collection:
        return max([collection.count(item) for item in collection])
    return 0