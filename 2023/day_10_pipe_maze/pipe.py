import matplotlib.pyplot as plt


ELEMENTS = {
    "|": [(0, -1), (0, 1)],  # | is a vertical pipe connecting north and south.
    "-": [(1, 0), (-1, 0)],  # - is a horizontal pipe connecting east and west.
    "L": [(0, -1), (1, 0)],    # L is a 90-degree bend connecting north and east.
    "J": [(0, -1), (-1, 0)],    # J is a 90-degree bend connecting north and west.
    "7": [(0, 1), (-1, 0)],    # 7 is a 90-degree bend connecting south and west.
    "F": [(0, 1), (1, 0)],    # F is a 90-degree bend connecting south and east.
    "S": []  # S is the starting position of the animal
    # . is ground; there is no pipe in this tile.
}


def c(x, y):
    return MAP[y][x]


def get_pipes_around(in_x, in_y):
    out = []
    mouse_value = []
    if c(in_x, in_y) == "S":
        for j_x, j_y in [(x, y) for x in [-1, 0, 1] for y in [-1, 0, 1] if (x, y) != (0, 0)]:
            if in_x + j_x < 0 or in_y + j_y < 0:
                continue
            if c(in_x + j_x, in_y + j_y) in ELEMENTS:
                if (in_x, in_y) in get_pipes_around(in_x + j_x, in_y + j_y):
                    out.append((in_x + j_x, in_y + j_y))
                    mouse_value.append((j_x, j_y))
        assert len(out) == 2
        print(f"Mouse is {[e for e in ELEMENTS.keys() if ELEMENTS[e] == mouse_value]}")
        return out
    nbg = ELEMENTS.get(c(in_x, in_y))
    for x, y in nbg:
        try:
            if c(in_x + x, in_y + y) in ELEMENTS:
                out.append((in_x + x, in_y + y))
        except IndexError:
            continue
    assert len(out) < 3
    return out


def get_start():
    for y in range(len(MAP)):
        for x in range(len(MAP[y])):
            if MAP[y][x] == "S":
                return x, y


def main():
    curr_x, curr_y = START

    pointer_1, pointer_2 = get_pipes_around(curr_x, curr_y)
    prev_1, prev_2 = START, START
    i = 0

    pipes_in_loop = [START]

    while pointer_1 != pointer_2:
        pipes_in_loop.append(pointer_1)
        pipes_in_loop.append(pointer_2)
        i += 1
        new_pointer_1 = [x for x in get_pipes_around(*pointer_1) if x != prev_1][0]
        new_pointer_2 = [x for x in get_pipes_around(*pointer_2) if x != prev_2][0]
        plt.plot([prev_1[0], pointer_1[0]], [prev_1[1], pointer_1[1]], color='red')
        plt.plot([prev_2[0], pointer_2[0]], [prev_2[1], pointer_2[1]], color='blue')
        prev_1, prev_2 = pointer_1, pointer_2
        pointer_1, pointer_2 = new_pointer_1, new_pointer_2
    plt.plot([prev_1[0], pointer_1[0]], [prev_1[1], pointer_1[1]], color='red')
    plt.plot([prev_2[0], pointer_2[0]], [prev_2[1], pointer_2[1]], color='blue')

    pipes_in_loop.append(pointer_1)

    plt.scatter(*START, color='orange')

    inside_ct = 0
    mouse = "L"
    print(f"Using mouse = {mouse}")

    for y in range(len(MAP)):
        for x in range(len(MAP[y])):
            if (x, y) not in pipes_in_loop:
                intersects = 0
                prev_edge = None
                for nx in range(x + 1, len(MAP[y])):
                    p = c(nx, y)
                    if (nx, y) not in pipes_in_loop:
                        continue
                    if p == "S":
                        p = mouse
                    if p == "|":

                        intersects += 1
                    if p in "7J":
                        if ELEMENTS[p][0] != ELEMENTS.get(prev_edge, [None, None])[0]:
                            intersects += 1
                        prev_edge = None
                    if p in "LF":
                        prev_edge = p

                if intersects % 2:
                    plt.scatter(x, y, color='green')
                    inside_ct += 1
                else:
                    plt.scatter(x, y, color='gray')
    print(f"{i + 1} steps, {inside_ct} inside")
    plt.show()


if __name__ == "__main__":
    test_1 = '''
.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...'''

    test_2 = '''
...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
    '''

    test_3 = '''
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
'''

    # MAP = [x.strip() for x in test_3.split("\n") if x]
    MAP = []
    with open("input.txt") as f:
        for line in f.readlines():
            MAP.append(line.strip())

    START = get_start()
    main()
