from src.utils.utils import *

text = get_input(__file__)
ss = splitsplit(text)

TIME_LIMIT1 = 30
TIME_LIMIT2 = 26


def get_univisted_nei(curr, dists, valves):
    ret = []
    for nei in valves[curr][1]:
        if dists[nei] >= UNVISITED:
            ret.append(nei)

    return ret


def get_perm_value(full_perm, all_dists, valves, time_limit):
    total = 0
    flow = 0
    minute = 0
    curr = 'AA'
    for dest in full_perm:
        remaining = time_limit - minute
        # travel
        travel_time = all_dists[curr][dest]
        if travel_time <= remaining:
            minute += travel_time
            curr = dest
            total += flow * travel_time
        else:
            break

        remaining = time_limit - minute
        # open
        open_time = 1
        if open_time <= remaining:
            minute += open_time
            total += flow * open_time
            flow += valves[curr][0]
        else:
            break

    remaining = time_limit - minute
    total += flow * remaining

    return total


def part1():
    # parse
    valves = {}
    for line in text.splitlines():
        stuff = re.findall(r'([A-Z]+|\d+)', line[1:])
        src, rate, *dests = stuff
        valves[src] = [int(rate), dests]

    important_valves = {k for k, v in valves.items() if (v[0] > 0)}
    all_dists = {v: {} for v in valves}

    # create dists between all valves
    for src in valves:
        curr_dists = {v: UNVISITED for v in valves}
        bfs(src, valves, curr_dists, get_univisted_nei)
        all_dists[src] = curr_dists

    # find optimal valve permutation
    bestest = 0
    best_full_perm = []
    remaining_valves = [v for v in important_valves]
    lookahead = 3  # less than this fails, more than this is slower.

    while len(best_full_perm) < len(important_valves):
        curr_best = 0
        best_perm = None
        perms = list(permutations(remaining_valves, min(lookahead, len(remaining_valves))))
        for perm in perms:
            full_perm = best_full_perm + list(perm)
            total = get_perm_value(full_perm, all_dists, valves, TIME_LIMIT1)

            if total > curr_best:
                # print("found new best:", total, full_perm)
                curr_best = total
                bestest = curr_best
                best_perm = perm

        best_full_perm.append(best_perm[0])
        remaining_valves.remove(best_perm[0])

    return bestest


def part2():
    # parse
    valves = {}
    for line in text.splitlines():
        stuff = re.findall(r'([A-Z]+|\d+)', line[1:])
        src, rate, *dests = stuff
        valves[src] = [int(rate), dests]

    important_valves = {k for k, v in valves.items() if (v[0] > 0)}
    all_dists = {v: {} for v in valves}

    # create dists between all valves
    for src in valves:
        curr_dists = {v: UNVISITED for v in valves}
        bfs(src, valves, curr_dists, get_univisted_nei)
        all_dists[src] = curr_dists

    # find optimal valve permutation
    bestest = 0
    best_full_perm_me = []
    best_full_perm_elephant = []
    remaining_valves = [v for v in important_valves]
    lookahead = 5  # less than this fails, more than this is slower.

    while (len(best_full_perm_me) + len(best_full_perm_elephant)) < len(important_valves):
        curr_best = 0
        best_perm_me = None
        best_perm_elephant = None
        perms = list(permutations(remaining_valves, min(lookahead, len(remaining_valves))))
        for perm_both in perms:
            for my_len in range(len(perm_both)):
                perm_me = perm_both[:my_len]
                perm_elephant = perm_both[my_len:]
                full_perm_me = best_full_perm_me + list(perm_me)
                total_me = get_perm_value(full_perm_me, all_dists, valves, TIME_LIMIT2)
                full_perm_elephant = best_full_perm_elephant + list(perm_elephant)
                total_elephant = get_perm_value(full_perm_elephant, all_dists, valves, TIME_LIMIT2)
                total = total_me + total_elephant

                if total > curr_best:
                    # print("found new best:", total, f'{full_perm_me=}, {full_perm_elephant=}')
                    curr_best = total
                    bestest = curr_best
                    best_perm_me = perm_me
                    best_perm_elephant = perm_elephant

        if len(best_perm_me) > 0:
            best_full_perm_me.append(best_perm_me[0])
            remaining_valves.remove(best_perm_me[0])
        else:
            assert len(best_perm_elephant) > 0
            best_full_perm_elephant.append(best_perm_elephant[0])
            remaining_valves.remove(best_perm_elephant[0])

    return bestest


print("part1:", part1())
print('part 2 takes ~10 sec:')
print("part2:", part2())
