# Uses python3

import sys
import queue


def bipartite(adj):
    # write your code here
    q = queue.Queue()
    q.put(0)
    visited = [0] * len(adj)
    visited[0] = 1
    while q.qsize() > 0:
        u = q.get()
        for el in adj[u]:
            if visited[el] == 0:

                q.put(el)
                if visited[u] == 1:
                    visited[el] = 2
                else:
                    visited[el] = 1
            elif visited[el] == visited[u]:
                return 0
    return 1


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
    print(bipartite(adj))
