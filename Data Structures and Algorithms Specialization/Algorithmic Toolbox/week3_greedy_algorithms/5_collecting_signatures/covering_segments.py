# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments, n):
    points = []

    segments.sort(key=lambda x: (x[1], x[0]))
    points.append(segments[0][1])

    for el in segments:
        if not (el[0] <= points[-1] <= el[1]):
            points.append(el[1])

    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments, n)
    print(len(points))
    print(*points)
