def print_fibonacci(length):
    fib_sequence = []
    
    if length >= 1:
        fib_sequence.append(0)
    if length >= 2:
        fib_sequence.append(1)
    
    while len(fib_sequence) < length:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    
    print(fib_sequence)

