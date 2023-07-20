#!/usr/bin/python3
def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fibonacci_seq = [0, 1]
    
    for i in range(2, n):
        next_number = fibonacci_seq[i - 1] + fibonacci_seq[i - 2]
        fibonacci_seq.append(next_number)
    return fibonacci_seq
