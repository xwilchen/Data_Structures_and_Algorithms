from gcd import faster_gcd

def faster_lcm(a, b):
    if a == b:
        return a

    big = max(a, b)
    small = min(a, b)
    if big % small == 0:
        return big

    gcd = faster_gcd(a, b)
    return a * b / gcd

if __name__ == "__main__":
    a, b = [int(num) for num in str(input()).split()]
    print(faster_lcm(a, b))