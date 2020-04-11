# python3

import sys
import threading


class Node:
    def __init__(self, label, parent):
        self.root = True if parent == -1 else False
        self.label = label
        self.parent_label = parent
        self.children = []

    def add_child(self, child):
        self.children.append(child)


def max_height_new(nodes, queue, height):
    while queue:
        pair = queue.pop(0)
        node, lvl = pair[0], pair[1]

        if nodes[node].children:
            lvl += 1
            for el in nodes[node].children:
                queue.append((el.label, lvl))
        if lvl > height:
            height += 1

    return height


def compute_height(n, parents):
    nodes = [Node(i, parents[i]) for i in range(n)]

    root = 0

    for child_index in range(n):
        parent_index = nodes[child_index].parent_label
        if parent_index != -1:
            nodes[parent_index].add_child(nodes[child_index])
        else:
            root = child_index

    height = 1
    queue = [(root, 1)]
    return max_height_new(nodes, queue, height)


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


main()
