# python3
import sys


def compute_min_refills(distance, tank, stops):
    full_stops = [0] + stops + [distance]
    current_stop = 0
    refill_count = 0

    while current_stop <= len(stops):
        last_refill = current_stop
        while current_stop <= len(stops) and tank >= full_stops[current_stop + 1] - full_stops[last_refill]:
            current_stop += 1
        if current_stop == last_refill:
            return -1
        if current_stop <= len(stops):
            refill_count += 1
    return refill_count

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
