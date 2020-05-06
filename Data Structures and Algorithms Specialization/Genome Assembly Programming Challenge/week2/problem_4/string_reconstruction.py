# python3

import sys


class EulerianPath:
    def __init__(self, adj):
        self.adj = adj
        self.n = len(self.adj)
        self.nUnEdges = 0  # number of unexplored edges
        self.nodesWUE = dict()  # key: node with unused edges; value: the position of such node in the current path
        self.in_deg = dict()
        self.out_deg = dict()
        self.adj_cur_pos = dict()
        self.path = []
        for w, v_list in self.adj.items():
            self.in_deg[w] = self.in_deg.get(w, 0)
            for v in v_list:
                self.in_deg[v] = self.in_deg.get(v, 0) + 1
            self.out_deg[w] = len(v_list)
            self.nUnEdges += len(v_list)
            self.adj_cur_pos[w] = 0

    def explore(self, s):
        self.path.append(s)
        cur_pos = self.adj_cur_pos[s]
        cur_max_pos = self.out_deg[s]
        while cur_pos < cur_max_pos:
            self.adj_cur_pos[s] = cur_pos + 1
            if cur_pos + 1 < cur_max_pos:
                self.nodesWUE[s] = len(self.path) - 1
            else:
                if s in self.nodesWUE:
                    del self.nodesWUE[s]
            v = self.adj[s][cur_pos]
            self.path.append(v)
            s = v
            cur_pos = self.adj_cur_pos[s]
            cur_max_pos = self.out_deg[s]
            self.nUnEdges -= 1

    def update_path(self, start_pos):
        l = len(self.path) - 1
        self.path = self.path[start_pos:l] + self.path[:start_pos]
        for node, pos in self.nodesWUE.items():
            if pos < start_pos:
                self.nodesWUE[node] = pos + l - start_pos
            else:
                self.nodesWUE[node] = pos - start_pos

    def calculate_eulerian_cycle(self):
        if type(self.adj) is dict:
            w, v_list = self.adj.popitem()
            self.adj[w] = v_list
            self.explore(w)
        else:
            self.explore(0)
        while self.nUnEdges > 0:
            node, pos = self.nodesWUE.popitem()
            self.update_path(pos)
            self.explore(node)
        return self.path


class StringReconstruction:
    def __init__(self):
        self.k, self.adj = self.read_data()
        self.path = EulerianPath(self.adj).calculate_eulerian_cycle()
        print(self.reconstruct_from_path(self.path)[:-self.k + 1])

    def read_data(self):
        data = list(sys.stdin.read().strip().split())
        adj = self.de_brujin(len(data[0]), data)
        return len(data[0]), adj

    @staticmethod
    def de_brujin(k, patterns):
        adj_db = dict()
        for p in patterns:
            if p[:k - 1] in adj_db:
                adj_db[p[:k - 1]].append(p[1:])
            else:
                adj_db[p[:k - 1]] = []
                adj_db[p[:k - 1]].append(p[1:])
            if p[1:] not in adj_db:
                adj_db[p[1:]] = []
        return adj_db

    @staticmethod
    def reconstruct_from_path(path):
        return path[0] + ''.join(seq[-1] for seq in path[1:])


if __name__ == "__main__":
    StringReconstruction()
