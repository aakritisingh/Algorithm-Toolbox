# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    stops.sort(reverse=True)
    num_stops = 0
    first_stop = 0
    max_index = 0
    for i, stop in enumerate(stops):
        if tank - stop > 0:
            first_stop = stop
            max_index = i
            num_stops += 1
            break
        else:
            print("going further away")
            return -1
    if distance - first_stop < tank:
        return num_stops

    return -1

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
