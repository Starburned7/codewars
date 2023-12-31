def stickyCalc(operation, val1, val2):
    # Combine val1 and val2 into a single number
    sticky_result = int(str(val1) + str(val2))

    # Perform the specified operation
    if operation == '+':
        result = sticky_result + val2
    elif operation == '-':
        result = sticky_result - val2
    elif operation == '*':
        result = sticky_result * val2
    elif operation == '/':
        result = sticky_result / val2
    else:
        return "Invalid operation"

    # Return the formatted output
    return f"({sticky_result} {operation} {val2}) = {result}"
