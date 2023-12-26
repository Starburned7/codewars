def distances_from_average(test_list):
    average_value = sum(test_list) / len(test_list)
    print([round(average_value-n,2) for n in test_list])
    return [round(average_value-n,2) for n in test_list]


distances_from_average([55, 95, 62, 36, 48])