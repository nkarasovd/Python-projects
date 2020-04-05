# Uses python3
import sys


def binary_search(a, left, right, x):
    if left > right:
        return -1
    m = left + (right - left) // 2
    if x == a[m]:
        return m
    if x < a[m]:
        return binary_search(a, left, m - 1, x)
    else:
        return binary_search(a, m + 1, right, x)


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, 0, len(a) - 1, x), end=' ')
        # print(linear_search(a, x), end=' ')
