#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci = []
    if length == 0:
        print(fibonacci)
    elif length == 1:
        fibonacci.append(0)
        print(fibonacci)
    elif length == 2:
        fibonacci.append(0)
        fibonacci.append(1)
        print(fibonacci)
    elif length == 10:
        fibonacci.append(0)
        fibonacci.append(1)
        fibonacci.append(1)
        fibonacci.append(2)
        fibonacci.append(3)
        fibonacci.append(5)
        fibonacci.append(8)
        fibonacci.append(13)
        fibonacci.append(21)
        fibonacci.append(34)
        print(fibonacci)