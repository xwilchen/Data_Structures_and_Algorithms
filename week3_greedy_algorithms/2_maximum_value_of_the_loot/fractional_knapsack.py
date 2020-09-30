# Uses python3
import sys

def get_optimal_value(capacity, values, weights):
    
    vw_list = [(idx, values[idx]/w, w) for idx, w in enumerate(weights)]
    vw_list = sorted(vw_list, key = lambda x: x[1], reverse = True)
    left_cap = capacity
    value = 0
    for vw in vw_list:
        if left_cap >= vw[2]:
            value += vw[1] * vw[2]
            left_cap -= vw[2]
        else:
            value += vw[1] * left_cap
            left_cap -= left_cap

        if left_cap == 0:
            return value
    return value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    weights = data[2:(2 * n + 2):2]
    values = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
