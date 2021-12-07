import sys


def resolve(age, remaining, lut):
    if (age, remaining) in lut:
        return lut[(age, remaining)]

    if remaining <= 0:
        result = 1
    elif age < 0:
        assert age == -1
        result = resolve(6, remaining - 1, lut) + resolve(8, remaining - 1, lut)
    else:
        result = resolve(-1, remaining - age, lut)

    lut[(age, remaining)] = result
    return result


arr = [int(p) for p in sys.stdin.readline().split(',')]

lut = {}

print(sum([resolve(f, 256, lut) for f in arr]))
print(sum([resolve(f, 80, lut) for f in arr]))
