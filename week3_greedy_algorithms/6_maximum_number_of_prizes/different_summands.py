# Uses python3
import sys

def optimal_summands(n):
    if n <= 2:
        return [n]
    summands = []
    i = 1
    left = n
    while i <= left:
        left -= i
        if left <= i:
            summands.append(left + i)
            return summands
        summands.append(i)
        i += 1

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
