from src.utils.utils import *

text = get_input(__file__)
ss = splitsplit(text)

Y = 2_000_000


def is_illegal_spot(spotX, spotY, sensors, is_beacon_illegal=True) -> bool:
    is_illegal = False
    for s in sensors:
        sx, sy, bx, by = s
        if (bx, by) == (spotX, spotY):
            return is_beacon_illegal

        my_d = mandist(spotX, spotY, sx, sy)
        his_d = mandist(bx, by, sx, sy)
        if my_d <= his_d:
            is_illegal = True

    return is_illegal


def part1():
    sensors = []
    min_x, max_x = 1_000_000, 0
    for line in text.splitlines():
        x, y, xx, yy = ints(line)
        min_x = min(x, min_x)
        max_x = max(x, max_x)
        sensors.append((x, y, xx, yy))

    DELTA = 3_000_000
    illegal = 0
    start = min_x - DELTA
    end = max_x + DELTA
    for x in range(start, end):
        illegal += is_illegal_spot(x, Y, sensors, is_beacon_illegal=False)

    return illegal


def part2():
    # go around radii of sensors
    sensors = []
    for line in text.splitlines():
        x, y, xx, yy = ints(line)
        sensors.append((x, y, xx, yy))

    start = 0
    end = 4_000_000
    allowed = range(start, end)
    result = None
    for s in sensors:
        sx, sy, bx, by = s
        radius = mandist(bx, by, sx, sy) + 1

        # go left to top
        x, y = sx - radius, sy
        while x <= sx:
            if (x not in allowed) or (y not in allowed):
                x += 1
                y -= 1
                continue
            if not is_illegal_spot(x, y, sensors):
                result = (4_000_000 * x) + y
            x += 1
            y -= 1

        # go top to right
        x, y = sx, sy - radius
        while y <= sy:
            if (x not in allowed) or (y not in allowed):
                x += 1
                y += 1
                continue
            if not is_illegal_spot(x, y, sensors):
                result = (4_000_000 * x) + y
            x += 1
            y += 1

        # go right to bottom
        x, y = sx + radius, sy
        while x >= sx:
            if (x not in allowed) or (y not in allowed):
                x -= 1
                y += 1
                continue
            if not is_illegal_spot(x, y, sensors):
                result = (4_000_000 * x) + y
            x -= 1
            y += 1

        # go bottom to left
        x, y = sx, sy + radius
        while y >= sy:
            if (x not in allowed) or (y not in allowed):
                x -= 1
                y -= 1
                continue
            if not is_illegal_spot(x, y, sensors):
                result = (4_000_000 * x) + y
            x -= 1
            y -= 1

        if result is not None:
            return result

    return "fail"


print("part1:", part1())
print("part2:", part2())
