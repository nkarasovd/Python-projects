# Uses python3
import sys
import itertools


def partition3(souvenirs):
    total = sum(souvenirs)
    if total % 3 != 0:
        return 0

    size = total // 3
    table = [[False for _ in range(total + 1)] for _ in range(total + 1)]
    table[0][0] = True

    for i in range(len(souvenirs)):
        j = total
        while j >= 0:
            k = total
            while k >= 0:
                if table[j][k]:
                    table[j + souvenirs[i]][k] = True
                    table[j][k + souvenirs[i]] = True
                k -= 1
            j -= 1

    return int(table[size][size])


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))
