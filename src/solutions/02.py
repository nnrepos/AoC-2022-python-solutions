from src.utils.utils import *

text = get_input(__file__)


def part1():
    # X 1 Y2 Z3
    # lose 0 draw 3 win 6
    total = 0
    for them, me in splitsplit(text):
        if them == 'A' and me == 'X':
            total += 1 + 3
        if them == 'A' and me == 'Y':
            total += 2 + 6
        if them == 'A' and me == 'Z':
            total += 3 + 0
        if them == 'B' and me == 'X':
            total += 1 + 0
        if them == 'B' and me == 'Y':
            total += 2 + 3
        if them == 'B' and me == 'Z':
            total += 3 + 6
        if them == 'C' and me == 'X':
            total += 1 + 6
        if them == 'C' and me == 'Y':
            total += 2 + 0
        if them == 'C' and me == 'Z':
            total += 3 + 3

    return total


def part2():
    # X lose Y draw Z win
    total = 0
    for them, me in splitsplit(text):
        if them == 'A' and me == 'X':
            total += 3 + 0
        if them == 'A' and me == 'Y':
            total += 1 + 3
        if them == 'A' and me == 'Z':
            total += 2 + 6
        if them == 'B' and me == 'X':
            total += 1 + 0
        if them == 'B' and me == 'Y':
            total += 2 + 3
        if them == 'B' and me == 'Z':
            total += 3 + 6
        if them == 'C' and me == 'X':
            total += 2 + 0
        if them == 'C' and me == 'Y':
            total += 3 + 3
        if them == 'C' and me == 'Z':
            total += 1 + 6
    return total


print("part1:", part1())
print("part2:", part2())
