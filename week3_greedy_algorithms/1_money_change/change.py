# Uses python3
import sys

def get_change(m):
    coins = 0
    ris = m
    for value in [10,5,1]:
        coins += int(ris / value)
        ris = ris % value
    return coins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
