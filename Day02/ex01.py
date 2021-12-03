depth = 0
horizontal = 0

with open("input.txt") as f:
    for line in f.readlines():
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