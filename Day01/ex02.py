with open('input.txt') as f:
    lines = [int(l) for l in f.readlines()]

print(sum(a > b for a, b in zip(lines[3:], lines)))