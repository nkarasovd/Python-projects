# Uses python3
import sys


def get_majority_element(a, left, right):
    el_dict = dict()
    for el in a:
        if el_dict.get(el) is None:
            el_dict[el] = 1
        else:
            el_dict[el] += 1
        if el_dict[el] > right // 2:
            return 1
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))

    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
