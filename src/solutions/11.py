from src.utils.utils import *

text = get_input(__file__)
ss = splitsplit(text)


def part1():
    items = dict()
    operations = dict()
    tests = dict()
    trues = dict()
    falses = dict()
    for monkey in text.split('\n\n'):
        a, b, c, d, e, f = [x.strip() for x in monkey.splitlines()]
        m = int(a.split(' ')[1].split(':')[0])
        item0 = [int(x) for x in b.split(': ')[1].split(', ')]
        oper = c.split('= old ')[1].split(' ')
        if oper[1].isdigit():
            oper[1] = int(oper[1])
        test = int(d.split('by ')[1])
        tr = int(e.split('monkey ')[1])
        fa = int(f.split('monkey ')[1])

        items[m] = item0
        operations[m] = oper
        tests[m] = test
        trues[m] = tr
        falses[m] = fa
    num_monkeys = len(falses)

    rounds = [0 for _ in range(num_monkeys)]

    for r in range(20):
        for m in range(num_monkeys):
            while items[m]:
                rounds[m] += 1
                old = items[m].pop(0)
                symbol, amount = operations[m]
                if amount == 'old':
                    amount = old
                if symbol == '*':
                    old *= amount
                else:
                    assert symbol == '+'
                    old += amount
                old //= 3

                if old % tests[m] == 0:
                    items[trues[m]].append(old)
                else:
                    items[falses[m]].append(old)

    x = max(rounds)
    rounds.pop(rounds.index(x))
    y = max(rounds)
    return x * y


def part2():
    items = dict()
    operations = dict()
    tests = dict()
    trues = dict()
    falses = dict()
    for monkey in text.split('\n\n'):
        a, b, c, d, e, f = [x.strip() for x in monkey.splitlines()]
        m = int(a.split(' ')[1].split(':')[0])
        item0 = [int(x) for x in b.split(': ')[1].split(', ')]
        oper = c.split('= old ')[1].split(' ')
        if oper[1].isdigit():
            oper[1] = int(oper[1])
        test = int(d.split('by ')[1])
        tr = int(e.split('monkey ')[1])
        fa = int(f.split('monkey ')[1])

        items[m] = item0
        operations[m] = oper
        tests[m] = test
        trues[m] = tr
        falses[m] = fa
    num_monkeys = len(falses)
    modu = 1
    for test in tests.values():
        modu *= test

    rounds = [0 for _ in range(num_monkeys)]

    for r in range(10000):
        for m in range(num_monkeys):
            while items[m]:
                rounds[m] += 1
                old = items[m].pop(0)
                symbol, amount = operations[m]
                if amount == 'old':
                    amount = old
                if symbol == '*':
                    old *= amount
                else:
                    assert symbol == '+'
                    old += amount
                old %= modu
                if old % tests[m] == 0:
                    items[trues[m]].append(old)
                else:
                    items[falses[m]].append(old)

    x = max(rounds)
    rounds.pop(rounds.index(x))
    y = max(rounds)
    return x * y


print("part1:", part1())
print("part2:", part2())
