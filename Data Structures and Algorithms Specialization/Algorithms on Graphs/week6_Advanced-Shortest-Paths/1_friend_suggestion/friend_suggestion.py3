#!/usr/bin/python3

import sys
import queue


class DijkstraOnedirectional:
    def __init__(self, n, m, adj, cost, _x=None, _y=None):
        self.n = n  # Number of nodes
        self.m = m
        self.adj = adj
        self.cost = cost
        self.inf = n * 10 ** 6  # All distances in the graph are smaller
        self.dist = [self.inf] * n  # Initialize distances for forward and backward searches
        self.visited = [False] * n  # visited[v] == True iff v was visited by forward or backward search
        self.workset = []  # All the nodes visited by forward or backward search
        self.parent = [None] * n  # Used for backtracking

    def clear(self):
        """
        Reinitialize the data structures for the next query after the previous query.
        """
        for v in self.workset:
            self.dist[v] = self.inf
            self.visited[v] = False
        self.workset = []
        self.parent = [None] * n

    def query(self, source, target):
        if source == target:
            return 0

        self.clear()
        q = queue.PriorityQueue()

        self.dist[source] = 0
        q.put((0, source))

        while not q.empty():
            _, u = q.get()
            self.visit(q, u)

        if self.dist[target] != self.inf:
            return self.dist[target]

        return -1

    def visit(self, q, u):
        """
        Try to relax the distance to node u from direction side by value dist.
        """
        neighbors = self.adj[0][u]
        for v_index, v in enumerate(neighbors):
            alt = self.dist[u] + self.cost[0][u][v_index]

            if alt < self.dist[v]:
                self.dist[v] = alt
                self.parent[v] = u
                self.workset.append(v)
                q.put((alt, v))

        self.workset.append(u)
        self.visited[u] = True

    def backtrack(self, source, target):
        path = []

        current = target
        while current != source:
            path.append(current)
            current = self.parent[current]
        path.append(current)
        path.reverse()

        return self.dist[target], path


# -----------------------------------------------------------------------------


class BiDij:
    def __init__(self, n, m, adj, cost):
        self.n = n  # Number of nodes
        self.m = m  # Number of edges
        self.adj = adj
        self.cost = cost
        self.inf = n * 10 ** 6  # All distances in the graph are smaller
        self.d = [[self.inf] * n, [self.inf] * n]  # Initialize distances for forward and backward searches
        self.visited = [[False] * n, [False] * n]  # visited[v] == True iff v was visited by forward or backward search
        self.workset = []  # All the nodes visited by forward or backward search
        self.parent = [[None] * n, [None] * n]  # Used for backtracking

    def clear(self):
        """Reinitialize the data structures for the next query after the previous query."""
        for v in self.workset:
            self.d[0][v] = self.d[1][v] = self.inf
            self.visited[0][v] = self.visited[1][v] = False
        self.workset = []

    def visit(self, q, side, u):
        """Try to relax the distance to node u from direction side by value dist."""
        neighbors = self.adj[side][u]

        for v_index, v in enumerate(neighbors):
            alt = self.d[side][u] + self.cost[side][u][v_index]

            if alt < self.d[side][v]:
                self.d[side][v] = alt
                self.parent[side][v] = u
                q[side].put((alt, v))
                self.workset.append(v)

        self.visited[side][u] = True
        self.workset.append(u)

    def do_iteration(self, q, side):
        if q[side].empty():
            return None
        _, u = q[side].get()

        self.visit(q, side, u)

        other_side = 1 - side
        if self.visited[other_side][u]:
            return self.calculate_dist()

        return None

    def calculate_dist(self):
        """Find the distance between nodes."""
        dist = self.inf

        for u in self.workset:
            candidate_dist = self.d[0][u] + self.d[1][u]
            if candidate_dist < dist:
                dist = candidate_dist
        return dist

    def backtrack(self, source, target):
        """Restoring the path from node source to node target."""
        u_best = -1
        dist = self.inf

        for u in self.workset:
            candidate_dist = self.d[0][u] + self.d[1][u]
            if candidate_dist < dist:
                u_best = u
                dist = candidate_dist

        path = []
        last = u_best

        while last != source:
            path.append(last)
            last = self.parent[0][last]
        path.append(last)
        path.reverse()

        last = u_best
        while last != target:
            last = self.parent[1][last]
            path.append(last)
        print(' '.join(map(lambda x: str(x + 1), path)))

    def query(self, s, t):
        if s == t:
            return 0
        self.clear()
        q = [queue.PriorityQueue(), queue.PriorityQueue()]
        self.d[0][s] = self.d[1][t] = 0

        q[0].put((0, s))
        q[1].put((0, t))

        while not q[0].empty() or not q[1].empty():
            dist = self.do_iteration(q, 0)
            if dist is not None:
                return dist

            dist = self.do_iteration(q, 1)
            if dist is not None:
                return dist

        return -1


def readl():
    return map(int, sys.stdin.readline().split())


if __name__ == '__main__':
    n, m = readl()
    adj = [[[] for _ in range(n)], [[] for _ in range(n)]]
    cost = [[[] for _ in range(n)], [[] for _ in range(n)]]
    for e in range(m):
        u, v, c = readl()
        adj[0][u - 1].append(v - 1)
        cost[0][u - 1].append(c)
        adj[1][v - 1].append(u - 1)
        cost[1][v - 1].append(c)
    t, = readl()
    bidij = BiDij(n, m, adj, cost)
    for i in range(t):
        s, t = readl()
        print(bidij.query(s - 1, t - 1))
