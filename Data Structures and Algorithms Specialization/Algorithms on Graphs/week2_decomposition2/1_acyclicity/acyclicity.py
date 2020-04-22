# Uses python3

import sys


def acyclic(adj):
    clr = [0 for _ in range(len(adj))]

    for i in range(len(adj)):
        if dfs(adj, clr, i):
            break
    if cycle_st == -1:
        return 0
    return 1


def dfs(adj, clr, v):
    global cycle_st
    clr[v] = 1
    for el in adj[v]:
        if clr[el] == 0:
            if dfs(adj, clr, el):
                return True
        elif clr[el] == 1:
            cycle_st = el
            return True
    clr[v] = 2
    return False


if __name__ == '__main__':
    cycle_st = -1
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
