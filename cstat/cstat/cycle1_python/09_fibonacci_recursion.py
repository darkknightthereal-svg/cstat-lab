def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


n = int(input("Enter n: "))
print("The", n, "th Fibonacci number is", fib(n))
