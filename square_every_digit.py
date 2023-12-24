def square_digits(num):
  num = str(num)
  #int_list = [int(n) for n in num]
  #square_list = [n** 2 for n in int_list]
  square_list = [(int(n)** 2) for n in num]
  print(square_list)
  result = int(''.join([str(n) for n in square_list]))
  print(result)

square_digits(765)

# Solution
def square_digits(num):
  square_list = [(int(n)** 2) for n in str(num)]
  result = int(''.join([str(n) for n in square_list]))
  return result