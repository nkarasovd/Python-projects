# Uses python3
from sys import stdin


def fibonacci_sum_squares(n):
    if n <= 1:
        return n

    el_mod_10, i = [0, 1], 2
    while not (el_mod_10[i - 2] == 0 and el_mod_10[i - 1] == 1) or i <= 2:
        el_mod_10.append((el_mod_10[i - 2] + el_mod_10[i - 1]) % 10)
        i += 1
    return (el_mod_10[n % (i - 2)] * (el_mod_10[n % (i - 2)] + el_mod_10[n % (i - 2) - 1])) % 10


if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares(n))
