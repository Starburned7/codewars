# def count_repeats(txt):
#     input_length = len(txt)
#     unique_elements_length = len(set(txt))
#     print(input_length)
#     print(unique_elements_length)
#     print(input_length -unique_elements_length)
#     return input_length -unique_elements_length 


def count_repeats(txt):
    string_length = len(txt)
    count = 0
    for i in range(1,len(txt)):
       if txt[i-1]==txt[i]:
          count+=1
    return count

count_repeats('abbbbc')
count_repeats('abbcca')
       
