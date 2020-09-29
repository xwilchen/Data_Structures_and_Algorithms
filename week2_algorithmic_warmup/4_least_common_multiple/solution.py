def faster_gcd(a, b):
    if a == b:
        return a

    big = max(a, b)
    small = min(a, b)
    while big % small != 0:
        big, small = small, big % small
    return small

if __name__ == "__main__":
    N = int(input())
    print(faster_gcd(N))