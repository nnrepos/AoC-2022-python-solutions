from src.utils.utils import *

text = get_input(__file__)
ss = splitsplit(text)

DELTA = 2
cubes = set()
min_x, max_x, min_y, max_y, min_z, max_z = 0, 0, 0, 0, 0, 0
for line in text.splitlines():
    xx, yy, zz = ints(line)
    cubes.add((xx, yy, zz))
    min_x = min(min_x, xx - DELTA)
    min_y = min(min_y, yy - DELTA)
    min_z = min(min_z, zz - DELTA)
    max_x = max(max_x, xx + DELTA)
    max_y = max(max_y, yy + DELTA)
    max_z = max(max_z, zz + DELTA)


def part1():
    total = 0
    for x, y, z in cubes:
        curr = 0
        for dx, dy, dz in ADJ3D:
            if (x + dx, y + dy, z + dz) not in cubes:
                curr += 1
        total += curr
    return total


def get_unvisited_nei(curr, dists, _):
    x, y, z = curr
    ret = []
    for dx, dy, dz in ADJ3D:
        new_x, new_y, new_z = (x + dx, y + dy, z + dz)
        new_coord = (new_x, new_y, new_z)
        if (new_coord in dists) and (new_coord not in cubes) and (dists[new_coord] >= INF_DIST):
            ret.append(new_coord)

    return ret


def part2():
    global cubes
    # add cubes which have inf dist from edges
    dists = {(x, y, z): INF_DIST for x in range(min_x, max_x) for y in range(min_y, max_y) for z in range(min_z, max_z)}
    bfs((min_x, min_y, min_z), None, dists, get_unvisited_nei)

    internal = set()
    for c in dists:
        if dists[c] >= INF_DIST:
            internal.add(c)

    total = 0
    for x, y, z in cubes:
        curr = 0
        for dx, dy, dz in ADJ3D:
            new_coord = (x + dx, y + dy, z + dz)
            if (new_coord not in cubes) and (new_coord not in internal):
                curr += 1
        total += curr
    return total


print("part1:", part1())
print("part2:", part2())
