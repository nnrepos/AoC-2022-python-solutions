from src.utils.utils import *

text = get_input(__file__)
ss = splitsplit(text, None)


def part1():
    for i in range(3, len(text)):
        a = text[i]
        b = text[i - 1]
        c = text[i - 2]
        dd = text[i - 3]
        if a == b or b == c or c == dd or a == c or a == dd or b == dd:
            continue
        return i + 1

    return -1


def part2():
    for i in range(14, len(text)):
        c = Counter(text[i - 14: i])

        good = True
        for k, v in c.items():
            if v > 1:
                good = False
                break
        if not good:
            continue
        return i

    return -1


print("part1:", part1())
print("part2:", part2())
