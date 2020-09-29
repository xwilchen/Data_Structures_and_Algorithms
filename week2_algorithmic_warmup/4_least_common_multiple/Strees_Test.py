import random
from solution import faster_lcm
from lcm import lcm_naive

def Stress_Test(N):
    while True:
        a = random.randint(1, N)
        b = random.randint(1, N)
        print(a, b)

        faster_lcm_n = faster_lcm(a, b)
        lcm_naive_n = lcm_naive(a, b)

        if faster_lcm_n == lcm_naive_n:
            print("OK!")
        else:
            assert faster_lcm_n == lcm_naive_n, f"{faster_lcm_n}, {lcm_naive_n}"

if __name__ == '__main__':
    N = int(input())
    Stress_Test(N)