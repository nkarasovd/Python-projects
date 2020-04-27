# python3
import sys

NA = -1


class Node:
    def __init__(self):
        self.next = {'A': NA, 'C': NA, 'G': NA, 'T': NA}
        self.leaf = True


def construct_trie(patterns):
    trie = [Node()]
    max = 0
    for pattern in patterns:
        current_node = 0
        for current_symbol in pattern:
            if trie[current_node].next[current_symbol] != NA:
                current_node = trie[current_node].next[current_symbol]
            else:
                trie.append(Node())
                trie[current_node].next[current_symbol] = max + 1
                trie[current_node].leaf = False
                max += 1
                current_node = max

    return trie


def trie_matching(text, trie):
    v = i = 0

    while i < len(text) + 1:
        symbol = text[min(i, len(text) - 1)]
        if trie[v].leaf:
            return True
        elif trie[v].next[symbol] != NA:
            v = trie[v].next[symbol]
            i += 1
        else:
            return False
    return False


def solve(text, n, patterns):
    trie = construct_trie(patterns)
    result = []
    for i in range(len(text)):
        if trie_matching(text[i:], trie):
            result.append(i)

    return result


text = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
patterns = []
for i in range(n):
    patterns += [sys.stdin.readline().strip()]

ans = solve(text, n, patterns)

sys.stdout.write(' '.join(map(str, ans)) + '\n')
