# Uses python3
import sys


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def get_fibonacci_huge(n, m):
    el_mod_m, i = [0, 1], 2
    while not (el_mod_m[i - 2] == 0 and el_mod_m[i - 1] == 1) or i <= 2:
        el_mod_m.append((el_mod_m[i - 2] + el_mod_m[i - 1]) % m)
        i += 1
    return el_mod_m[n % (i - 2)]


if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
