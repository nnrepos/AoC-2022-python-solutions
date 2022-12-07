from src.utils.utils import *

text = get_input(__file__)


def part1():
    dir_hierarchy = []
    curr_dir_name = ''
    sizes = d()
    for i, line in enumerate(text.splitlines()):
        line = line.strip()
        if line == '$ cd ..':
            if len(dir_hierarchy) > 1:
                sizes[dir_hierarchy[-2]] += sizes[dir_hierarchy[-1]]
                curr_dir_name = dir_hierarchy[-2]
            dir_hierarchy.pop()
        elif line.startswith('$ cd'):
            target = line.split('$ cd ')[1]
            curr_dir_name += f'{target}/'
            dir_hierarchy.append(curr_dir_name)
        elif line.startswith('dir'):
            continue
        elif line.startswith('$ ls'):
            continue
        else:
            num, *other = line.split()
            assert num.isdigit(), "not a number"
            sizes[dir_hierarchy[-1]] += int(num)

    while dir_hierarchy:
        # go back up to root
        if len(dir_hierarchy) > 1:
            sizes[dir_hierarchy[-2]] += sizes[dir_hierarchy[-1]]
        dir_hierarchy.pop()

    total = 0
    for s in sizes.values():
        if s <= 100000:
            total += s
    return total


def part2():
    dir_hierarchy = []
    curr_dir_name = ''
    sizes = d()
    for i, line in enumerate(text.splitlines()):
        line = line.strip()
        if line == '$ cd ..':
            if len(dir_hierarchy) > 1:
                sizes[dir_hierarchy[-2]] += sizes[dir_hierarchy[-1]]
                curr_dir_name = dir_hierarchy[-2]
            dir_hierarchy.pop()
        elif line.startswith('$ cd'):
            target = line.split('$ cd ')[1]
            curr_dir_name += f'{target}/'
            dir_hierarchy.append(curr_dir_name)
        elif line.startswith('dir'):
            continue
        elif line.startswith('$ ls'):
            continue
        else:
            num, *other = line.split()
            assert num.isdigit(), "not a number"
            sizes[dir_hierarchy[-1]] += int(num)

    while dir_hierarchy:
        # go back up to root
        if len(dir_hierarchy) > 1:
            sizes[dir_hierarchy[-2]] += sizes[dir_hierarchy[-1]]
        dir_hierarchy.pop()

    curr_best_size = 9999999999999999
    free = 70_000_000 - sizes['//']
    optimal_size = 30_000_000 - free
    for s in sizes.values():
        if optimal_size <= s < curr_best_size:
            curr_best_size = s
    return curr_best_size


print("part1:", part1())
print("part2:", part2())
