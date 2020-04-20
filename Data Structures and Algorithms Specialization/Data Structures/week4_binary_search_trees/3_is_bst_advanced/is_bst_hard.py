import sys
import threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
    def __init__(self):
        pass

    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for _ in range(self.n)]
        self.left = [0 for _ in range(self.n)]
        self.right = [0 for _ in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self):
        self.result = []
        self.height = []
        if self.n == 0:
            return [self.result, self.height]
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self.in_order(0, 'm', 0)
        return [self.result, self.height]

    def in_order(self, i, char, height):
        if i == -1:
            return
        node = self.key[i]
        left = self.left[i]
        right = self.right[i]
        self.in_order(left, 'l', height + 1)
        self.result.append((node, char))
        self.height.append(height + 1)
        self.in_order(right, 'r', height + 1)


def main():
    tree = TreeOrders()
    tree.read()
    result, height = tree.inOrder()
    # print(result)
    for i in range(len(result) - 1):
        if result[i + 1][0] < result[i][0] or result[i + 1][0] == result[i][0] and height[i] > height[i + 1] and \
                result[i][1] == 'l':
            print("INCORRECT")
            break
    else:
        print("CORRECT")


threading.Thread(target=main).start()
