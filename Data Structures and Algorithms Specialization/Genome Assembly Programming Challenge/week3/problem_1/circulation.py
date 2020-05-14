# python3

import queue


class Edge:
    def __init__(self, u, v, lower_bound, capacity):
        self.u = u
        self.v = v
        self.lower_bound = lower_bound
        self.capacity = capacity
        self.diff = capacity - lower_bound
        self.flow = 0


class FlowGraph:

    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n + 2)]
        # The demand function
        self.dv = [0] * (n + 2)
        self.D = 0

    def add_edge(self, from_, to, lower_bound, capacity):
        forward_edge = Edge(from_, to, lower_bound, capacity)
        backward_edge = Edge(to, from_, 0, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)
        self.dv[from_] += lower_bound
        self.dv[to] -= lower_bound

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow
        self.edges[id].diff -= flow
        self.edges[id ^ 1].diff += flow


class CirculationProblem:
    def __init__(self):
        graph, n, m = self._input()
        flow, flows = self.find_circulation(graph, n, m)
        self.print_result(flow, flows)

    @staticmethod
    def _input():
        vertex_count, edge_count = map(int, input().split())
        graph = FlowGraph(vertex_count)
        for _ in range(edge_count):
            u, v, lower_bound, capacity = map(int, input().split())
            graph.add_edge(u - 1, v - 1, lower_bound, capacity)

        # update source and sink
        for v in range(vertex_count):
            if graph.dv[v] < 0:
                graph.add_edge(vertex_count, v, 0, -graph.dv[v])
            if graph.dv[v] > 0:
                graph.add_edge(v, vertex_count + 1, 0, graph.dv[v])
                graph.D += graph.dv[v]

        return graph, vertex_count, edge_count

    @staticmethod
    def bfs(graph, from_, to):
        x = float('inf')
        has_path = False
        n = graph.size()
        dist = [float('inf')] * n
        path = []
        parent = [(None, None)] * n
        q = queue.Queue()
        dist[from_] = 0
        q.put(from_)
        while not q.empty():
            currFromNode = q.get()
            for id in graph.get_ids(currFromNode):
                currEdge = graph.get_edge(id)
                if float('inf') == dist[currEdge.v] and currEdge.diff > 0:
                    dist[currEdge.v] = dist[currFromNode] + 1
                    parent[currEdge.v] = (currFromNode, id)
                    q.put(currEdge.v)
                    if currEdge.v == to:
                        while True:
                            path.insert(0, id)
                            currX = graph.get_edge(id).diff
                            x = min(currX, x)
                            if currFromNode == from_:
                                break
                            currFromNode, id = parent[currFromNode]
                        has_path = True
                        return has_path, path, x
        return has_path, path, x

    def max_flow(self, graph, from_, to):
        flow = 0
        while True:
            has_path, path, x = self.bfs(graph, from_, to)
            if not has_path:
                return flow
            for id in path:
                graph.add_flow(id, x)
            flow += x

    def find_circulation(self, graph, n, m):
        flow = self.max_flow(graph, n, n + 1)

        flows = [0] * m
        if flow != graph.D:
            return False, flows
        else:
            for i in range(m):
                currForwardEdge = graph.edges[i * 2]
                flows[i] = currForwardEdge.flow + currForwardEdge.lower_bound
            return True, flows

    @staticmethod
    def print_result(flow, flows):
        if not flow:
            print('NO')
        else:
            print('YES')
            print('\n'.join(map(str, flows)))


if __name__ == "__main__":
    CirculationProblem()
