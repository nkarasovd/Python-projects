# Uses python3
import sys
import math
import queue


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


def minimum_distance(x, y, n):
    nodes = []
    for i in range(n):
        nodes.append(Node(x[i], y[i], i))
    result = 0.
    edges = [Edge(i, j, distance(x[i], x[j], y[i], y[j])) for i in range(n) for j in range(i + 1, n)]
    edges.sort(key=lambda x: x.weight)
    while edges:
        edge = edges.pop(0)
        u = edge.u
        v = edge.v
        if find(u, nodes) != find(v, nodes):
            result += edge.weight
            union(u, v, nodes)

    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y, n)))
