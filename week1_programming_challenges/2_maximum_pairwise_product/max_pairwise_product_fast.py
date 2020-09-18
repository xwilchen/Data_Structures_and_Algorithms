# python3


def max_pairwise_product_fast(numbers):
    n = len(numbers)
    first_idx = 0
    for i in range(1,n):
        if numbers[i] > numbers[first_idx]:
            first_idx = i
    second_idx = 0
    for j in range(1,n):
        if j != first_idx and numbers[j] >= numbers[second_idx]:
            second_idx = j
    print(numbers)
    return numbers[first_idx] * numbers[second_idx]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_fast(input_numbers))
