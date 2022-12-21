from src.utils.utils import *

text = get_input(__file__)


def part1():
    monkeys = {}
    for line in text.splitlines():
        me, rest = line.split(':')
        monkeys[me] = rest.strip()

    unyelled = set()
    for m in monkeys:
        unyelled.add(m)

    to_remove = set()
    values = {}
    while len(unyelled) > 0:
        for un in unyelled:
            mon = monkeys[un]
            if mon.isdigit():
                values[un] = int(mon)
                to_remove.add(un)
            else:
                m1, s, m2 = mon.split()
                if m1.strip() in values and m2.strip() in values:
                    mm1 = values[m1]
                    mm2 = values[m2]
                    res = eval(f'{mm1} {s} {mm2}')
                    values[un] = res
                    to_remove.add(un)

        unyelled -= to_remove

    return int(values['root'])


def part2():
    # for this part, i first had to manually test whether increasing my number increases or decreases the value of each root monkey.
    monkeys = {}
    my_min = 0
    my_max = 1000000000000000
    while True:
        my_num = (my_min + my_max) // 2
        first_root_monkey, second_root_monkey = None, None
        for line in text.splitlines():
            me, rest = line.split(':')
            if me == 'root':
                first_root_monkey = (rest.strip().split()[0])
                second_root_monkey = (rest.strip().split()[2])
            elif me == 'humn':
                monkeys[me] = str(my_num)
            else:
                monkeys[me] = rest.strip()

        unyelled = set()
        for m in monkeys:
            unyelled.add(m)

        to_remove = set()
        values = {}
        while len(unyelled) > 0:
            for un in unyelled:
                mon = monkeys[un]
                if len(ints(mon)) > 0:
                    values[un] = int(mon)
                    to_remove.add(un)
                else:
                    m1, s, m2 = mon.split()
                    if m1.strip() in values and m2.strip() in values:
                        mm1 = values[m1]
                        mm2 = values[m2]
                        res = eval(f'{mm1} {s} {mm2}')
                        values[un] = res
                        to_remove.add(un)

            unyelled -= to_remove

        if values[first_root_monkey] < values[second_root_monkey]:
            my_max = my_num
        elif values[first_root_monkey] > values[second_root_monkey]:
            my_min = my_num
        else:
            return my_num


print("part1:", part1())
print("part2:", part2())
