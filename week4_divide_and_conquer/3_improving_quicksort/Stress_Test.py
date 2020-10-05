from sorting import randomized_quick_sort, randomized_quick_sort_2_part
import random

def Stress_Test(N):

    while True:
        arr_len = random.randint(1,N)
        arr = [random.randint(1,N) for i in range(arr_len)]
        arr2 = arr.copy()
        print(arr)
        randomized_quick_sort(arr, 0, arr_len - 1)
        randomized_quick_sort_2_part(arr2, 0, arr_len-1)
        if arr == arr2:
            print("OK!")
        else:
            print("Fail!")
            print(arr, arr2)
            return

if __name__ == '__main__':
    N = int(input())
    Stress_Test(N)