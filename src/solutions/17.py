from src.utils.utils import *

text = get_input(__file__)
# text = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'
ss = splitsplit(text)

# y, x
ROCK0 = {(0, 2), (0, 3), (0, 4), (0, 5)}
ROCK1 = {(2, 3), (1, 2), (1, 3), (1, 4), (0, 3)}
ROCK2 = {(2, 4), (1, 4), (0, 2), (0, 3), (0, 4)}
ROCK3 = {(3, 2), (2, 2), (1, 2), (0, 2)}
ROCK4 = {(1, 2), (1, 3), (0, 2), (0, 3)}
ROCK_ORDER = (ROCK0, ROCK1, ROCK2, ROCK3, ROCK4)
ROCK_TYPES = len(ROCK_ORDER)
NUM_ROCKS = 2022
BIG_NUM_ROCKS = 1000000000000
DELTA = 4
WIDTH = 7
WALL_RANGE = range(WIDTH)
FLOOR_Y = 0

pushes = text.strip()
n = len(pushes)


def is_free_below(curr_rock, blocks):
    for y, x in curr_rock:
        new_y = y - 1
        if (new_y, x) in blocks or new_y < FLOOR_Y:
            return False
    return True


def is_free_sideways(curr_rock, delta, blocks):
    for y, x in curr_rock:
        new_x = x + delta
        if new_x not in WALL_RANGE or (y, new_x) in blocks:
            return False
    return True


def drop_new_rock(direction_index, rock_index, blocks, highest_block, highest_block_per_x):
    # create starting rock
    rock_template = ROCK_ORDER[rock_index % ROCK_TYPES]
    curr_rock = set()
    for block in rock_template:
        curr_block = (block[0] + DELTA + highest_block, block[1])
        curr_rock.add(curr_block)

    while True:
        # move sideways
        direction = pushes[direction_index % n]
        delta = (1 if direction == '>' else -1)
        if is_free_sideways(curr_rock, delta, blocks):
            new_curr_rock = set()
            for y, x in curr_rock:
                new_curr_rock.add((y, x + delta))
            curr_rock = new_curr_rock
        direction_index += 1

        # move down
        if is_free_below(curr_rock, blocks):

            new_curr_rock = set()
            for y, x in curr_rock:
                new_curr_rock.add((y - 1, x))
            curr_rock = new_curr_rock
        else:
            break

    # store blocks
    blocks |= curr_rock
    curr_highest_block = max(y for y, _ in curr_rock)
    highest_block = max(curr_highest_block, highest_block)

    if highest_block_per_x:
        for y, x in curr_rock:
            highest_block_per_x[x] = max(highest_block_per_x[x], y)

    return direction_index, curr_rock, highest_block


def part1():
    blocks = set()
    highest_block = -1
    direction_index = 0

    for rock_index in range(NUM_ROCKS):
        direction_index, curr_rock, highest_block = drop_new_rock(direction_index, rock_index, blocks, highest_block, None)

    return highest_block + 1  # 0 indexed


def part2():
    blocks = set()
    highest_block = -1
    highest_block_per_x = [-1 for _ in range(WIDTH)]
    direction_index = 0
    states = {}
    found = False
    rock_index = 0
    state_start_index, state_end_index = None, None
    heights = []

    while not found:
        direction_index, curr_rock, highest_block = drop_new_rock(direction_index, rock_index, blocks, highest_block, highest_block_per_x)

        direction_modulo = direction_index % n
        rock_modulo = rock_index % ROCK_TYPES
        floor_heights = tuple([highest_block - highest_block_per_x[x] for x in range(WIDTH)])
        state = (direction_modulo, rock_modulo, floor_heights)
        heights.append(highest_block)
        for k, v in states.items():
            if state == v:
                state_start_index = k
                state_end_index = rock_index
                found = True
                states[rock_index] = state
                break

        states[rock_index] = state
        rock_index += 1

    # loop maths
    state_start = states[state_start_index]
    height_diff = heights[state_end_index] - heights[state_start_index]
    state_index_diff = state_end_index - state_start_index
    num_loops = (BIG_NUM_ROCKS - state_end_index) // state_index_diff
    highest_block += num_loops * height_diff
    highest_block_per_x = [highest_block - state_start[2][x] for x in range(WIDTH)]
    blocks = set(tuple([highest_block_per_x[x], x]) for x in range(WIDTH))
    rock_index_after_loop = rock_index + (num_loops * state_index_diff)

    # keep going from end of loop
    for rock_index in range(rock_index_after_loop, BIG_NUM_ROCKS):
        direction_index, curr_rock, highest_block = drop_new_rock(direction_index, rock_index, blocks, highest_block, None)

    return highest_block + 1  # 0 indexed


print("part1:", part1())
print("part2:", part2())
