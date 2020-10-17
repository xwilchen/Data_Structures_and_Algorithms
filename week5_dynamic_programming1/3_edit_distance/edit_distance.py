import numpy as np
# Uses python3
def edit_distance(s, t):
    dp_table = np.zeros((len(s) + 1, len(t) + 1))
    dp_table[0] = range(len(t) + 1)
    dp_table[:,0] = range(len(s) + 1)

    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i - 1] == t[j - 1]:
                dp_table[i, j] = dp_table[i - 1, j - 1]
            else:
               dp_table[i, j] = min(dp_table[i - 1, j - 1], dp_table[i - 1, j], dp_table[i, j - 1]) + 1
    return int(dp_table[len(s), len(t)])

if __name__ == "__main__":
    print(edit_distance(input(), input()))
