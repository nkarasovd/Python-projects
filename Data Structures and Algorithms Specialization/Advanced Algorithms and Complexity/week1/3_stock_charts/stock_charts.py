# python3
import queue


class StockCharts:
    @staticmethod
    def read_data():
        n, k = map(int, input().split())
        stock_data = [list(map(int, input().split())) for _ in range(n)]
        return stock_data

    @staticmethod
    def write_response(result):
        print(result)

    @staticmethod
    def min_charts(stock_data):
        n = len(stock_data)
        adj = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if all([x < y for x, y in zip(stock_data[i], stock_data[j])]):
                    adj[i][j] = 1
        matching = [-1] * n
        busy_right = [False] * n

        def bfs():
            # Source: 1
            # Left: 2
            # Right: 3
            # Sink: 4
            visited_nodes = set()
            q = queue.Queue()
            q.put((1, None))
            visited_nodes.add((1, None))
            path = []
            parent = dict()
            while not q.empty():
                curr_node = q.get()
                if 1 == curr_node[0]:  # Source
                    for i in range(n):
                        if -1 == matching[i]:
                            visited_nodes.add((2, i))
                            parent[(2, i)] = curr_node
                            q.put((2, i))
                elif 2 == curr_node[0]:  # Left
                    i = curr_node[1]
                    for j in range(n):
                        if 1 == adj[i][j] and j != matching[i] and not (3, j) in visited_nodes:
                            visited_nodes.add((3, j))
                            parent[(3, j)] = curr_node
                            q.put((3, j))
                elif 3 == curr_node[0]:
                    j = curr_node[1]
                    if not busy_right[j]:
                        prev_node = curr_node
                        curr_node = (4, j)
                        while True:
                            path.insert(0, (prev_node, curr_node))
                            if 1 == prev_node[0]:
                                break
                            curr_node = prev_node
                            prev_node = parent[curr_node]
                        for e in path:
                            if 2 == e[0][0]:
                                matching[e[0][1]] = e[1][1]
                            elif 3 == e[0][0] and 4 == e[1][0]:
                                busy_right[e[1][1]] = True
                        return True  # There is a path
                    else:
                        for i in range(n):
                            if j == matching[i] and not (2, i) in visited_nodes:
                                visited_nodes.add((2, i))
                                parent[(2, i)] = curr_node
                                q.put((2, i))
            return False  # There isn't a path

        while bfs():
            continue
        return len([0 for i in matching if -1 == i])

    def solve(self):
        stock_data = self.read_data()
        result = self.min_charts(stock_data)
        self.write_response(result)


if __name__ == '__main__':
    stock_charts = StockCharts()
    stock_charts.solve()
