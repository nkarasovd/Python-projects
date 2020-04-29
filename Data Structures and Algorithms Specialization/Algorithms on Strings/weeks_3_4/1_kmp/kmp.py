# python3
import sys


def compute_prefix_function(p):
    s, border = [0], 0
    for i in range(1, len(p)):
        while border > 0 and p[i] != p[border]:
            border = s[border - 1]
        if p[i] == p[border]:
            border += 1
        else:
            border = 0
        s.append(border)
    return s


def find_pattern(pattern, text):
    """
    Find all the occurrences of the pattern in the text
    and return a list of all positions in the text
    where the pattern starts in the text.
    """
    s = pattern + '$' + text

    result_util = compute_prefix_function(s)
    len_p = len(pattern)

    result = [i - 2 * len_p for i in range(len_p + 1, len(s)) if result_util[i] == len_p]

    return result


if __name__ == '__main__':
    pattern = sys.stdin.readline().strip()
    text = sys.stdin.readline().strip()
    result = find_pattern(pattern, text)
    print(" ".join(map(str, result)))
