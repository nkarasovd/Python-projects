# python3
import sys


def BWT(text):
    matrix = [text[i:] + text[:i] for i in range(len(text) - 1, -1, -1)]
    matrix.sort()

    bwt = ''
    for el in matrix:
        bwt += el[-1]

    return bwt


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))
