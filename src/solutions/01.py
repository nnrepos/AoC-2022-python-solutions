from src.utils.utils import *

lines = get_input(__file__)

def top3():
    curr = 0
    m1, m2, m3 = 0, 0, 0
    for line in (lines + "\n").splitlines():
        if line:
            curr += int(line)
        else:
            if curr > m1:
                m3 = m2
                m2 = m1
                m1 = curr
            elif curr > m2:
                m3 = m2
                m2 = curr
            elif curr > m3:
                m3 = curr
            curr = 0

    return m1, m2, m3


def part1():
    return top3()[0]


def part2():
    return sum(top3())


print("part1:", part1())
print("part2:", part2())
