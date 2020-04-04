# Uses python3
import sys


def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10


def fibonacci_partial_sum(from_, to):
    el_mod_10, i = [0, 1], 2

    while not (el_mod_10[i - 1] == 1 and el_mod_10[i - 2] == 0) or i <= 2:
        el_mod_10.append((el_mod_10[i - 1] + el_mod_10[i - 2]) % 10)
        i += 1

    if to <= i - 2:
        return (sum(el_mod_10[from_: to + 1])) % 10
    else:
        k = (to - from_) // (i - 2)
        new_to = to % (i - 2) + 1
        new_from_ = from_ % (i - 2)
        return (sum(el_mod_10[new_from_: i - 1]) + (k-1) * sum(el_mod_10[:i - 1]) + sum(el_mod_10[:new_to])) % 10


if __name__ == '__main__':
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))
