def fib_last_digit(n):
    previous = 0
    current = 1
    for i in range(n - 1):
        previous, current = current, (previous + current) % 10
    return current

if __name__ == "__main__":
    N = int(input())
    print(fib_last_digit(N))