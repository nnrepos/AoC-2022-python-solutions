from src.utils.utils import *

text = get_input(__file__)
ss = splitsplit(text)


def part1():
    curr_to_start_index = {}
    start_to_curr_index = {}
    nums_moved = []
    mx, mn = 0, 0
    for i, x in enumerate((text.splitlines())):
        num = int(x)
        mn = min(mn, num)
        mx = max(mx, num)
        start_to_curr_index[i] = i
        curr_to_start_index[i] = i
        nums_moved.append(num)

    n = len(start_to_curr_index)
    for start_index in range(n):
        curr_index = start_to_curr_index[start_index]
        num = nums_moved[curr_index]

        new_index = (curr_index + num)

        # do not jump over yourself (%n)
        new_index %= (n - 1)

        if new_index == 0:
            # this causes the order of the numbers in `nums_moved` to be indentical to the website's example.
            # part1 still works when this is commented out, because we only care about cyclic order.
            new_index = n - 1

        if curr_index < new_index:
            nums_moved = nums_moved[:curr_index] + nums_moved[curr_index + 1:new_index + 1] + [num] + nums_moved[new_index + 1:]
            for i in range(curr_index, new_index):
                curr_to_start_index[i] = curr_to_start_index[i + 1]
                start_to_curr_index[curr_to_start_index[i]] -= 1
            start_to_curr_index[start_index] = new_index
            curr_to_start_index[new_index] = start_index

        elif new_index < curr_index:
            nums_moved = nums_moved[:new_index] + [num] + nums_moved[new_index: curr_index] + nums_moved[curr_index + 1:]
            for i in range(curr_index, new_index, -1):
                curr_to_start_index[i] = curr_to_start_index[i - 1]
                start_to_curr_index[curr_to_start_index[i]] += 1
            start_to_curr_index[start_index] = new_index
            curr_to_start_index[new_index] = start_index
        # else nop

    zindex = -1
    for j, num2 in enumerate(nums_moved):
        if 0 == num2:
            zindex = j
            break
    assert zindex > -1

    offsets = (1000, 2000, 3000)
    total = sum(nums_moved[(zindex + i) % n] for i in offsets)

    return total


def part2():
    dkey = 811589153
    num_cycles = 10

    curr_to_start_index = {}
    start_to_curr_index = {}
    nums_moved = []
    mx, mn = 0, 0
    for i, x in enumerate((text.splitlines())):
        num = int(x) * dkey
        mn = min(mn, num)
        mx = max(mx, num)
        start_to_curr_index[i] = i
        curr_to_start_index[i] = i
        nums_moved.append(num)

    n = len(start_to_curr_index)

    for _ in range(num_cycles):
        for start_index in range(n):
            curr_index = start_to_curr_index[start_index]
            num = nums_moved[curr_index]

            new_index = (curr_index + num)

            # do not jump over yourself (%n)
            new_index %= (n - 1)

            if new_index == 0 and num != 0:
                # this causes the order of the numbers in `nums_moved` to be indentical to the website's example.
                # part2 still works when this is commented out, because we only care about cyclic order.
                new_index = n - 1

            if curr_index < new_index:
                nums_moved = nums_moved[:curr_index] + nums_moved[curr_index + 1:new_index + 1] + [num] + nums_moved[new_index + 1:]
                for i in range(curr_index, new_index):
                    curr_to_start_index[i] = curr_to_start_index[i + 1]
                    start_to_curr_index[curr_to_start_index[i]] -= 1
                start_to_curr_index[start_index] = new_index
                curr_to_start_index[new_index] = start_index

            elif new_index < curr_index:
                nums_moved = nums_moved[:new_index] + [num] + nums_moved[new_index: curr_index] + nums_moved[curr_index + 1:]
                for i in range(curr_index, new_index, -1):
                    curr_to_start_index[i] = curr_to_start_index[i - 1]
                    start_to_curr_index[curr_to_start_index[i]] += 1
                start_to_curr_index[start_index] = new_index
                curr_to_start_index[new_index] = start_index
            # else nop

    zindex = -1
    for j, num2 in enumerate(nums_moved):
        if 0 == num2:
            zindex = j
            break
    assert zindex > -1

    offsets = (1000, 2000, 3000)
    total = sum(nums_moved[(zindex + i) % n] for i in offsets)

    return total


print("part1:", part1())
print("part2 takes ~10 seconds...")
print("part2:", part2())
