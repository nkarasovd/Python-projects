# Uses python3
import sys


def get_change(m):
    c_10 = m // 10
    c_5 = (m - c_10 * 10) // 5
    c_1 = (m - c_10 * 10 - c_5 * 5)
    return c_1 + c_5 + c_10


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
