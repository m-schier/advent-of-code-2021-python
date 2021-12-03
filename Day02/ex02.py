import sys

depth = 0
horizontal = 0
aim = 0

for line in sys.stdin.readlines():
    cmd, val = line.split(' ')
    val = int(val)
    if cmd == 'forward':
        horizontal += val
        depth += aim * val
    elif cmd == 'down':
        aim += val
    elif cmd == 'up':
        aim -= val
    else:
        raise ValueError(line)

print(horizontal * depth)