from src.utils.utils import *

text = get_input(__file__)


def part1():
    grid = [[int(x) for x in line] for line in text.splitlines()]
    num_rows = len(grid)
    num_cols = len(grid[0])
    dd = dict()
    
    for i in range(num_rows):
        for j in range(num_cols):
            dd[(i, j)] = False

    # from above
    for j in range(num_cols):
        curr_height = -1
        for i in range(num_rows):
            curr_tree = grid[i][j]
            if curr_tree > curr_height:
                curr_height = curr_tree
                dd[(i, j)] = True

    # from below
    for j in range(num_cols):
        curr_height = -1
        for i in range(num_rows - 1, -1, -1):
            curr_tree = grid[i][j]
            if curr_tree > curr_height:
                curr_height = curr_tree
                dd[(i, j)] = True

    # from right
    for i in range(num_rows):
        curr_height = -1
        for j in range(num_cols - 1, -1, -1):
            curr_tree = grid[i][j]
            if curr_tree > curr_height:
                curr_height = curr_tree
                dd[(i, j)] = True

    # from left
    for i in range(num_rows):
        curr_height = -1
        for j in range(num_cols):
            curr_tree = grid[i][j]
            if curr_tree > curr_height:
                curr_height = curr_tree
                dd[(i, j)] = True

    visible = sum(dd.values())
    return visible


def part2():
    # bruteforce
    grid = [[int(x) for x in line] for line in text.splitlines()]
    num_rows = len(grid)
    num_cols = len(grid[0])
    dd = dict()
    for i in range(num_rows):
        for j in range(num_cols):
            dd[(i, j)] = 0

    for my_row in range(num_rows):
        for my_col in range(num_cols):
            my_score = 1
            my_height = grid[my_row][my_col]

            # down
            curr_count = 0
            for i in range(my_row + 1, num_rows):
                if grid[i][my_col] < my_height:
                    curr_count += 1
                else:
                    curr_count += 1
                    break
            my_score *= curr_count

            # up
            curr_count = 0
            for i in range(my_row - 1, -1, -1):
                if grid[i][my_col] < my_height:
                    curr_count += 1
                else:
                    curr_count += 1
                    break
            my_score *= curr_count

            # right
            curr_count = 0
            for j in range(my_col + 1, num_cols):
                if grid[my_row][j] < my_height:
                    curr_count += 1
                else:
                    curr_count += 1
                    break
            my_score *= curr_count

            # left
            curr_count = 0
            for j in range(my_col - 1, -1, -1):
                if grid[my_row][j] < my_height:
                    curr_count += 1
                else:
                    curr_count += 1
                    break
            my_score *= curr_count

            dd[(my_row, my_col)] = my_score

    visible = max(dd.values())
    return visible


print("part1:", part1())
print("part2:", part2())
