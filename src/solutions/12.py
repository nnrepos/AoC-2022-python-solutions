from src.utils.utils import *

text = get_input(__file__)
ss = splitsplit(text)

grid = [[x for x in line] for line in text.splitlines()]
nrow = len(grid)
ncol = len(grid[0])
dists = None


def get_unvisited_nei(coords, dists, grid):
    ret = []
    row, col = coords
    myletter = grid[row][col]
    for drow, dcol in ADJ:
        srow, scol = row + drow, col + dcol
        if srow in range(nrow) and scol in range(ncol):
            if (dists[(srow, scol)]) >= UNVISITED:
                hisletter = grid[srow][scol]
                if (ord(hisletter) <= ord(myletter) + 1) or myletter == 'S' or hisletter == 'E':
                    ret.append((srow, scol))
    return ret


def part1():
    global dists
    dists = {(i, j): UNVISITED for i, line in enumerate(text.splitlines()) for j, _ in enumerate(line)}
    start, end = None, None
    for row in range(nrow):
        for col in range(ncol):
            if grid[row][col] == 'S':
                start = (row, col)
            if grid[row][col] == 'E':
                end = (row, col)
    bfs(start, grid, dists, get_unvisited_nei)

    return dists[(end[0], end[1])]


def part2():
    global dists
    dists = {(i, j): UNVISITED for i, line in enumerate(text.splitlines()) for j, _ in enumerate(line)}

    end = None
    As = set()
    for row in range(nrow):
        for col in range(ncol):
            if grid[row][col] == 'S':
                As.add((row, col))
            if grid[row][col] == 'E':
                end = (row, col)
            if grid[row][col] == 'a':
                As.add((row, col))

    bfs(As, grid, dists, get_unvisited_nei)

    return dists[(end[0], end[1])]


print("part1:", part1())
print("part2:", part2())
