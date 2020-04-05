# Uses python3
import sys


class Point:
    def __init__(self, value, index):
        self.value = value
        self.index = index

    def get_index(self):
        return self.index

    def get_value(self):
        return self.value


def fast_count_segments(starts, ends, points):

    points_classes = [Point(points[i], i) for i in range(len(points))]

    points_classes.sort(key=lambda x: (x.get_value()))

    cnt = [0] * len(points)
    starts.sort()
    ends.sort()

    min_start = 0
    for el in points_classes:
        if el.get_value() >= starts[min_start]:
            while min_start < len(starts) and el.get_value() >= starts[min_start]:
                min_start += 1
            min_start -= 1

            second_start = min_start
            if el.get_value() <= ends[second_start]:
                while second_start >= 0 and el.get_value() <= ends[second_start]:
                    second_start -= 1
                    cnt[el.get_index()] += 1

    return cnt


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    # use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
