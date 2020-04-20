
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
        if self.n == 0:
            return self.result
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self.in_order(0)
        return self.result

    def in_order(self, i):
        if i == -1:
            return
        node = self.key[i]
        left = self.left[i]
        right = self.right[i]
        self.in_order(left)
        self.result.append(node)
        self.in_order(right)


def main():
    tree = TreeOrders()
    tree.read()
    result = tree.inOrder()
    # print(result)
    for i in range(len(result) - 1):
        if result[i + 1] <= result[i]:
            print("INCORRECT")
            break
    else:
        print("CORRECT")


threading.Thread(target=main).start()
