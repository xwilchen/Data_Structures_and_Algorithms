import random
import max_pairwise_product
import max_pairwise_product_fast


def Stress_Test(N, M):
    while True:
        n = random.randint(2, N)
        A = list(range(n))
        for i in A:
            A[i] = random.randint(0, M)
        print(A)

        naive_result = max_pairwise_product.max_pairwise_product(A)
        fast_result = max_pairwise_product_fast.max_pairwise_product_fast(A)

        if naive_result == fast_result:
            print("OK!")
        else:
            print("Wrong Answer!",naive_result, fast_result)
            return


if __name__ == '__main__':
    N, M = [int(number) for number in input().split()]
    Stress_Test(N, M)
