import random
from solution import fib_last_digit
from fibonacci_last_digit import get_fibonacci_last_digit_naive

def Stress_Test(N):
    while True:
        n = random.randint(1, N)
        print(n)

        faster_fib = fib_last_digit(n)
        naive_fib_n = get_fibonacci_last_digit_naive(n)

        if faster_fib == naive_fib_n:
            print("OK!")
        else:
            assert faster_fib == naive_fib_n, f"{faster_fib}, {naive_fib_n}"

if __name__ == '__main__':
    N = int(input())
    Stress_Test(N)