# python3
import sys

sys.setrecursionlimit(100000)


class Node:
    def __init__(self, label='Root'):
        self.label = label
        self.next = []
        self.count = 0

    def __next__(self):
        if self.count < len(self.next):
            self.count += 1
            return self.next[self.count - 1]
        else:
            raise StopIteration

    def __iter__(self):
        return self


def find(old_edge, current_suffix):
    length = min(len(old_edge), len(current_suffix))
    for i in range(length):
        if old_edge[i] != current_suffix[i]:
            return i
    return -1


def build_suffix_tree_util(current_node, current_suffix, result):
    first_symbol = current_suffix[0]
    node = None

    for el in current_node.next:
        if first_symbol == el.label[0]:
            node = el
            break

    if node is None:
        current_node.next.append(Node(current_suffix))
        result.append(current_suffix)
    else:
        edge_label = node.label
        i = find(edge_label, current_suffix)

        if i != -1:
            head, tail = edge_label[:i], edge_label[i:]

            node_tail = Node(tail)
            node_tail.next.extend(node.next)

            node.label = head
            node.next = [node_tail, Node(current_suffix[i:])]

            result.extend([head, tail, current_suffix[i:]])
            result.remove(edge_label)
        else:
            build_suffix_tree_util(node, current_suffix[len(edge_label):], result)


def iter(tree, result):
    for el in tree:
        result.append(el.label)
        iter(el, result)


def build_suffix_tree(text):
    """
    Build a suffix tree of the string text and return a list
    with all of the labels of its edges (the corresponding
    substrings of the text) in any order.
    """
    tree = Node()
    result = []
    for i in range(len(text)):
        current_suffix = text[i:]
        current_node = tree
        build_suffix_tree_util(current_node, current_suffix, result)

    # result = []
    # iter(tree, result)

    return result


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    result = build_suffix_tree(text)
    print("\n".join(result))
