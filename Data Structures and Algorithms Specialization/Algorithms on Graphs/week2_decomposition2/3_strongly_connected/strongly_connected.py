# Uses python3

import sys

sys.setrecursionlimit(200000)


def dfs1(adj, visited, order, v):
    visited[v] = True
    for el in adj[v]:
        if not visited[el]:
            dfs1(adj, visited, order, el)
    order.append(v)


def dfs2(adj, visited, v, component):
    visited[v] = True
    # component.append(v)
    for el in adj[v]:
        if not visited[el]:
            dfs2(adj, visited, el, component)


def number_of_strongly_connected_components(adj, adj_r):
    visited = [False] * len(adj)
    order = []
    for i in range(len(adj)):
        if not visited[i]:
            dfs1(adj, visited, order, i)

    visited = [False] * len(adj)
    scc = 0
    component = []
    for el in reversed(order):
        if not visited[el]:
            dfs2(adj_r, visited, el, component)
            # print(component)
            # component.clear()
            scc += 1

    return scc


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    adj_r = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj_r[b - 1].append(a - 1)
    print(number_of_strongly_connected_components(adj, adj_r))
