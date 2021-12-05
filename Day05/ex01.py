import sys
import numpy as np


vents = []

for line in sys.stdin.readlines():
    v1, v2 = line.split(' -> ')
    vents.append(([int(c) for c in v1.split(',')], [int(c) for c in v2.split(',')]))

vents = np.array(vents)
map = np.zeros(np.max(vents, axis=(0, 1)) + 1, dtype=int)

for (v1x, v1y), (v2x, v2y) in vents:
    vay, vby = min(v1y, v2y), max(v1y, v2y)
    vax, vbx = min(v1x, v2x), max(v1x, v2x)
    if v1x == v2x:
        map[vay:vby+1, v1x] += 1
    elif v1y == v2y:
        map[v1y, vax:vbx+1] += 1

print(map)
print(np.sum(map >= 2))