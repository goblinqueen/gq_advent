def m(tile: tuple) -> str:
    return MAP[tile[0]][tile[1]]


def in_m(tile: tuple) -> bool:
    return -1 < tile[0] < len(MAP) and -1 < tile[1] < len(MAP[0])


def pass_tile(in_tile: tuple) -> list:
    prev_tile, curr_tile = in_tile
    global VISITED
    k = VISITED.get(curr_tile, [])
    if prev_tile in k:
        return []
    k.append(prev_tile)
    VISITED[curr_tile] = k
    shift = [prev_tile[x] - curr_tile[x] for x in [0, 1]]

    out = []

    if m(curr_tile) == ".":
        out.append((-1 * shift[0] + curr_tile[0], -1 * shift[1] + curr_tile[1]))

    elif m(curr_tile) == "\\":
        out.append((-1 * shift[1] + curr_tile[0], -1 * shift[0] + curr_tile[1]))

    elif m(curr_tile) == "/":
        out.append((shift[1] + curr_tile[0], shift[0] + curr_tile[1]))

    elif m(curr_tile) == "|":
        if shift[0] != 0:
            out.append((-1 * shift[0] + curr_tile[0], -1 * shift[1] + curr_tile[1]))
        else:
            out.append((curr_tile[0] + 1, curr_tile[1]))
            out.append((curr_tile[0] - 1, curr_tile[1]))

    elif m(curr_tile) == "-":
        if shift[1] != 0:
            out.append((-1 * shift[0] + curr_tile[0], -1 * shift[1] + curr_tile[1]))
        else:
            out.append((curr_tile[0], curr_tile[1] + 1))
            out.append((curr_tile[0], curr_tile[1] - 1))

    out = [(curr_tile, x) for x in out if in_m(x)]
    return out


def run(start_tile):
    global VISITED
    VISITED = {}
    tiles = [start_tile]
    while tiles:
        next_tiles = []
        for tile in tiles:
            next_tiles += pass_tile(tile)
        tiles = next_tiles

    for i in range(len(MAP)):
        out = ""
        for j in range(len(MAP[i])):
            if (i, j) in VISITED.keys():
                out += "#"
            else:
                out += "."
        # print(out)

    return len(VISITED.keys())


def main():
    max_power = 0

    # from the left
    for i in range(len(MAP)):
        p = run(((i, -1), (i, 0)))
        max_power = max(p, max_power)

    # from the right
    for i in range(len(MAP)):
        p = run(((i, len(MAP[0])), (i, len(MAP[0])-1)))
        max_power = max(p, max_power)

    # from the top
    for j in range(len(MAP[0])):
        p = run(((-1, j), (0, j)))
        max_power = max(p, max_power)

    # from the bottom
    for j in range(len(MAP[0])):
        p = run(((len(MAP[0]), j), (len(MAP[0]) - 1, j)))
        max_power = max(p, max_power)

    print(max_power)


if __name__ == '__main__':

    TEST_INPUT = '''.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|....'''

    MAP = []
    VISITED = {}

    with open("input.txt") as f:
        for line in f.readlines():
        # for line in TEST_INPUT.split("\n"):
            line = line.strip()
            MAP.append(line)

    main()
