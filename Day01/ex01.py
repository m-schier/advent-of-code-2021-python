import sys

lines = [int(l) for l in sys.stdin.readlines()]

print(sum(a > b for a, b in zip(lines[1:], lines)))