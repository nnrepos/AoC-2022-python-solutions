from src.utils.utils import *

text = get_input(__file__)
ss = splitsplit(text, None)
deqs = None

def init_deqs():
    global deqs
    deqs = [deque() for _ in range(10)]
    deqs[1].appendleft('F')
    deqs[1].appendleft('H')
    deqs[1].appendleft('M')
    deqs[1].appendleft('T')
    deqs[1].appendleft('V')
    deqs[1].appendleft('L')
    deqs[1].appendleft('D')
    deqs[2].appendleft('P')
    deqs[2].appendleft('N')
    deqs[2].appendleft('T')
    deqs[2].appendleft('C')
    deqs[2].appendleft('J')
    deqs[2].appendleft('G')
    deqs[2].appendleft('Q')
    deqs[2].appendleft('H')
    deqs[3].appendleft('H')
    deqs[3].appendleft('P')
    deqs[3].appendleft('M')
    deqs[3].appendleft('D')
    deqs[3].appendleft('S')
    deqs[3].appendleft('R')
    deqs[4].appendleft('F')
    deqs[4].appendleft('V')
    deqs[4].appendleft('B')
    deqs[4].appendleft('L')
    deqs[5].appendleft('Q')
    deqs[5].appendleft('L')
    deqs[5].appendleft('G')
    deqs[5].appendleft('H')
    deqs[5].appendleft('N')
    deqs[6].appendleft('P')
    deqs[6].appendleft('M')
    deqs[6].appendleft('R')
    deqs[6].appendleft('G')
    deqs[6].appendleft('D')
    deqs[6].appendleft('B')
    deqs[6].appendleft('W')
    deqs[7].appendleft('Q')
    deqs[7].appendleft('L')
    deqs[7].appendleft('H')
    deqs[7].appendleft('C')
    deqs[7].appendleft('R')
    deqs[7].appendleft('N')
    deqs[7].appendleft('M')
    deqs[7].appendleft('G')
    deqs[8].appendleft('W')
    deqs[8].appendleft('L')
    deqs[8].appendleft('C')
    deqs[9].appendleft('T')
    deqs[9].appendleft('M')
    deqs[9].appendleft('Z')
    deqs[9].appendleft('J')
    deqs[9].appendleft('Q')
    deqs[9].appendleft('L')
    deqs[9].appendleft('D')
    deqs[9].appendleft('R')


def part1():
    init_deqs()
    for line in text.splitlines()[10:]:
        _, bb, _, dd, _, ff = line.split()
        num = int(bb)
        src = int(dd)
        dest = int(ff)
        for i in range(num):
            deqs[dest].append(deqs[src].pop())

    ans = ''
    for i in range(1, 10):
        ans += deqs[i].pop()

    return ans


def part2():
    init_deqs()
    for line in text.splitlines()[10:]:
        _, bb, _, dd, _, ff = line.split()
        num = int(bb)
        src = int(dd)
        dest = int(ff)

        curr = []
        for i in range(num):
            curr.append(deqs[src].pop())
        for i in range(num):
            deqs[dest].append(curr.pop())

    ans = ''
    for i in range(1, 10):
        ans += deqs[i].pop()

    return ans


print("part1:", part1())
print("part2:", part2())
