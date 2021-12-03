import sys

depth = 0
horizontal = 0

for line in sys.stdin.readlines():
    cmd, val = line.split(' ')
    val = int(val)
    if cmd == 'forward':
        horizontal += val
    elif cmd == 'down':
        depth += val
    elif cmd == 'up':
        depth -= val
    else:
        raise ValueError(line)

print(horizontal * depth)