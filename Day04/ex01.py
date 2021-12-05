import sys
import numpy as np


def PartReader():
    def read_part(line):
        while True:
            if len(line.strip()) == 0:
                return
            yield line
            line = sys.stdin.readline()

    while True:
        line = sys.stdin.readline()
        if not line:
            break
        yield read_part(line)


part_reader = PartReader()
seq = np.loadtxt(next(part_reader), delimiter=',').astype(int)
boards = np.array([np.loadtxt(r) for r in part_reader]).astype(int)
marked = np.zeros(boards.shape, dtype=bool)

first_score = None
last_score = None

for s in seq:
    marked[boards == s] = True
    won_by_row = np.any(np.all(marked, axis=1), axis=1)
    won_by_col = np.any(np.all(marked, axis=2), axis=1)
    won_mask = np.logical_or(won_by_col, won_by_row)
    won = np.nonzero(won_mask)[0]

    if len(won) == 1 and first_score is None:
        first_score = np.sum(boards[won[0], np.logical_not(marked[won[0]])]) * s
    elif len(won) == 1 and len(boards) == 1 and last_score is None:
        last_score = np.sum(boards[won[0], np.logical_not(marked[won[0]])]) * s

    # Drop won boards
    not_won_mask = np.logical_not(won_mask)
    boards, marked = boards[not_won_mask], marked[not_won_mask]

print(first_score, last_score)