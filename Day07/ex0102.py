import sys
import numpy as np

data = np.genfromtxt(sys.stdin, delimiter=',', dtype=int)

dists = np.sum(np.abs(data[:, None] - np.arange(np.max(data) + 1)), axis=0)
cost = np.cumsum(np.arange(np.max(data) + 1))
dists2 = np.sum(cost[np.abs(data[:, None] - np.arange(np.max(data) + 1))], axis=0)

print(np.min(dists), np.min(dists2))
