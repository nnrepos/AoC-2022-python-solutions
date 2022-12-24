from src.utils.utils import *

text = get_input(__file__)
# text = '''#.######
# #>>.<^<#
# #.<..<<#
# #>v.><>#
# #<^v^^>#
# ######.#'''

blizzards0 = None
start = None
end = None
maxwall_row = 0
maxwall_col = 0

ARROWS = ('<', '^', '>', 'v')


def parse():
    global blizzards0
    global maxwall_row
    global maxwall_col
    global start
    global end
    start = 0 + 1j
    blizzards0 = set()
    for i, line in enumerate(text.splitlines()):
        for j, c in enumerate(line):
            if c == '#':
                maxwall_row = max(maxwall_row, i)
                maxwall_col = max(maxwall_col, j)
            elif c in ARROWS:
                blizzards0.add((i + j * 1j, c))

    end = maxwall_row + (maxwall_col - 1) * 1j


@lru_cache(maxsize=None)
def get_bliz_at(bliz_id):
    if bliz_id == 0:
        return blizzards0

    curr_bliz = get_bliz_at(bliz_id - 1)
    next_bliz = set()
    for coords, direction in curr_bliz:
        if direction == '<':
            coords -= 1j
        elif direction == '^':
            coords -= 1
        elif direction == '>':
            coords += 1j
        else:
            assert direction == 'v'
            coords += 1

        if coords.real == 0:
            coords = round(coords.imag) * 1j + maxwall_row - 1
        elif coords.real == maxwall_row:
            coords = round(coords.imag) * 1j + 1
        elif coords.imag == 0:
            coords = round(coords.real) + (maxwall_col - 1) * 1j
        elif coords.imag == maxwall_col:
            coords = round(coords.real) + 1j

        assert round(coords.real) in range(1, maxwall_row), f"curr_bliz can't escape map {coords}"
        assert round(coords.imag) in range(1, maxwall_col), f"curr_bliz can't escape map {coords}"

        next_bliz.add((coords, direction))

    return next_bliz


def is_legal(coord, bliz: set) -> bool:
    for arrow in ARROWS:
        if (coord, arrow) in bliz:
            return False
    if coord in (start, end):
        return True
    if coord.real not in range(1, maxwall_row):
        return False
    if coord.imag not in range(1, maxwall_col):
        return False

    return True


def print_bliz_at(bliz_id):
    print('bliz at', bliz_id)
    bliz = get_bliz_at(bliz_id)
    print('#.' + '#' * (maxwall_col - 1))
    for i in range(1, maxwall_row):
        print('#', end='')
        for j in range(1, maxwall_col):
            found = '.'
            for ar in ARROWS:
                if (i + j * 1j, ar) in bliz:
                    if found != '.':
                        found = 2
                    else:
                        found = ar
            print(found, end='')
        print('#')
    print(('#' * (maxwall_col - 1)) + '.#')


def part1():
    parse()
    time0 = 0
    curr_time = time0
    state0 = (start, time0)
    curr_states = {state0}

    while True:
        next_states = set()
        next_time = curr_time + 1
        next_bliz = get_bliz_at(next_time)
        for s in curr_states:
            curr_coords, _ = s
            for delta in (COMPLEX_ADJ + [0]):
                next_coords = curr_coords + delta
                if is_legal(next_coords, next_bliz):
                    if next_coords == end:
                        return next_time
                    next_states.add((next_coords, next_time))

        curr_time = next_time
        curr_states = next_states


def part2():
    parse()
    time0 = 0
    checkpoint0 = 0
    curr_time = time0
    state0 = (start, time0, checkpoint0)
    curr_states = {state0}

    while True:
        next_states = set()
        next_time = curr_time + 1
        next_bliz = get_bliz_at(next_time)
        for s in curr_states:
            curr_coords, _, curr_checkpoint = s
            curr_end = end if (curr_checkpoint % 2 == 0) else start
            for delta in (COMPLEX_ADJ + [0]):
                next_checkpoint = curr_checkpoint
                next_coords = curr_coords + delta
                if is_legal(next_coords, next_bliz):
                    if next_coords == curr_end:
                        next_checkpoint += 1
                        if next_checkpoint == 3:
                            return next_time
                    next_states.add((next_coords, next_time, next_checkpoint))

        curr_time = next_time
        curr_states = next_states


print("part1:", part1())
print("this takes ~5 sec")
print("part2:", part2())
