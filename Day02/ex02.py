depth = 0
horizontal = 0
aim = 0

with open("input.txt") as f:
    for line in f.readlines():
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