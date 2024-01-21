def variance(numbers): 
    # your code here
    mean = sum(numbers) / len(numbers)
    variance = sum([(n - mean) **2 for n in numbers]) / len(numbers)
    print(variance)
    return variance
    
    
variance([-10, 0, 10, 20, 30])