# python3


def build_heap_naive(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps


class Heap:
    def __init__(self, data):
        self.data = data
        self.size = len(self.data)
        self.n_swap = 0
        self.swaps = []

    def build_heap(self):
        for i in range(self.size // 2, -1, -1):
            self.swift_down(i)

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swift_down(self, i):
        max_index = i
        l = self.left_child(i)
        if l < self.size and self.data[l] < self.data[max_index]:
            max_index = l
        r = self.right_child(i)
        if r < self.size and self.data[r] < self.data[max_index]:
            max_index = r
        if i != max_index:
            self.data[i], self.data[max_index] = self.data[max_index], self.data[i]
            self.n_swap += 1
            self.swaps.append((i, max_index))
            self.swift_down(max_index)


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    h = Heap(data)
    h.build_heap()
    print(h.n_swap)

    for i, j in h.swaps:
        print(i, j)


if __name__ == "__main__":
    main()
