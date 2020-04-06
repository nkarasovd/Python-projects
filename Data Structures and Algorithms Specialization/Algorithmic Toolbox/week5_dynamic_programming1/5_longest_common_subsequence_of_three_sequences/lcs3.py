# Uses python3

import sys


def lcs3(a, b, c):
    d = [[[0] * (cn + 1) for _ in range(bn + 1)] for _ in range(an + 1)]

    for i in range(1, an + 1):
        for j in range(1, bn + 1):
            for k in range(1, cn + 1):

                if a[i - 1] == b[j - 1] and b[j - 1] == c[k - 1]:
                    d[i][j][k] = d[i - 1][j - 1][k - 1] + 1
                else:
                    d[i][j][k] = max(d[i - 1][j][k], d[i][j - 1][k], d[i][j][k - 1])
    return d[an][bn][cn]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
