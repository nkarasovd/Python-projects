# Uses python3
import sys
import math


def clustering(x, y, n, k):
    return clustering_util(x, y, n, k)


class Node:
    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.parent = c
        self.rank = 0


class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight


def distance(x1, x2, y1, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def find(i, nodes):
    if i != nodes[i].parent:
        nodes[i].parent = find(nodes[i].parent, nodes)
    return nodes[i].parent


def union(u, v, nodes):
    p1 = find(u, nodes)
    p2 = find(v, nodes)
    if p1 != p2:
        if nodes[p1].rank > nodes[p2].rank:
            nodes[p2].parent = p1
        else:
            nodes[p1].parent = p2
            if nodes[p1].rank == nodes[p2].rank:
                nodes[p2].rank += 1


def clustering_util(x, y, n, k):
    nodes = []
    for i in range(n):
        nodes.append(Node(x[i], y[i], i))

    edges = [Edge(i, j, distance(x[i], x[j], y[i], y[j])) for i in range(n) for j in range(i + 1, n)]
    edges.sort(key=lambda x: x.weight)

    list_edge = []

    while edges:
        edge = edges.pop(0)
        u = edge.u
        v = edge.v
        if find(u, nodes) != find(v, nodes):
            list_edge.append(edge)
            union(u, v, nodes)

    return list_edge[len(list_edge) - k + 1].weight


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, n, k)))
