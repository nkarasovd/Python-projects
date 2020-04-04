# Uses python3
def calc_fib(n):
    if n <= 1:
        return n
    fib1 = 0
    fib2 = 1
    for _ in range(n):
        fib1, fib2 = fib2, fib1 + fib2
    return fib1


n = int(input())
print(calc_fib(n))
