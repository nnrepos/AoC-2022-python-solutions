from src.utils.utils import *
import json

text = get_input(__file__)
ss = splitsplit(text)


def recursive_cmp(left, right):
    if type(left) == int and type(right) == int:
        if left > right:
            return 'left'
        elif right > left:
            return 'right'
        else:
            return 'equal'

    if type(left) == int:
        left = [left]
    elif type(right) == int:
        right = [right]

    if not left and not right:
        return 'equal'
    if not left:
        return "right"
    if not right:
        return "left"

    # iterate lists
    minlen = min(len(right), len(left))
    for i in range(minlen):
        result = recursive_cmp(left[i], right[i])
        if result == 'right':
            return 'right'
        if result == 'left':
            return 'left'

    # compare lengths
    if len(right) > len(left):
        return 'right'
    elif len(left) > len(right):
        return 'left'
    else:
        return 'equal'


def part1():
    packet_pairs = [[json.loads(pair.splitlines()[0]), json.loads(pair.splitlines()[1])] for pair in text.split('\n\n')]
    total = 0
    for p in range(len(packet_pairs)):
        greater = recursive_cmp(packet_pairs[p][0], packet_pairs[p][1])
        if greater == 'right':
            total += p + 1
    return total


def part2():
    packets = [json.loads(x) for pair in text.split('\n\n') for x in pair.splitlines()] + [[[2]], [[6]]]
    num_packets = len(packets)

    # bubble sort
    for i in range(num_packets):
        for p in range(num_packets - 1):
            if recursive_cmp(packets[p], packets[p + 1]) == 'left':
                packets[p], packets[p + 1] = packets[p + 1], packets[p]

    first, second = 0, 0
    for p in range(num_packets):
        if packets[p] == [[2]]:
            first = p + 1
        if packets[p] == [[6]]:
            second = p + 1
    assert first < second
    total = first * second
    return total


print("part1:", part1())
print("part2:", part2())
