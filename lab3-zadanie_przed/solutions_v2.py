def fib(n):
    if (n == 1 or n == 2):
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fib_2(n):
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    else:
        return fib_2(n-1) + fib_2(n-2)


for i in range(22):
    print(f"{i:>2} {fib_2(i):>6}")
