from src.utils.utils import *

text = get_input(__file__)


def part1():
    total = 0
    for line in text.splitlines():
        ll = len(line) // 2
        a, b = line[:ll], line[ll:]
        sa = set(a)
        sb = set(b)
        for x in sa.intersection(sb):
            if ord('a') <= ord(x) <= ord('z'):
                total += (ord(x) - ord('a')) + 1
            else:
                total += (ord(x) - ord('A')) + 27

    return total


def part2():
    total = 0
    a, b, c = '', '', ''
    for i, line in enumerate(text.splitlines()):
        if i % 3 == 0:
            a = line
        elif i % 3 == 1:
            b = line
        else:
            c = line
            sa = set(a)
            sb = set(b)
            sc = set(c)
            for x in sa.intersection(sb).intersection(sc):
                if ord('a') <= ord(x) <= ord('z'):
                    total += (ord(x) - ord('a')) + 1
                else:
                    total += (ord(x) - ord('A')) + 27

    return total


print("part1:", part1())
print("part2:", part2())
