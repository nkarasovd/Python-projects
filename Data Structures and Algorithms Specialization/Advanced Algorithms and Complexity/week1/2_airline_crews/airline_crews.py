# python3
import queue
import sys


class Edge:
    def __init__(self, from_, to, capacity):
        self.from_ = from_
        self.to = to
        self.capacity = capacity
        self.flow = 0


class FlowGraph:
    def __init__(self, n):
        self.edges = []
        self.graph = [[] for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        forward_edge = Edge(from_, to, capacity)

        backward_edge = Edge(to, from_, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id_):
        return self.edges[id_]

    def add_flow(self, id_, flow):
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id_].flow += flow
        self.edges[id_ ^ 1].flow -= flow


class MaxMatching:
    @staticmethod
    def read_data():
        n, m = map(int, input().split())
        adj_matrix = [list(map(int, input().split())) for _ in range(n)]
        return adj_matrix

    @staticmethod
    def write_response(matching):
        line = [str(-1 if x == -1 else x + 1) for x in matching]
        print(' '.join(line))

    @staticmethod
    def build_graph(bipartite_graph):
        num_flights = len(bipartite_graph)

        num_crews = len(bipartite_graph[0])

        # indexes of source and sink vertices

        from_ = 0

        to = 1 + num_flights + num_crews

        graph = FlowGraph(1 + num_flights + num_crews + 1)
        #
        # add edges out of source vertex
        for i in range(num_flights + 1):
            graph.add_edge(from_, i, _capacity_)

        # add edges to sink vertex
        for i in range(num_flights + 1, num_flights + num_crews + 1):
            graph.add_edge(i, to, _capacity_)

        # add edges defined in the adjacency matrix
        for i in range(num_flights):
            for j in range(num_crews):
                if bipartite_graph[i][j]:
                    graph.add_edge(i + 1, j + 1 + num_flights, _capacity_)

        return graph

    @staticmethod
    def get_path(graph, from_, to):
        # инициализировать результат (обратная последовательность ребер для перехода от «from» в «to»)
        result = []

        # инициализировать массив посещенных узлов
        visited = []
        # initialize the map of parent nodes
        parents = dict()

        # инициализировать очередь узлов
        q = queue.Queue()
        q.put(from_)

        is_path_found = False

        # начать обход графа
        while not q.empty():
            # получить первый узел в очереди
            u = q.get()

            # получить узлы, смежные с первым узлом в очереди
            u_adj = graph.get_ids(u)

            # для каждого узла v, смежного с u...
            for v in u_adj:
                v_edge = graph.get_edge(v)
                residual_flow = v_edge.capacity - v_edge.flow
                if residual_flow > 0 and v_edge.to not in visited:
                    q.put(v_edge.to)
                    visited.append(v_edge.to)
                    parents[v_edge.to] = v
                    # можем остановаиться, если путь найден
                    if v_edge.to == to:
                        is_path_found = True
                        break

            # можем остановаиться, если путь найден
            if is_path_found:
                break
        if to in visited:
            # построить путь как обратную последовательность ребер
            while to != from_:
                tmp_start = parents.get(to)
                result.append(tmp_start)
                e = graph.get_edge(tmp_start)
                to = e.from_

        return result

    def find_matching(self, adj_matrix):
        # Replace this code with an algorithm that finds the maximum
        # matching correctly in all cases.
        num_flights = len(adj_matrix)
        num_crews = len(adj_matrix[0])
        graph = self.build_graph(adj_matrix)

        matching = [-1] * num_flights

        from_ = 0
        to = 1 + num_flights + num_crews

        path = self.get_path(graph, from_, to)

        # while there is a path...
        while len(path) > 0:
            # modify matching array to record the recently found path
            for i in range(1, len(path) - 1):
                edge_index = path[i]

                # only consider the forward edges
                if edge_index % 2 == 0:
                    e = graph.get_edge(edge_index)
                    matching[e.from_ - 1] = e.to - 1 - num_flights

            # calculate the min residual flow through the current path
            min_residual = sys.maxsize
            for id_edge in path:
                e = graph.get_edge(id_edge)

                residual = e.capacity - e.flow
                if min_residual > residual:
                    min_residual = residual
                    # we can break the cycle once we found
                    # the first minResidual, because it's always
                    # going to be equal to 1, and it doesn't
                    # make sense to try improving it further
                    break

            # update the graph with the min residual flow

            for id_edge in path:
                graph.add_flow(id_edge, min_residual)

            # recalculate the path
            path = self.get_path(graph, from_, to)

        return matching

    def solve(self):
        adj_matrix = self.read_data()
        matching = self.find_matching(adj_matrix)
        self.write_response(matching)


if __name__ == '__main__':
    _capacity_ = 1
    max_matching = MaxMatching()
    max_matching.solve()
