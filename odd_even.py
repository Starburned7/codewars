def odd_or_even(arr):
    if sum(arr) % 2 == 0:
         print(sum(arr) % 2)
         return "even" 
    else:
         print(sum(arr) % 2)
         return "odd"
    
odd_or_even([1,2,3])

# Solution
def oddOrEven(arr):
    return 'even' if sum(arr) % 2 == 0 else 'odd'