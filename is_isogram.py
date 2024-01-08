def is_isogram(word):
    if isinstance(word, str) and len(word) >= 1:
        word = ''.join(l.lower() for l in word if l.isalpha())
        word_dict = {l: word.count(l) for l in word}

        if word_dict:
            first_value = list(word_dict.values())[0]
            all_equal = all(value == first_value for value in word_dict.values())
            return all_equal

    return False


# def is_isogram(word):
#     word = word.lower()
#     word_dict = {l: word.count(l) for l in word}
#     print(word_dict)
#     first_value = list(word_dict.values())[0]
#     all_equal = all(value == first_value for value in word_dict.values())
#     print(all_equal)
#     return all_equal
   


#is_isogram("isogram")
is_isogram("moOse")