# Uses python3

import sys


def is_greater_or_equal(digit, maxDigit):
    num1 = int(digit + maxDigit)
    num2 = int(maxDigit + digit)
    return num1 >= num2


def largest_number(a):
    res = ""
    while a:
        max_digit = '0'
        for digit in a:
            if is_greater_or_equal(digit, max_digit):
                max_digit = digit
        res += max_digit
        a.remove(max_digit)
    for x in a:
        res += x
    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
