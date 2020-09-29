import random
from fibonacci import calc_fib
from naive_fib import naive_fib

def Stress_Test(N):
    while True:
        n = random.randint(1, N)
        print(n)

        faster_fib = calc_fib(n)
        naive_fib_n = naive_fib(n)

        if faster_fib == naive_fib_n:
            print("OK!")
        else:
            assert faster_fib == naive_fib_n, f"{faster_fib}, {naive_fib_n}"

if __name__ == '__main__':
    N = int(input())
    Stress_Test(N)