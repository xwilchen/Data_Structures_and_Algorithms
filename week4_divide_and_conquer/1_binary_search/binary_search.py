# Uses python3
import sys

def binary_search_while(a, x, left, right):
    while left < right:
        mid = int((left + right) / 2)
        if a[mid] == x:
            return mid
        elif x < a[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def binary_search(a, x, left, right):
    if right < left:
        return -1

    mid = int((left + right) / 2)
    if a[mid] == x:
        return mid
    elif x < a[mid]:
        return binary_search(a,x,left,mid-1)
    else:
        return binary_search(a,x, mid+1, right)

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x, 0, len(a)-1), end = ' ')
