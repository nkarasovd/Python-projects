# python3
import sys


def compute_min_refills(distance, tank, stops, n):
    num_refills = 0
    cur_refill = 0
    stops = [0] + stops + [distance]

    while cur_refill <= n:
        last_refill = cur_refill
        while cur_refill <= n and (stops[cur_refill + 1] - stops[last_refill] <= tank):
            cur_refill += 1
        if cur_refill == last_refill:
            return -1
        if cur_refill <= n:
            num_refills += 1

    return num_refills


if __name__ == '__main__':
    d, m, n, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops, n))
