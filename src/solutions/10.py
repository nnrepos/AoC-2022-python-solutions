from src.utils.utils import *

text = get_input(__file__)
ss = splitsplit(text)


def part1():
    cycle = 1
    x = 1
    total = 0
    for c, *rest in ss:
        if cycle in (20, 60, 100, 140, 180, 220):
            total += cycle * x
        if c == 'noop':
            cycle += 1

        else:
            n = int(rest[0])
            cycle += 1
            if cycle in (20, 60, 100, 140, 180, 220):
                total += cycle * x
            x += n
            cycle += 1

    return total


def part2():
    cycle = 0
    x = 1
    result = []
    col = -1
    for c, *rest in ss:
        row = cycle % 40
        if row == 0:
            result.append('')
            col += 1
        if x - 1 <= row <= x + 1:
            result[col] += '#'
        else:
            result[col] += '.'
        if c == 'noop':
            cycle += 1

        else:
            n = int(rest[0])
            cycle += 1
            row = cycle % 40
            if row == 0:
                result.append('')
                col += 1
            if x - 1 <= row <= x + 1:
                result[col] += '#'
            else:
                result[col] += '.'
            x += n
            cycle += 1

    return '\n' + '\n'.join(result)


print("part1:", part1())
print("part2:", part2())
