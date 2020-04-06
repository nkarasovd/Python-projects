# Uses python3
import sys


def optimal_sequence(n):
    # +1, *2, *3
    sequence = [0]

    for i in range(1, n + 1):
        prev_1 = sys.maxsize
        prev_3 = sys.maxsize
        prev_2 = sys.maxsize
        if i >= 1:
            prev_1 = sequence[i - 1] + 1
        if i % 3 == 0:
            prev_3 = sequence[i // 3] + 1
        if i % 2 == 0:
            prev_2 = sequence[i // 2] + 1

        sequence.append(min([prev_1, prev_3, prev_2]))

    solution = [n]

    while n != 1:
        prev_1 = sequence[n - 1]
        prev_3 = sys.maxsize
        prev_2 = sys.maxsize

        if n % 3 == 0:
            prev_3 = sequence[n // 3]
        if n % 2 == 0:
            prev_2 = sequence[n // 2]

        cur_min = min([prev_1, prev_3, prev_2])
        if cur_min == prev_1:
            n -= 1
            solution.append(n)
        elif cur_min == prev_3:
            n = n // 3
            solution.append(n)
        else:
            n = n // 2
            solution.append(n)

    return reversed(solution)


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    sequence = list(optimal_sequence(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')
