#!/usr/bin/python3

import sys
import queue
import heapq

# Maximum allowed edge length
maxlen = 2 * 10 ** 6


class DistPreprocessLarge:
    def __init__(self, n, adj, cost):
        # See description of these parameters in the starter for friend_suggestion
        self.n = n
        self.inf = float("inf")
        self.adj = adj
        self.cost = cost
        self.bidistance = [[self.inf] * n, [self.inf] * n]
        self.visited = [[False] * n, [False] * n]
        self.discovered = [set(), set()]
        self.closedset = set()
        self.contractedNeighbors = [0] * n
        # Levels of nodes for node ordering heuristics
        self.level = [0] * n
        # Positions of nodes in the node ordering
        self.rank = [0] * n

        # Implement preprocessing here
        self.preprocess()

    def preprocess(self):
        class PQNode:
            def __init__(self, priority, node):
                self.priority = priority
                self.node = node
                self.valid = True

            def __lt__(self, other):
                return self.priority < other.priority

        q = []
        qdict = dict()
        for v in range(self.n):
            sc = self.getShortcuts(v)
            ed = len(sc) - len(self.adj[0][v]) - len(self.adj[1][v])
            node = PQNode(ed, v)
            heapq.heappush(q, node)
            qdict[v] = node

        # contract nodes
        count = 1
        sc = []
        while q:
            current = heapq.heappop(q)
            if not current.valid or self.rank[current.node] > 0:
                continue
            validnode = current.node
            while True:
                v = current.node
                sc, nc = self.getShortcuts(v)
                current_ed = len(sc) - len(self.adj[0][v]) - len(self.adj[1][v]) + self.contractedNeighbors[v] + \
                             self.level[v] + nc
                current.priority = current_ed
                current = heapq.heappushpop(q, current)
                if validnode == current.node:
                    self.contractNode(v)
                    self.rank[v] = count
                    count += 1

                    # update neighbors
                    neighbors = set(self.adj[0][v])
                    neighbors.update(self.adj[1][v])
                    for w in neighbors:
                        self.level[w] = max(self.level[w], self.level[v] + 1)
                        self.contractedNeighbors[w] += 1

                    break
                validnode = current.node

    def add_arc(self, u, v, c):
        def update(adj, cost, u, v, c):
            for i in range(len(adj[u])):
                if adj[u][i] == v:
                    cost[u][i] = min(cost[u][i], c)
                    return
            adj[u].append(v)
            cost[u].append(c)

        update(self.adj[0], self.cost[0], u, v, c)
        update(self.adj[1], self.cost[1], v, u, c)

    def contractNode(self, v):
        shortcuts, _ = self.getShortcuts(v)
        for u, w, c in shortcuts:
            self.add_arc(u, w, c)

    def getShortcuts(self, v, max_hops=3):
        """ Create list of shortcuts if v is contracted and also
            counts already contracted neighbors
        """
        shortcuts = []  # store necessary shortcuts
        node_covered = set()

        # calculate distance upper bound for dijkstra search
        max_v_in = 0
        max_v_out = 0
        min_wp_in = self.inf
        for wi, w in enumerate(self.adj[0][v]):
            if self.rank[w] > 0:
                continue
            max_v_out = max(max_v_out, self.cost[0][v][wi])
            for wpi, wp in enumerate(self.adj[1][w]):
                if self.rank[wp] == 0 and wp != v:
                    min_wp_in = min(min_wp_in, self.cost[1][w][wpi])

        for wi, w in enumerate(self.adj[1][v]):
            if self.rank[w] > 0:
                continue
            max_v_in = max(max_v_in, self.cost[1][v][wi])

        max_dist = max_v_in + max_v_out - min_wp_in

        # dijkstra
        for si, s in enumerate(self.adj[1][v]):
            if self.rank[s] > 0 or s == v:
                continue

            q = []
            visited = dict()
            dist = dict()
            heapq.heappush(q, (0, s, 0))
            dist[s] = 0

            visited[v] = True

            while q:
                d, u, h = heapq.heappop(q)
                if d > max_dist:
                    break

                if u in visited or h + 1 > max_hops:
                    continue

                visited[u] = True
                for i, u_v in enumerate(self.adj[0][u]):
                    if self.rank[u_v] > 0 or u_v in visited:
                        continue
                    dist_u_v = dist[u] + self.cost[0][u][i]
                    if not u_v in dist or dist_u_v < dist[u_v]:
                        dist[u_v] = dist_u_v
                        heapq.heappush(q, (dist[u_v], u_v, h + 1))

            for ti, t in enumerate(self.adj[0][v]):
                if self.rank[t] > 0:
                    continue
                current_dist = self.cost[1][v][si] + self.cost[0][v][ti]
                if t in dist:
                    if dist[t] > current_dist:
                        shortcuts.append((s, t, current_dist))
                        node_covered.add(s)
                        node_covered.add(t)
                else:
                    shortcuts.append((s, t, current_dist))
                    node_covered.add(s)
                    node_covered.add(t)

        return shortcuts, len(node_covered)

    def mark_visited(self, x):
        if not self.visited[x]:
            self.visited[x] = True
            self.visited.append(x)

    # See description of this method in the starter for friend_suggestion
    def clear(self):
        for v in self.discovered[0]:
            self.bidistance[0][v] = self.inf
            self.visited[0][v] = False

        for v in self.discovered[1]:
            self.bidistance[1][v] = self.inf
            self.visited[1][v] = False

        self.discovered = [set(), set()]

    def discover(self, q, side, u):
        for vi, v in enumerate(self.adj[side][u]):
            if self.rank[u] > self.rank[v] or self.visited[side][v]:
                continue
            v_dist = self.bidistance[side][u] + self.cost[side][u][vi]
            if self.bidistance[side][v] > v_dist:
                self.bidistance[side][v] = v_dist
                self.discovered[side].add(v)
                heapq.heappush(q, (v_dist, v))

    # Returns the distance from s to t in the graph
    def query(self, s, t):
        if s == t:
            return 0
        self.clear()
        q = [[], []]
        estimate = self.inf

        self.bidistance[0][s] = 0
        self.bidistance[1][t] = 0
        self.discovered[0].add(s)
        self.discovered[1].add(t)
        heapq.heappush(q[0], (0, s))
        heapq.heappush(q[1], (0, t))

        while q[1] or q[0]:
            if q[0]:
                df, uf = heapq.heappop(q[0])
                if not self.visited[0][uf]:
                    if df > estimate:
                        q[0].clear()
                    self.discover(q[0], 0, uf)
                    self.visited[0][uf] = True
                    if self.visited[1][uf]:
                        d_temp = self.bidistance[0][uf] + self.bidistance[1][uf]
                        if d_temp < estimate:
                            estimate = d_temp

            if q[1]:
                db, ub = heapq.heappop(q[1])
                if not self.visited[1][ub]:
                    if db > estimate:
                        q[1].clear()
                    if ub == t and estimate > self.bidistance[0][ub]:
                        estimate = self.bidistance[0][ub]

                    self.discover(q[1], 1, ub)
                    self.visited[1][ub] = True
                    if self.visited[0][ub]:
                        d_temp = self.bidistance[0][ub] + self.bidistance[1][ub]
                        if d_temp < estimate:
                            estimate = d_temp

        return -1 if estimate == self.inf else estimate


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

    ch = DistPreprocessLarge(n, adj, cost)
    print("Ready")
    sys.stdout.flush()
    t, = readl()
    for i in range(t):
        s, t = readl()
        print(ch.query(s - 1, t - 1))