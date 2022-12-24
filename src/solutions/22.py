from src.utils.utils import *

text = get_input(__file__)

SIDE_SIZE = 50

grid_text, commands = text.split('\n\n')


def add_edges(curr_row, curr_col):
    if curr_col not in min_cols:
        min_cols[curr_col] = curr_row
    else:
        min_cols[curr_col] = min(min_cols[curr_col], curr_row)

    if curr_col not in max_cols:
        max_cols[curr_col] = curr_row
    else:
        max_cols[curr_col] = max(max_cols[curr_col], curr_row)

    if curr_row not in min_rows:
        min_rows[curr_row] = curr_col
    else:
        min_rows[curr_row] = min(min_rows[curr_row], curr_col)

    if curr_row not in max_rows:
        max_rows[curr_row] = curr_col
    else:
        max_rows[curr_row] = max(max_rows[curr_row], curr_col)


min_cols = {}
max_cols = {}
min_rows = {}
max_rows = {}

RIGHT = (0, 1)
DOWN = (1, 0)
LEFT = (0, -1)
UP = (-1, 0)
FACES = [RIGHT, DOWN, LEFT, UP]

FACE_DICT = {RIGHT: 0,
             DOWN: 1,
             LEFT: 2,
             UP: 3}

grid = {}

start_row = 0
start_col = 1000

for row_id, line in enumerate(grid_text.splitlines()):
    for col_id, symbol in enumerate(line):
        if (row_id == start_row) and symbol == '.':
            start_col = min(start_col, col_id)
        if symbol in ('.', '#'):
            grid[(row_id, col_id)] = symbol
            add_edges(curr_row=row_id, curr_col=col_id)

step_list = ints(commands)
rotations = list((x for x in re.findall(r'([A-Z]+)', commands)))


def wrap(pos, dir):
    """
    i shamelessly stole this method, too lazy to hard-code everything.
    this is how i see the map of cube sides:
     12
     3
    54
    6  
    """
    x, y = pos.real, pos.imag
    match dir, x//50, y//50:
        case  1j, 0, _: return complex(149-x, 99), -1j # 2R
        case  1j, 1, _: return complex( 49,x+ 50), -1  # 3R
        case  1j, 2, _: return complex(149-x,149), -1j # 4R
        case  1j, 3, _: return complex(149,x-100), -1  # 6R
        case -1j, 0, _: return complex(149-x,  0),  1j # 1L
        case -1j, 1, _: return complex(100,x- 50),  1  # 3L
        case -1j, 2, _: return complex(149-x, 50),  1j # 5L
        case -1j, 3, _: return complex(  0,x-100),  1  # 6L
        case  1 , _, 0: return complex(  0,y+100),  1  # 6D
        case  1 , _, 1: return complex(100+y, 49), -1j # 4D
        case  1 , _, 2: return complex(-50+y, 99), -1j # 2D
        case -1 , _, 0: return complex( 50+y, 50),  1j # 5U
        case -1 , _, 1: return complex(100+y,  0),  1j # 1U
        case -1 , _, 2: return complex(199,y-100), -1  # 2U


def get_next_tile2(curr_row, curr_col, delta):
    delta_row, delta_col = delta
    next_row = curr_row + delta_row
    next_col = curr_col + delta_col
    next_delta = delta

    if (next_row, next_col) not in grid:
        # tuple to complex
        pos = complex(curr_row, curr_col)
        face = None
        match delta:
            case (0, 1):
                face = 1j
            case (1, 0):
                face = 1
            case (0, -1):
                face = -1j
            case (-1, 0):
                face = -1

        next_pos, next_face = wrap(pos, face)
        next_row = round(next_pos.real)
        next_col = round(next_pos.imag)
        next_delta = None
        match next_face:
            case 1:
                next_delta = (1, 0)
            case 1j:
                next_delta = (0, 1)
            case -1:
                next_delta = (-1, 0)
            case -1j:
                next_delta = (0, -1)

    assert (next_row, next_col) in grid

    if grid[(next_row, next_col)] == '.':
        return next_row, next_col, next_delta
    else:
        assert grid[(next_row, next_col)] == '#'
        return None


def get_next_tile1(curr_row, curr_col, delta):
    delta_row, delta_col = delta
    next_row = curr_row + delta_row
    next_col = curr_col + delta_col

    if delta == RIGHT and next_col > max_rows[next_row]:
        next_col = min_rows[next_row]
    if delta == DOWN and next_row > max_cols[next_col]:
        next_row = min_cols[next_col]
    if delta == LEFT and next_col < min_rows[next_row]:
        next_col = max_rows[next_row]
    if delta == UP and next_row < min_cols[next_col]:
        next_row = max_cols[next_col]

    assert (next_row, next_col) in grid

    if grid[(next_row, next_col)] == '.':
        return next_row, next_col
    else:
        assert grid[(next_row, next_col)] == '#'
        return None


def part1():
    curr_face_id = 0
    curr_tile = (start_row, start_col)
    for i, step in enumerate(step_list):
        for s in range(step):
            next_tile = get_next_tile1(curr_tile[0], curr_tile[1], FACES[curr_face_id])
            if next_tile:
                curr_tile = next_tile
            else:
                break
        if i < len(rotations):
            rotation = rotations[i]
            if rotation == 'L':
                curr_face_id = (curr_face_id - 1) % len(FACES)
            else:
                assert rotation == 'R'
                curr_face_id = (curr_face_id + 1) % len(FACES)

    result = (1000 * (curr_tile[0] + 1)) + (4 * (curr_tile[1] + 1)) + curr_face_id

    return result


def part2():
    curr_face_id = 0
    curr_tile = (start_row, start_col)
    for i, step in enumerate(step_list):
        for s in range(step):
            next_stuff = get_next_tile2(curr_tile[0], curr_tile[1], FACES[curr_face_id])
            if next_stuff:
                next_row, next_col, next_delta = next_stuff
                curr_tile = (next_row, next_col)
                curr_face_id = FACE_DICT[next_delta]

            else:
                break
        if i < len(rotations):
            rotation = rotations[i]
            if rotation == 'L':
                curr_face_id = (curr_face_id - 1) % len(FACES)
            else:
                assert rotation == 'R'
                curr_face_id = (curr_face_id + 1) % len(FACES)

    result = (1000 * (curr_tile[0] + 1)) + (4 * (curr_tile[1] + 1)) + curr_face_id

    return result


print("part1:", part1())
print("part2:", part2())
