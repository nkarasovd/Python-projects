# Uses python3

import sys
import queue


def distance(adj, cost, s, t):
    # write your code here
    dist = [-1] * len(adj)
    bfs(adj, cost, s, dist)
    return dist[t]


def bfs(adj, cost, s, dist):
    dist[s] = 0
    q = queue.PriorityQueue()
    q.put((dist[s], s))
    while q.qsize() > 0:
        u = q.get()[1]
        for id, el in enumerate(adj[u]):
            if dist[el] == -1 or dist[el] > dist[u] + cost[u][id]:
                dist[el] = dist[u] + cost[u][id]
                q.put((dist[el], el))


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
