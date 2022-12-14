from src.utils.utils import *

text = get_input(__file__)
ss = splitsplit(text, '->')

m = None


def add_rocks(last_x, last_y, x, y):
    global m
    xx = min(last_x, x)
    xxx = max(last_x, x)
    yy = min(last_y, y)
    yyy = max(last_y, y)

    for a in range(xx, xxx + 1):
        for b in range(yy, yyy + 1):
            m[b][a] = '#'


def part1():
    global m
    m = [['.' for _ in range(1000)] for _ in range(1000)]
    max_rock_y = 0
    min_rock_y = 1000
    for line in ss:
        last_x, last_y = None, None
        for coords in line:
            x, y = (int(i) for i in coords.strip().split(','))
            if last_x is not None:
                add_rocks(last_x, last_y, x, y)
            last_x, last_y = x, y
            max_rock_y = max(max_rock_y, y)
            min_rock_y = min(min_rock_y, y)

    done = False
    at_rest = 0
    while not done:
        curr_x = 500
        curr_y = min_rock_y - 1

        while True:
            if curr_y > max_rock_y:
                done = True
                break

            if m[curr_y + 1][curr_x] == '.':
                curr_y += 1
            elif m[curr_y + 1][curr_x - 1] == '.':
                curr_y += 1
                curr_x -= 1
            elif m[curr_y + 1][curr_x + 1] == '.':
                curr_y += 1
                curr_x += 1
            else:
                at_rest += 1
                m[curr_y][curr_x] = 'o'
                min_rock_y = min(min_rock_y, curr_y)
                break

    return at_rest


def part2():
    global m
    m = [['.' for _ in range(1000)] for _ in range(1000)]
    max_rock_y = 0
    min_rock_y = 1000
    for line in ss:
        last_x, last_y = None, None
        for coords in line:
            x, y = (int(i) for i in coords.strip().split(','))
            if last_x is not None:
                add_rocks(last_x, last_y, x, y)
            last_x, last_y = x, y
            max_rock_y = max(max_rock_y, y)
            min_rock_y = min(min_rock_y, y)
    floor_y = max_rock_y + 2
    add_rocks(0, floor_y, 999, floor_y)

    done = False
    at_rest = 0
    while not done:
        curr_x = 500
        curr_y = min_rock_y - 1

        while True:
            if curr_y == -1:
                done = True
                break

            if m[curr_y + 1][curr_x] == '.':
                curr_y += 1
            elif m[curr_y + 1][curr_x - 1] == '.':
                curr_y += 1
                curr_x -= 1
            elif m[curr_y + 1][curr_x + 1] == '.':
                curr_y += 1
                curr_x += 1
            else:
                at_rest += 1
                m[curr_y][curr_x] = 'o'
                min_rock_y = min(min_rock_y, curr_y)
                break

    return at_rest


print("part1:", part1())
print("part2:", part2())
