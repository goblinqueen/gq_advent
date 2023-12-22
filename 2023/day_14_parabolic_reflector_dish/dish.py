from day_13_point_of_incidence.incidence import t


def tilt(data, way):
    out = []
    if way in "NS":
        data = t(data)
    for line in data:
        if way in "SE":
            line = line[::-1]
        out_line = ["."] * len(line)
        curr_stop = 0
        for i, ch in enumerate(line):
            if ch == "#":
                out_line[i] = "#"
                curr_stop = i + 1
            elif ch == "O":
                out_line[curr_stop] = "O"
                curr_stop += 1
        if way in "SE":
            out_line = out_line[::-1]
        out.append("".join(out_line))
    if way in "NS":
        out = t(out)
    return out


def run_cycle(data):
    for way in "NWSE":
        data = tilt(data, way)
    return data


def main():
    data = []
    with open("input.txt") as f:
        for line in f.readlines():
        # for line in TEST_INPUT.split("\n"):
            line = line.strip()
            data.append(line)

    cycles = {str(data): 0}
    cycle_len, cycle_start = None, None
    new_data = data
    for i in range(1, 1000000000):
        new_data = run_cycle(new_data)
        if str(new_data) not in cycles:
            cycles[str(new_data)] = i
        else:
            cycle_start = cycles[str(new_data)]
            cycle_len = i - cycles[str(new_data)]
            break
    runs = (1000000000 - 1 - cycle_start) % cycle_len + cycle_start + 1
    print(f"{runs} runs required")
    for i in range(runs):
        data = run_cycle(data)
    print(count_load(data))


def count_load(data):
    res = 0
    for i, line in enumerate(data):
        res += len([x for x in line if x == "O"]) * (len(data) - i)
    return res


if __name__ == '__main__':

    TEST_INPUT = '''O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....'''

    main()
