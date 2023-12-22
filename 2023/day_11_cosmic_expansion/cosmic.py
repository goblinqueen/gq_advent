from itertools import combinations

import numpy as np


def main():
    space = np.array(SPACE)

    empty_0 = []
    empty_1 = []

    for i in range(space.shape[0]):
        if sum(space[i]) == 0:
            empty_0.append(i)

    galaxies = []
    for i in range(space.shape[1]):
        if sum(space[:, i]) == 0:
            empty_1.append(i)
        else:
            for k in range(len(space[:, i])):
                if space[k][i]:
                    galaxies.append(np.array([k, i], dtype=np.float64))

    res = 0

    for g1, g2 in combinations(galaxies, 2):
        e_0 = len([x for x in list(empty_0) if min([g1[0], g2[0]]) < x < max([g1[0], g2[0]])])
        e_1 = len([x for x in list(empty_1) if min([g1[1], g2[1]]) < x < max([g1[1], g2[1]])])
        res += sum(abs(g1 - g2)) + e_0 * EXPAND + e_1 * EXPAND
    print(res)


if __name__ == "__main__":

    TEST_INPUT = '''
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
'''
    EXPAND = 1000000 - 1
    with open("input.txt") as f:
        SPACE = []
        for line in f.readlines():
        # for line in TEST_INPUT.split("\n"):
            if not line:
                continue
            line = line.strip()
            out = []
            for char in line:
                assert char in ".#"
                out.append(int(char == "#"))
            SPACE.append(out)

        main()
