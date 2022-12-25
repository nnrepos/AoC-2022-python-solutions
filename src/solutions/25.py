from src.utils.utils import *

text = get_input(__file__)

SNAFU_MAP = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}


def snafu_to_decimal(snafu):
    ln = len(snafu)
    total = 0
    p = 1
    for i in range(ln - 1, -1, -1):
        curr = SNAFU_MAP[snafu[i]]
        total += p * curr
        p *= 5
    return total


def decimal_to_snafu(decimal):
    res = ''
    while decimal != 0:
        if decimal % 5 == 0:
            res += '0'
        elif decimal % 5 == 1:
            res += '1'
            decimal -= 1
        elif decimal % 5 == 2:
            res += '2'
            decimal -= 2
        elif decimal % 5 == 3:
            res += '='
            decimal += 2
        elif decimal % 5 == 4:
            res += '-'
            decimal += 1
        else:
            assert False

        decimal //= 5

    return res[::-1]


def part1():
    total = 0
    for line in text.splitlines():
        total += snafu_to_decimal(line.strip())
    
    return decimal_to_snafu(total)


def part2():
    return "naisu"


print("part1:", part1())
print("part2:", part2())
