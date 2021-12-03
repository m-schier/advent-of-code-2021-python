import numpy as np

with open("input.txt") as f:
    lines = [list(l.strip()) for l in f.readlines()]

data = np.array(lines) == '1'

gamma_bits = np.sum(data, axis=0) > len(data) / 2
gamma = int(''.join(['1' if a else '0' for a in gamma_bits]), 2)
epsilon = 2 ** data.shape[1] - 1 - gamma

print(gamma * epsilon)
