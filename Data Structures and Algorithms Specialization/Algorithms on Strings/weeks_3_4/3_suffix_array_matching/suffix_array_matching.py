# python3
import sys


def sort_characters(s, n):
    my_map = {'$': 0, 'A': 1, 'C': 2, 'G': 3, 'T': 4}
    order = [0 for _ in range(n)]
    count = [0 for _ in range(alphabet)]
    for el in s:
        count[my_map[el]] += 1
    for i in range(1, alphabet):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        count[my_map[s[i]]] -= 1
        order[count[my_map[s[i]]]] = i

    return order


def compute_char_classes(text, order, n):
    char_class = [0 for _ in range(n)]
    # char_class[order[0]] = 0
    for i in range(1, n):
        if text[order[i]] != text[order[i - 1]]:
            char_class[order[i]] = char_class[order[i - 1]] + 1
        else:
            char_class[order[i]] = char_class[order[i - 1]]

    return char_class


def sort_doubled(L, order, char_class, n):
    count = [0 for _ in range(n)]
    new_order = [0 for _ in range(n)]
    for i in range(n):
        count[char_class[i]] = count[char_class[i]] + 1

    for j in range(1, n):
        count[j] = count[j] + count[j - 1]

    for i in range(n - 1, -1, -1):
        start = (order[i] - L + n) % n

        cl = char_class[start]
        count[cl] = count[cl] - 1
        new_order[count[cl]] = start

    return new_order


def update_classes(new_order, char_class, L):
    n = len(new_order)
    new_class = [0 for _ in range(n)]
    new_class[new_order[0]] = 0
    for i in range(1, n):
        cur = new_order[i]
        prev = new_order[i - 1]
        mid = cur + L
        mid_prev = (prev + L) % n
        if char_class[cur] != char_class[prev] or char_class[mid] != char_class[mid_prev]:
            new_class[cur] = new_class[prev] + 1
        else:
            new_class[cur] = new_class[prev]

    return new_class


def build_suffix_array(text):
    """
    Build suffix array of the string text and
    return a list result of the same length as the text
    such that the value result[i] is the index (0-based)
    in text where the i-th lexicographically smallest
    suffix of text starts.
    """
    n = len(text)
    order = sort_characters(text, n)

    char_class = compute_char_classes(text, order, n)

    L = 1
    while L < n:
        order = sort_doubled(L, order, char_class, n)
        char_class = update_classes(order, char_class, L)
        L = 2 * L

    return order


def find_occurrences(text, patterns, suffix_array):
    result = []
    n = len(text)

    for pattern in patterns:
        start = 0
        end = n
        while start < end:
            mid = (start + end) // 2
            suffix = text[suffix_array[mid]: int(min(suffix_array[mid] + len(pattern), n))]
            if pattern > suffix:
                start = mid + 1
            else:
                end = mid

        begin = start
        end = n
        while start < end:
            mid = (start + end) // 2
            suffix = text[suffix_array[mid]: int(min(suffix_array[mid] + len(pattern), n))]
            if pattern < suffix:
                end = mid
            else:
                start = mid + 1

        finish = end
        if begin <= finish:
            for i in range(begin, finish):
                result.append(suffix_array[i])

    return set(result)


if __name__ == '__main__':
    alphabet = 5
    text = sys.stdin.readline().strip()
    text += '$'
    pattern_count = int(sys.stdin.readline().strip())
    patterns = sys.stdin.readline().strip().split()
    suffix_array = build_suffix_array(text)
    occs = find_occurrences(text, patterns, suffix_array)
    print(" ".join(map(str, occs)))
