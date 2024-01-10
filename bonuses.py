# How much should each employee receive? 
# John thinks A should receive $230, B $276, C $345 since 230 * 18 = 276 * 15 = 345 * 12 and 230 + 276 + 345 = 851.

def bonus(arr, s):
    sum_of_inverted_values = sum(1 / x for x in arr)
    multiplier = s / sum_of_inverted_values
    bonuses = [round(multiplier / x) for x in arr]
    return bonuses

bonus([22, 3, 15], 18228)   