# Uses python3
import sys


def merge_sort(a):
    global num_inversions
    n = len(a)
    if n == 1:
        return a
    m = n // 2
    b = merge_sort(a[:m])
    c = merge_sort(a[m:])
    a_, count = merge(b, c)
    num_inversions += count
    return a_


def merge(b, c):
    d = []
    count = 0
    count_b = 0
    while b and c:
        b0 = b[0]
        c0 = c[0]
        if b0 <= c0:
            d.append(b0)
            b.remove(b0)
            count_b += 1
            count += len(d) - count_b
        else:
            d.append(c0)
            c.remove(c0)
    count += len(b) * (len(d) - count_b)
    d += b + c

    return d, count


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    num_inversions = 0
    # print(*merge_sort(a))
    merge_sort(a)
    print(num_inversions)
