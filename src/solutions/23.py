from src.utils.utils import *

text = get_input(__file__)

N = -1
S = 1
W = -1j
E = 1j

NE = N + E
NW = N + W
SE = S + E
SW = S + W

CHECK_ORDER = ['north', 'south', 'west', 'east']

elves = None


def parse_elves():
    global elves
    elves = set()
    for i, line in enumerate(text.splitlines()):
        for j, c in enumerate(line):
            if c == '#':
                elves.add(i + j * 1j)


def get_proposed_location(elf, r):
    alone = True
    for adj in AROUND_COMPLEX:
        if elf + adj in elves:
            alone = False

    if alone:
        return elf

    for check in range(4):
        curr = CHECK_ORDER[(check + r) % 4]
        if curr == 'north':
            if (elf + NE not in elves) and (elf + N not in elves) and (elf + NW not in elves):
                return elf + N
        elif curr == 'south':
            if (elf + SE not in elves) and (elf + S not in elves) and (elf + SW not in elves):
                return elf + S
        elif curr == 'west':
            if (elf + NW not in elves) and (elf + W not in elves) and (elf + SW not in elves):
                return elf + W
        else:
            if (elf + NE not in elves) and (elf + E not in elves) and (elf + SE not in elves):
                return elf + E

    return elf


def part1():
    global elves
    rounds = 10
    parse_elves()
    for r in range(rounds):
        proposed_locations = {}
        prop_count = ddi()
        for elf in elves:
            prop = get_proposed_location(elf, r)
            proposed_locations[elf] = prop
            prop_count[prop] += 1

        removed = set()
        added = set()
        for elf in elves:
            if prop_count[proposed_locations[elf]] == 1:
                removed.add(elf)
                added.add(proposed_locations[elf])

        elves = (elves - removed)
        elves = elves.union(added)

    minrow = 1000
    maxrow = 0
    mincol = 1000
    maxcol = 0
    for elf in elves:
        minrow = int(min(elf.real, minrow))
        maxrow = int(max(elf.real, maxrow))
        mincol = int(min(elf.imag, mincol))
        maxcol = int(max(elf.imag, maxcol))
    area = (maxrow - minrow + 1) * (maxcol - mincol + 1)
    return area - len(elves)


def part2():
    global elves
    parse_elves()
    r = 0
    while True:
        proposed_locations = {}
        prop_count = ddi()
        for elf in elves:
            prop = get_proposed_location(elf, r)
            proposed_locations[elf] = prop
            prop_count[prop] += 1

        removed = set()
        added = set()
        for elf in elves:
            if prop_count[proposed_locations[elf]] == 1:
                removed.add(elf)
                added.add(proposed_locations[elf])

        if removed == added:
            break
        elves = (elves - removed)
        elves = elves.union(added)

        r += 1

    return r + 1


print("part1:", part1())
print("part2:", part2())
