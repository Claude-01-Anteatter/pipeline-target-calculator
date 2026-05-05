def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b

def power(a, b):
    # bug: using multiplication instead of exponentiation
    return a * b

def is_even(n):
    # bug: off-by-one, returns True for odd numbers
    return n % 2 == 1
