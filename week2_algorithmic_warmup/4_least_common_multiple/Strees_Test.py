import random
from solution import faster_gcd
from gcd import gcd_naive

def Stress_Test(N):
    while True:
        a = random.randint(1, N)
        b = random.randint(1, N)
        print(a, b)

        faster_gcd_n = faster_gcd(a, b)
        gcd_naive_n = gcd_naive(a, b)

        if faster_gcd_n == gcd_naive_n:
            print("OK!")
        else:
            assert faster_gcd_n == gcd_naive_n, f"{faster_gcd_n}, {gcd_naive_n}"

if __name__ == '__main__':
    N = int(input())
    Stress_Test(N)