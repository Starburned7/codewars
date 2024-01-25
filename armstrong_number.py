def narcissistic( value ):
    value_list = []
    value_list.append(str(value))
    values_str = " ".join(value_list)
    degree = len(values_str)
    values = []
    for v in values_str:
        values.append(int(v) ** degree)
    if sum(values) == value:
        return True
    else: 
        return False
 
def narcissistic(value):
    value_str = str(value)
    degree = len(value_str)
    total = sum(int(digit) ** degree for digit in value_str)
    return total == value

def narcissistic( value ):
    values_str = str(value)
    degree = len(values_str)
    values = []
    for v in values_str:
        values.append(int(v) ** degree)
    return sum(values) == value
      
  

    

narcissistic(153)