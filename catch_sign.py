def catch_sign_change(lst):
    lst_str = "".join(str(n) for n in lst)
   
    print(lst_str)
    print(lst_str.count('-'))
    return lst_str.count('-')


catch_sign_change([-7,-7,7,0])