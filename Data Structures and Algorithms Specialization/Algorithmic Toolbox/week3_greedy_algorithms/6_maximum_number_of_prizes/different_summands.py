# Uses python3
import sys


def optimal_summands(n):
    summands = []
    i = 1
    while n > 0:
        if i > n:
            summands[-1] += n
            return summands
        summands.append(i)
        n -= i
        i += 1
    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
