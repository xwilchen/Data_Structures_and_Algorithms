# Uses python3
import sys

def optimal_sequence(n):
    if n == 1:
        return [1]
    operations = [1, 2, 3]
    min_steps = [0,0]
    for i in range(2, n+1):
        calculated_steps = []
        if i % 3 == 0:
            calculated_steps.append(min_steps[i // 3] + 1)
        if i % 2 == 0:
            calculated_steps.append(min_steps[i // 2] + 1)
        calculated_steps.append(min_steps[i - 1] + 1)
        min_steps.append(min(calculated_steps))

    sequence = [n]
    while sequence[-1] > 1:
        calculated_steps = []
        if sequence[-1] % 3 == 0:
            calculated_steps.append((sequence[-1] // 3, min_steps[sequence[-1] // 3]))
        if sequence[-1] % 2 == 0:
            calculated_steps.append((sequence[-1] // 2, min_steps[sequence[-1] // 2]))
        calculated_steps.append((sequence[-1] - 1, min_steps[sequence[-1] - 1]))
        calculated_steps = sorted(calculated_steps, key=lambda x: x[1])
        sequence.append(calculated_steps[0][0])
    return reversed(sequence)

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    sequence = list(optimal_sequence(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')
