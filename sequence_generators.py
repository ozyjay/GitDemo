# implementation of the Fibonacci sequence

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)
