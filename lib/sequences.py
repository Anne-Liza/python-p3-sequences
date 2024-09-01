#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])
        return
    
    if length == 1:
        print([0])
        return
    
    if length == 2:
        print([0,1])
        return
    
    a, b = 0, 1
    fibonacci_sequence = [a]

    while b <= length:
       fibonacci_sequence.append(b)
       a, b = b, a + b
    
    print (fibonacci_sequence)

print_fibonacci(34)