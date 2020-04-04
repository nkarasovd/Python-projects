# Uses python3
import sys


def fibonacci_sum(n):
    if n <= 1:
        return n

    el_mod_10, i = [0, 1], 2

    while not (el_mod_10[i-1] == 1 and el_mod_10[i-2] == 0) or i <= 2:
        el_mod_10.append((el_mod_10[i-1] + el_mod_10[i-2]) % 10)
        i += 1

    if n <= i:
        return (sum(el_mod_10[:n % (i - 2) + 1])) % 10
    else:
        k = n // (i - 2)
        return (sum(el_mod_10[:n % (i - 2) + 1]) + k * sum(el_mod_10[:i-1])) % 10


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum(n))
