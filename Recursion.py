# The function calls itself called recursion

# input a number
n = int(input("Enter the number: "))

# Function
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
    return fib(n-1)

print(fib(n))