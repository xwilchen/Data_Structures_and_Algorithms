# python3
import sys


def compute_min_refills(distance, tank, stops):
    if tank >= distance:
        return -1
    if len(stops) == 0 and distance > tank:
        return -1

    refill_stop = 0
    refill_count = 0
    while refill_stop
    for stop in stops:
        if tank + refill_stop > stop and distance - refill_stop > tank:
            last_stop = stop
        elif tank == stop - refill_stop:
            refill_stop = stop
            last_stop = stop
            refill_count += 1
        else:
            refill_stop = last_stop
            refill_count += 1
    if refill_stop != 0:
        return refill_count
    else:
        return -1

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
