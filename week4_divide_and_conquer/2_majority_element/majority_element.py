# Uses python3
import sys

def get_majority_element(a):
    count = {}
    for n in a:
        if n not in count:
            count[n] = 1
        else:
            count[n] += 1
    if max(count.values()) * 2 > len(a):
        return 1
    else:
        return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a) != -1:
        print(1)
    else:
        print(0)
