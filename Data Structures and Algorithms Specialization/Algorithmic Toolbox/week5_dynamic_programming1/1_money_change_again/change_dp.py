# Uses python3
import sys


def get_change(m):
    change = [0]
    for i in range(1, m + 1):
        change1 = sys.maxsize
        change3 = sys.maxsize
        change4 = sys.maxsize

        if i - 1 >= 0:
            change1 = change[i - 1] + 1
        if i - 3 >= 0:
            change3 = change[i - 3] + 1
        if i - 4 >= 0:
            change4 = change[i - 4] + 1

        change.append(min([change1, change3, change4]))

    return change[m]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
