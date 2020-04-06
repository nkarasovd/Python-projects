# Uses python3
import sys
import math

"""
Идея: разбиваем на две части, ищем минимум в каждой, потом ищем минимум в полосе.
Причем в полосе смотрим только 7 ближайших точек:

Итак, пусть мы рассматриваем какую-то точку p_i;
напомним, что множество C(p_i) — это множество точек, y-координата которых лежит в отрезке [y_i-h; y_i],
а, кроме того, по координате x и сама точка p_i, и все точки множества C(p_i) лежат в полосе шириной 2h.
Иными словами, рассматриваемые нами точки p_i и C(p_i) лежат в прямоугольнике размера 2h * h.

Наша задача — оценить максимальное количество точек, которое может лежать в этом прямоугольнике 2h * h;
тем самым мы оценим и максимальный размер множества C(p_i). При этом при оценке надо не забывать,
что могут встречаться повторяющиеся точки.

Вспомним, что h получалось как минимум из двух результатов рекурсивных вызовов — от множеств A_1 и A_2,
причём A_1 содержит точки слева от линии раздела и частично на ней,
A_2 — оставшиеся точки линии раздела и точки справа от неё. Для любой пары точек из A_1, равно как и из A_2,
расстояние не может оказаться меньше h — иначе бы это означало некорректность работы рекурсивной функции.

Для оценки максимального количества точек в прямоугольнике 2h * h разобьём его на два квадрата h * h,
к первому квадрату отнесём все точки C(p_i) пересечь с A_1, а ко второму — все остальные,
т.е. C(p_i) пересечь с A_2. Из приведённых выше соображений следует,
что в каждом из этих квадратов расстояние между любыми двумя точками не менее h.

Покажем, что в каждом квадрате не более четырёх точек. Например, это можно сделать следующим образом:
разобьём квадрат на 4 подквадрата со сторонами h/2. Тогда в каждом из этих подквадратов
не может быть больше одной точки (т.к. даже диагональ равна h / \sqrt{2}, что меньше h).
Следовательно, во всём квадрате не может быть более 4 точек.

Итак, мы доказали, что в прямоугольнике 2h * h не может быть больше 4 * 2 = 8 точек, а, следовательно,
размер множества C(p_i) не может превосходить 7, что и требовалось доказать."""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return str([self.x, self.y])


def distance(p1, p2):
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5


def construct_points(x, y):
    points = []
    for i in range(len(x)):
        points.append(Point(x[i], y[i]))

    return points


def minimum_distance(x, y):
    points = construct_points(x, y)
    sorted_p_x = sorted(points, key=lambda p: p.x)

    return large_size_min_distance(sorted_p_x)


def small_size_min_distance(points):
    result = sys.maxsize
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            result = min(result, distance(points[i], points[j]))
    return result


def large_size_min_distance(p_x):
    size = len(p_x)
    half_size = size // 2

    if size <= 3:
        return small_size_min_distance(p_x)

    left_p_x = p_x[:half_size]
    right_p_x = p_x[half_size:]

    left_min = large_size_min_distance(left_p_x)
    right_min = large_size_min_distance(right_p_x)

    separated_min = min(left_min, right_min)

    line_l = (left_p_x[-1].x + right_p_x[0].x) / 2

    hybrid_min = compute_hybrid_min(left_p_x, right_p_x, line_l, separated_min)

    return min(separated_min, hybrid_min)


def compute_hybrid_min(left_x, right_x, line_l, wide):
    left = []
    for i in range(len(left_x)):
        if abs(left_x[i].x - line_l) <= wide:
            left.append(left_x[i])
    right = []
    for i in range(len(right_x)):
        if abs(right_x[i].x - line_l) <= wide:
            right.append(right_x[i])
    total = left + right

    total = sorted(total, key=lambda p: p.y)

    result = wide
    for i in range(len(total)):
        for j in range(i + 1, min(i + 8, len(total))):
            if abs(total[i].y - total[j].y) <= wide:
                result = min(result, distance(total[i], total[j]))

    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
