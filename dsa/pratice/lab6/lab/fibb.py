def fibb(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibb(n-1) + fibb(n-2)

def print_fib_series(n):
    print("Fibonacci series:")
    for i in range(n):
        print(fibb(i), end=" ")

# Example: print first 10 Fibonacci numbers
print_fib_series(10)
