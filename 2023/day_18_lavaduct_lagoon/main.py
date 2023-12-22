import copy

import numpy as np
from rich.console import Console


def move(pointer, direction, steps=1):
    steps = int(steps)
    assert direction in "UDRL"
    if direction == "R":
        return [pointer[0], pointer[1] + steps]
    if direction == "L":
        return [pointer[0], pointer[1] - steps]
    if direction == "U":
        return [pointer[0] - steps, pointer[1]]
    if direction == "D":
        return [pointer[0] + steps, pointer[1]]


def dig(in_map):
    out = []
    for i in range(min([x[0] for x in in_map]), max([x[0] for x in in_map]) + 1):
        line = []
        for j in range(min([x[1] for x in in_map]), max([x[1] for x in in_map]) + 1):
            if (i, j) in in_map:
                line.append(1)
            else:
                line.append(0)
        out.append(line)
    return out


def fill(in_map):

    def get_type(dot_i, dot_j):  # 0 - vertical, 1 - horizontal, 2 - up, 3 - down
        if dot_i == 0:
            return 3
        if dot_i == len(in_map) - 1:
            return 2
        if in_map[dot_i - 1][dot_j] == 1 and in_map[dot_i + 1][dot_j] == 1:
            return 0
        if in_map[dot_i - 1][dot_j] == 0 and in_map[dot_i + 1][dot_j] == 0:
            return 1
        if in_map[dot_i - 1][dot_j] == 1 and in_map[dot_i + 1][dot_j] == 0:
            return 2
        if in_map[dot_i - 1][dot_j] == 0 and in_map[dot_i + 1][dot_j] == 1:
            return 3

    area = sum([sum(x) for x in in_map])
    new_map = copy.deepcopy(in_map)
    for i, row in enumerate(in_map):
        inside = False
        prev_dot = 0
        last_empty_start = None
        curr_type = 0
        for j, dot in enumerate(row):
            assert dot in (0, 1)
            if dot == 0:
                if prev_dot == 1:
                    last_empty_start = j
            else:
                if prev_dot == 0:
                    if inside:
                        for k in range(last_empty_start, j):
                            new_map[i][k] = 1
                    if get_type(i, j) == 0:
                        inside = inside is not True
                    else:
                        curr_type = get_type(i, j)
                else:
                    if get_type(i, j) != 1 and get_type(i, j) != curr_type:
                        inside = inside is not True
            prev_dot = dot
    return sum([sum(x) for x in new_map]), new_map


def draw(in_map):
    for i in in_map:
        print("".join(["#" if x else "." for x in i]))


def reader(hard_mode=False):
    pointer = [1, 1]
    yield pointer, 0
    with open("input.txt") as f:
        for line in f.readlines():
        # for line in TEST_INPUT.split("\n"):
            direction, steps, colour = line.strip().split()
            if hard_mode:
                colour = colour[2:-1]
                steps = int(colour[:-1], 16)
                r = {0: "R", 1: "D", 2: "L", 3: "U"}
                direction = r[int(colour[-1])]
            pointer = move(pointer, direction, steps)
            yield pointer, int(steps)


def main():
    x = []
    y = []
    p = 0.0
    for point, steps in reader(True):
        x.append(point[1])
        y.append(point[0])
        p += steps
    x = np.array(x, dtype=np.int64)
    y = np.array(y, dtype=np.int64)
    i = np.arange(len(x))
    area = np.abs(np.sum(x[i - 1] * y[i] - x[i] * y[i - 1]))
    print((area + p) // 2 + 1)


if __name__ == '__main__':
    TEST_INPUT = '''R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)'''

    OUT = []
    console = Console()
    main()
