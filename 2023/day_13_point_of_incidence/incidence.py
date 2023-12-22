import copy


def pos(line):
    out = []
    for i in range(1, len(line)):
        if line[max(0, 2*i - len(line)):i] == line[i:2*i][::-1]:
            out.append(i)
    return out


def check_cube(cube):
    curr_pos = None
    for line in cube:
        if curr_pos is None:
            curr_pos = pos(line)
        else:
            curr_pos = [x for x in pos(line) if x in curr_pos]
    return curr_pos


def t(x):
    return list(map(list, zip(*x)))


def main():
    with open("input.txt") as f:

        def check(in_cube):
            v = check_cube(in_cube)
            h = check_cube(t(in_cube))
            return h, v

        def flush(cube):
            initial_res = check(cube)
            for y, l in enumerate(cube):
                for x, ch in enumerate(cube[y]):
                    new_cube = copy.deepcopy(cube)
                    if cube[y][x] == 1:
                        new_cube[y][x] = 0
                    else:
                        new_cube[y][x] = 1
                    res = check(new_cube)
                    if res != ([], []) and res != initial_res:
                        h = [j for j in res[0] if j not in initial_res[0]]
                        v = [j for j in res[1] if j not in initial_res[1]]
                        assert len(h + v) == 1
                        return ([100 * j for j in h] + v)[0]

        curr_cube = []
        out = 0
        for line in f.readlines():
        # for line in TEST_INPUT.split("\n"):
            line = line.strip()
            if line == "":
                out += flush(curr_cube)
                curr_cube = []
                continue

            assert len(line) == len([x for x in line if x in ".#"])
            line = [int(ch == '#') for ch in line]
            curr_cube.append(line)
        out += flush(curr_cube)

        print(out)





if __name__ == '__main__':
    TEST_INPUT = '''#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#'''

    main()
