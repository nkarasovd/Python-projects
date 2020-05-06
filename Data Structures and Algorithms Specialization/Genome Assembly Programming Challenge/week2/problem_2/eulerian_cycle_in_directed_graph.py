# python3

import sys


class EulerianCycle:
    def __init__(self):
        # number of explored edges
        self.num_edges = 0
        # key: node with unused edges;
        # value: the position of such node in the current path
        self.nodes_w_u_e = dict()
        self.path = []
        is_balanced = self._input()
        if not is_balanced:
            print('0')
        else:
            print('1')
            self.calculate_eulerian_cycle()
            self.print_path()

    def _input(self):
        data = list(sys.stdin.read().strip().split())
        self.n, self.num_edges = int(data[0]), int(data[1])
        self.adj = [[] for _ in range(self.n)]
        self.unused_edges = [[] for _ in range(self.n)]
        self.out_deg = [0] * self.n
        self.in_deg = [0] * self.n
        self.adj_cur_pos = [0] * self.n

        for i in range(self.num_edges):
            cur_from = int(data[2 * i + 2]) - 1
            cur_to = int(data[2 * i + 3]) - 1
            self.adj[cur_from].append(cur_to)
            self.out_deg[cur_from] += 1
            self.in_deg[cur_to] += 1

        return all([self.out_deg[i] == self.in_deg[i] for i in range(self.n)])

    def explore(self, s):
        self.path.append(s)
        cur_pos = self.adj_cur_pos[s]
        cur_max_pos = self.out_deg[s]
        while cur_pos < cur_max_pos:
            self.adj_cur_pos[s] = cur_pos + 1
            if cur_pos + 1 < cur_max_pos:
                self.nodes_w_u_e[s] = len(self.path) - 1
            else:
                if s in self.nodes_w_u_e:
                    del self.nodes_w_u_e[s]
            v = self.adj[s][cur_pos]
            self.path.append(v)
            s = v
            cur_pos = self.adj_cur_pos[s]
            cur_max_pos = self.out_deg[s]
            self.num_edges -= 1

    def update_path(self, start_pos):
        l = len(self.path) - 1
        self.path = self.path[start_pos:l] + self.path[:start_pos]
        for node, pos in self.nodes_w_u_e.items():
            if pos < start_pos:
                self.nodes_w_u_e[node] = pos + l - start_pos
            else:
                self.nodes_w_u_e[node] = pos - start_pos

    def calculate_eulerian_cycle(self):
        self.explore(0)
        while self.num_edges > 0:
            node, pos = self.nodes_w_u_e.popitem()
            self.update_path(pos)
            self.explore(node)
        return self.path

    def print_path(self):
        print(' '.join([str(node + 1) for node in self.path[:-1]]))


if __name__ == "__main__":
    EulerianCycle()