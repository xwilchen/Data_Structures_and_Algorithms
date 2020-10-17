# Uses python3
import sys

def get_change(m):
    if m == 0:
        return 0
    denominators = [1, 3, 4]
    min_coins_array = [0]
    for i in range(1, m+1):
        min_coins = []
        for denom in denominators:
            if i >= denom:
                min_coins.append(min_coins_array[i - denom] + 1)
        min_coins_array.append(min(min_coins))

    #write your code here
    return min_coins_array[-1]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))