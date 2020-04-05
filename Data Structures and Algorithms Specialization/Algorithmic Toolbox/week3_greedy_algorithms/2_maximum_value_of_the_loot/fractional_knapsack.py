# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0.
    items = [(values[i] / weights[i], weights[i]) for i in range(len(values))]
    items.sort(key=lambda x: (x[0], x[1]), reverse=True)
    items_len = len(items)
    i = 0
    while capacity != 0 and i != items_len:
        min_weight = min(capacity, items[i][1])
        value += items[i][0] * min_weight
        capacity -= min_weight
        i += 1
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
