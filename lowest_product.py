def lowest_product(num):
    if len(num) >= 4:
        min_value = 99999999
        for i in range(0, len(num)-3):
            substr = num[i:i+4]
            substr_int=  [int(s) for s in substr]
            product = 1
            for n in substr_int:
                product = product * n
    
            if product < min_value:
                min_value = product
                print(product)


lowest_product('123456789')