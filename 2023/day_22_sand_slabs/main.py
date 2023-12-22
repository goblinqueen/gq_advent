from intersect import doIntersect


class Point:
    x = None
    y = None
    z = None

    def __init__(self, x, y, z=None):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"p({self.x}, {self.y}, {self.z})"


class Brick:
    p1 = Point(0, 0)
    p2 = Point(0, 1)
    name = None

    def __init__(self, p1, p2):
        global USED
        self.p1 = p1
        self.p2 = p2
        name = 65
        while name in USED:
            name += 1
        self.name = name
        USED.add(name)

    def __getitem__(self, item):
        if item == 0:
            return self.p1
        if item == 1:
            return self.p2
        raise IndexError

    def __repr__(self):
        return f"[{self.p1}, {self.p2}]"


def get_above(p1, p2, lvl):
    return count_bricks(p1, p2, lvl, 1)


def count_bricks(p1, p2, lvl, shift):
    if lvl + shift not in LEVELS:
        return []
    else:
        return [t for t in LEVELS[lvl + shift] if doIntersect(p1, p2, t[0], t[1])]


def get_below(p1, p2, lvl):
    return count_bricks(p1, p2, lvl, -1)


def can_remove(p1, p2, lvl):
    for brick_above in get_above(p1, p2, lvl):
        if len(get_below(*brick_above, lvl + 1)) < 2:
            return False
    return True


def main():
    global LEVELS
    global IGNORE
    global USED
    bricks = []
    with open("input.txt") as f:
        for line in f.readlines():
        # for line in TEST_INPUT.split("\n"):
            line = line.strip()
            pos_1, pos_2 = line.split("~")
            brick = Brick(Point(*[int(t) for t in pos_1.split(",")]), Point(*[int(t) for t in pos_2.split(",")]))
            bricks.append(brick)

    bricks.sort(key=lambda x: min(x.p1.z, x.p1.z))
    for brick in bricks:
        z = fall(brick)
        if brick.p1.z == brick.p2.z:
            LEVELS[z] = LEVELS.get(z, [])
            LEVELS[z].append(brick)
        else:  # we have a tall brick
            assert brick.p1.x == brick.p2.x and brick.p1.y == brick.p2.y
            top = max(brick[0].z, brick[1].z)
            bot = min(brick[0].z, brick[1].z)
            top = top - (bot - z)
            LEVELS[top] = LEVELS.get(top, [])
            LEVELS[top].append(brick)
            LEVELS[z] = LEVELS.get(z, [])
            LEVELS[z].append(brick)
            IGNORE.append(brick)

    # print(LEVELS)

    out = set()
    for lvl, bricks in LEVELS.items():
        for brick in bricks:
            # print(lvl, chr(brick.name), can_remove(*brick, lvl))
            # print(get_below(Point(0,0), Point(0,2), 3))
            if can_remove(*brick, lvl):
                out.add(brick.name)
    print(len(out))
    # print(LEVELS)


def fall(brick):
    z = min(brick.p1.z, brick.p2.z)
    if LEVELS.get(z, []):
        assert not max([doIntersect(brick.p1, brick.p2, t.p1, t.p2) for t in LEVELS.get(z, [])])
    supported = False
    while not supported:
        if z == 1:
            supported = True
        else:
            below = LEVELS.get(z - 1, [])
            if below:
                supported = max([doIntersect(brick.p1, brick.p2, t.p1, t.p2) for t in below])
        z -= 1
    z = z + 1
    return z


if __name__ == '__main__':
    TEST_INPUT = '''1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9'''

    LEVELS = {1: []}
    IGNORE = []
    USED = set()

    main()
