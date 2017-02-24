def fib(n):
    n1, n2 = 0, 1

    while n1 < n:
        print(n1)
        n1, n2 = n2, n1 + n2

fib(1000)
