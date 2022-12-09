from src.utils.utils import *

text = get_input(__file__)


def addd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def part1():
    curr_head = (0, 0)  # x,y
    curr_tail = (0, 0)
    tail_pos = set()
    tail_pos.add(curr_tail)
    dirmap = {'U': [0, 1], 'D': [0, -1], 'R': [1, 0], 'L': [-1, 0]}
    for direc, num in splitsplit(text):
        num = int(num)
        for _ in range(num):
            tail_offset = [0, 0]
            offset = dirmap[direc]
            curr_head = addd(curr_head, offset)
            if curr_head[0] == curr_tail[0]:
                if curr_head[1] - curr_tail[1] > 1:
                    tail_offset = [0, 1]
                elif curr_head[1] - curr_tail[1] < -1:
                    tail_offset = [0, -1]
            elif curr_head[1] == curr_tail[1]:
                if curr_head[0] - curr_tail[0] > 1:
                    tail_offset = [1, 0]
                elif curr_head[0] - curr_tail[0] < -1:
                    tail_offset = [-1, 0]
            else:
                absdist = abs(curr_head[1] - curr_tail[1]) + abs(curr_head[0] - curr_tail[0])
                if absdist > 2:
                    if curr_head[1] > curr_tail[1] and curr_head[0] > curr_tail[0]:
                        tail_offset = [1, 1]
                    elif curr_head[1] > curr_tail[1] and curr_head[0] < curr_tail[0]:
                        tail_offset = [-1, 1]
                    elif curr_head[1] < curr_tail[1] and curr_head[0] > curr_tail[0]:
                        tail_offset = [1, -1]
                    elif curr_head[1] < curr_tail[1] and curr_head[0] < curr_tail[0]:
                        tail_offset = [-1, -1]

            curr_tail = addd(curr_tail, tail_offset)
            tail_pos.add(curr_tail)

    return len(tail_pos)


def part2():
    curr_tails = [(0, 0) for _ in range(10)]
    tail_pos = set()
    tail_pos.add(curr_tails[9])
    dirmap = {'U': [0, 1], 'D': [0, -1], 'R': [1, 0], 'L': [-1, 0]}
    for direc, num in splitsplit(text):
        num = int(num)
        for _ in range(num):
            offset = dirmap[direc]
            curr_tails[0] = addd(curr_tails[0], offset)
            for i in range(1, 10):
                tail_offset = [0, 0]
                curr_head = curr_tails[i - 1]
                curr_tail = curr_tails[i]

                if curr_head[0] == curr_tail[0]:
                    if curr_head[1] - curr_tail[1] > 1:
                        tail_offset = [0, 1]
                    elif curr_head[1] - curr_tail[1] < -1:
                        tail_offset = [0, -1]
                elif curr_head[1] == curr_tail[1]:
                    if curr_head[0] - curr_tail[0] > 1:
                        tail_offset = [1, 0]
                    elif curr_head[0] - curr_tail[0] < -1:
                        tail_offset = [-1, 0]
                else:
                    absdist = abs(curr_head[1] - curr_tail[1]) + abs(curr_head[0] - curr_tail[0])
                    if absdist > 2:
                        if curr_head[1] > curr_tail[1] and curr_head[0] > curr_tail[0]:
                            tail_offset = [1, 1]
                        elif curr_head[1] > curr_tail[1] and curr_head[0] < curr_tail[0]:
                            tail_offset = [-1, 1]
                        elif curr_head[1] < curr_tail[1] and curr_head[0] > curr_tail[0]:
                            tail_offset = [1, -1]
                        elif curr_head[1] < curr_tail[1] and curr_head[0] < curr_tail[0]:
                            tail_offset = [-1, -1]
                curr_tail = addd(curr_tail, tail_offset)
                curr_tails[i] = curr_tail
                tail_pos.add(curr_tails[9])

    return len(tail_pos)


print("part1:", part1())
print("part2:", part2())
