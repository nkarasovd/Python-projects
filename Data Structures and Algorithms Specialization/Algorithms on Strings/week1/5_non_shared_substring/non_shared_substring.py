# python3
# python3
import sys

sys.setrecursionlimit(100000)


class Node:
    def __init__(self, label=''):
        self.label = label
        self.next = []
        self.count = 0
        self.path = ''

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
        new_node = Node(current_suffix)
        new_node.path += current_node.path + current_node.label + new_node.label
        current_node.next.append(new_node)
        result.append(current_suffix)
    else:
        edge_label = node.label
        i = find(edge_label, current_suffix)

        if i != -1:
            head, tail = edge_label[:i], edge_label[i:]

            node_tail = Node(tail)
            node_tail.next.extend(node.next)
            node_tail.path += node.path + node.label

            node.label = head
            new_node = Node(current_suffix[i:])
            new_node.path += node.path + node.label
            node.next = [node_tail, new_node]

            result.extend([head, tail, current_suffix[i:]])
            result.remove(edge_label)
        else:
            build_suffix_tree_util(node, current_suffix[len(edge_label):], result)


def iter(tree, result, string):
    count = 0
    for el in tree:
        if '#' in el.label and len(el.next) == 0:
            count += 1
    if count == len(tree.next):
        result.append(tree.path)
    else:
        tree.count = 0
        for el in tree:
            if '#' in el.label and len(el.next) == 0:
                result.append(el.path + el.label[0])
            else:
                string += el.label
                iter(el, result, string)


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

    result = []
    string = ''
    iter(tree, result, string)
    # for el in tree:
    #     string = el.label
    #     iter(tree, result, string)

    return result


def solve(p, q):
    result = build_suffix_tree(p + '#' + q + '$')
    result.sort(key=lambda x: len(x))
    return result


if __name__ == '__main__':
    p = sys.stdin.readline().strip()
    q = sys.stdin.readline().strip()

    ans = solve(p, q)
    print("\n".join(ans))
    # sys.stdout.write(ans + '\n')
