from src.utils.utils import *

text = get_input(__file__)
ss = splitsplit(text, ',')


def part1():
    ans = 0
    for s in ss:
        a, b = s
        a = a.split('-')
        a1 = int(a[0])
        a2 = int(a[1])
        b = b.split('-')
        b1 = int(b[0])
        b2 = int(b[1])

        aa = list(range(a1, a2 + 1))
        bb = list(range(b1, b2 + 1))
        if all(x in bb for x in aa) or all(y in aa for y in bb):
            ans += 1

    return ans


def part2():
    ans = 0
    for s in ss:
        a, b = s
        a = a.split('-')
        a1 = int(a[0])
        a2 = int(a[1])
        b = b.split('-')
        b1 = int(b[0])
        b2 = int(b[1])

        aa = list(range(a1, a2 + 1))
        bb = list(range(b1, b2 + 1))
        if any(x in bb for x in aa) or any(y in aa for y in bb):
            ans += 1

    return ans


print("part1:", part1())
print("part2:", part2())
