def naive_fib(n):
    if (n <= 1):
        return n
    return naive_fib(n - 1) + naive_fib(n - 2)

if __name__ == '__main__':
    n = int(input())
    print(naive_fib(n))