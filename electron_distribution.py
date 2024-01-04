def atomic_number(electrons):
    distribution_list = []
    shell_number = 1
    
    while electrons > 0:
        max_number = 2 * (shell_number ** 2)
        
        if max_number <= electrons:
            distribution_list.append(max_number)
            electrons -= max_number
        else:
            distribution_list.append(electrons)
            break
         
        
        shell_number +=1
    
    return distribution_list
