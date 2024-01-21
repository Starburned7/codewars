def range_function(*args):
    start, step, stop = 1, 1, None
    if len(args) == 1:
        stop = args[0]
    elif len(args) == 2:
        start = args[0]
        stop = args[1]
    elif len(args) == 3:
        start, step, stop = args[0], args[1], args[2]
        
    value = start
    while value <= stop:
        yield value
        value += step