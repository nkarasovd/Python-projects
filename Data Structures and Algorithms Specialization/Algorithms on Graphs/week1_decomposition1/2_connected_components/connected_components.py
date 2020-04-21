# Uses python3

import sys


def number_of_components(adj):
    cc = 0
    visited = []
    for id, el in enumerate(adj):
        if id not in visited:
            explore(adj, id, visited, cc)
            cc += 1
    return cc


def explore(adj, x, visited, cc):
    visited.append(x)
    for el in adj[x]:
        if el not in visited:
            explore(adj, el, visited, cc)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
