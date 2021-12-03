import numpy as np

def find(data, co2):
    pos = 0

    while True:
        common = np.sum(data[:, pos]) >= len(data) / 2

        if co2:
            common = not common

        data = data[data[:, pos] == common]

        if len(data) <= 1:
            return int(''.join(['1' if a else '0' for a in data[0]]), 2)
        
        pos += 1

with open("input.txt") as f:
    lines = [list(l.strip()) for l in f.readlines()]

data = np.array(lines) == '1'
print(find(data, True) * find(data, False))
