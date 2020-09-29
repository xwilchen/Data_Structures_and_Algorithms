# Uses python3
def calc_fib(n):
    if n <= 1:
        return n
    arr = [0,1]
    for i in range(2,n):
        arr.append(arr[i - 1] + arr[i - 2])
    return arr[-1] + arr[-2]

if __name__ == '__main__':
    n = int(input())
    print(calc_fib(n))
