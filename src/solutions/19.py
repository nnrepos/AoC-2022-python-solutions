from src.utils.utils import *

text = get_input(__file__)

TIME_LIMIT1 = 24
TIME_LIMIT2 = 32
NUM_ROCKS = 4
GEODE_ROCK_INDEX = 3


def part1():
    total_quality = 0
    time_limit = TIME_LIMIT1
    ore_robot_max_minute = time_limit - 6
    clay_robot_max_minute = time_limit - 4
    obs_robot_max_minute = time_limit - 2
    num_bps = len(text.splitlines())
    
    for line in text.splitlines():
        # ore robot's ore req, clay robot's ore req, etc...
        curr_bp, ore_ore, clay_ore, obs_ore, obs_clay, geode_ore, geode_obs = ints(line)

        curr_states = set()
        # ore_rock, clay_rock, obs_rock, geode_rock, ore_robot, clay_robot, obs_robot, geode_robot
        start = (1, 0, 0, 0, 1, 0, 0, 0)
        curr_states.add(start)
        for minute in range(1, time_limit):
            next_states = set()
            for state in curr_states:
                ore_rock, clay_rock, obs_rock, geode_rock, ore_robot, clay_robot, obs_robot, geode_robot = state
                # wait
                next_states.add((ore_rock + ore_robot, clay_rock + clay_robot, obs_rock + obs_robot, geode_rock + geode_robot,
                                 ore_robot, clay_robot, obs_robot, geode_robot))
                # make ore robot
                if ore_rock >= ore_ore and minute < ore_robot_max_minute:
                    next_states.add((ore_rock + ore_robot - ore_ore, clay_rock + clay_robot, obs_rock + obs_robot, geode_rock + geode_robot,
                                     ore_robot + 1, clay_robot, obs_robot, geode_robot))
                # make clay robot
                if ore_rock >= clay_ore and minute < clay_robot_max_minute:
                    next_states.add((ore_rock + ore_robot - clay_ore, clay_rock + clay_robot, obs_rock + obs_robot, geode_rock + geode_robot,
                                     ore_robot, clay_robot + 1, obs_robot, geode_robot))
                # make obs robot
                if ore_rock >= obs_ore and clay_rock >= obs_clay and minute < obs_robot_max_minute:
                    next_states.add((ore_rock + ore_robot - obs_ore, clay_rock + clay_robot - obs_clay, obs_rock + obs_robot, geode_rock + geode_robot,
                                     ore_robot, clay_robot, obs_robot + 1, geode_robot))
                # make geode robot
                if ore_rock >= geode_ore and obs_rock >= geode_obs:
                    next_states.add((ore_rock + ore_robot - geode_ore, clay_rock + clay_robot, obs_rock + obs_robot - geode_obs, geode_rock + geode_robot,
                                     ore_robot, clay_robot, obs_robot, geode_robot + 1))

            curr_states = next_states

        best_geodes = max(state[GEODE_ROCK_INDEX] for state in curr_states)
        curr_quality = curr_bp * best_geodes
        total_quality += curr_quality
        print(f'{curr_bp=}/{num_bps}, {curr_quality=}')

    return total_quality


def part2():
    first_bps = text.splitlines()[:3]
    num_bps = len(first_bps)
    total_quality = 1
    time_limit = TIME_LIMIT2
    ore_robot_max_minute = time_limit - 6
    clay_robot_max_minute = time_limit - 4
    obs_robot_max_minute = time_limit - 2

    for line in first_bps:
        # ore robot's ore req, clay robot's ore req, etc...
        curr_bp, ore_ore, clay_ore, obs_ore, obs_clay, geode_ore, geode_obs = ints(line)
        max_ore_needed = max(ore_ore, clay_ore, obs_ore)
        max_clay_needed = obs_clay
        max_obs_needed = geode_obs

        curr_states = set()
        # ore_rock, clay_rock, obs_rock, geode_rock, ore_robot, clay_robot, obs_robot, geode_robot
        start = (1, 0, 0, 0, 1, 0, 0, 0)
        curr_states.add(start)
        for minute in range(1, time_limit):
            next_states = set()
            for state in curr_states:
                ore_rock, clay_rock, obs_rock, geode_rock, ore_robot, clay_robot, obs_robot, geode_robot = state
                # wait
                next_states.add((ore_rock + ore_robot, clay_rock + clay_robot, obs_rock + obs_robot, geode_rock + geode_robot,
                                 ore_robot, clay_robot, obs_robot, geode_robot))
                # make ore robot
                if ore_rock >= ore_ore and minute < ore_robot_max_minute and ore_robot < max_ore_needed:
                    next_states.add((ore_rock + ore_robot - ore_ore, clay_rock + clay_robot, obs_rock + obs_robot, geode_rock + geode_robot,
                                     ore_robot + 1, clay_robot, obs_robot, geode_robot))
                # make clay robot
                if ore_rock >= clay_ore and minute < clay_robot_max_minute and clay_robot < max_clay_needed:
                    next_states.add((ore_rock + ore_robot - clay_ore, clay_rock + clay_robot, obs_rock + obs_robot, geode_rock + geode_robot,
                                     ore_robot, clay_robot + 1, obs_robot, geode_robot))
                # make obs robot
                if ore_rock >= obs_ore and clay_rock >= obs_clay and minute < obs_robot_max_minute and obs_robot < max_obs_needed:
                    next_states.add((ore_rock + ore_robot - obs_ore, clay_rock + clay_robot - obs_clay, obs_rock + obs_robot, geode_rock + geode_robot,
                                     ore_robot, clay_robot, obs_robot + 1, geode_robot))
                # make geode robot
                if ore_rock >= geode_ore and obs_rock >= geode_obs:
                    next_states.add((ore_rock + ore_robot - geode_ore, clay_rock + clay_robot, obs_rock + obs_robot - geode_obs, geode_rock + geode_robot,
                                     ore_robot, clay_robot, obs_robot, geode_robot + 1))

            curr_states = next_states

        best_geodes = max(state[GEODE_ROCK_INDEX] for state in curr_states)
        curr_quality = best_geodes
        total_quality *= curr_quality
        print(f'{curr_bp=}/{num_bps}, {curr_quality=}')

    return total_quality


print("part1 takes a couple minutes...")
print("part1:", part1())
print("part2 takes around 10 minutes...")
print("part2:", part2())
