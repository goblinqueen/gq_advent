class Crucible:

    _pos = None
    _str_c = None
    _shift = None
    _heat_loss = 0

    def is_valid(self):
        return self._pos[0] < len(MAP) and self._pos[1] < len(MAP[0]) and self not in VISITED

    def is_goal(self):
        return self._pos == [len(MAP)-1, len(MAP[0])-1]

    def __hash__(self):
        return hash(str([self._pos, self._shift, self._str_c]))

    def __init__(self, pos, prev_pos, str_c, heat_loss):
        self._pos = list(pos)
        self._shift = [prev_pos[x] - pos[x] for x in [0, 1]]
        assert sum([abs(x) for x in self._shift]) == 1
        self._str_c = str_c
        self._heat_loss = heat_loss

    def lose_heat(self):
        self._heat_loss += int(MAP[self._pos[0]][self._pos[1]])

    def __repr__(self):
        return f"{self._pos}{'*'*self._str_c} {self._heat_loss}"

    def get_next_pos(self):
        out = []
        # Straight on
        if self._str_c:
            new_pos = [self._pos[x] + self._shift[x]*-1 for x in [0, 1]]
            out.append(Crucible(new_pos, self._pos, self._str_c - 1, self._heat_loss))
        # Left and right
            if self._shift[0] == 0:
                out.append(Crucible([self._pos[0] + 1, self._pos[1]], self._pos, 3, self._heat_loss))
                out.append(Crucible([self._pos[0] - 1, self._pos[1]], self._pos, 3, self._heat_loss))
            else:
                out.append(Crucible([self._pos[0], self._pos[1] + 1], self._pos, 3, self._heat_loss))
                out.append(Crucible([self._pos[0], self._pos[1] - 1], self._pos, 3, self._heat_loss))

        out = [x for x in out if x.is_valid()]
        return out

    def run(self):
        global MIN
        global VISITED
        for crucible in self.get_next_pos():
            crucible.lose_heat()
            VISITED.add(crucible)
            if crucible.is_goal():
                yield crucible._heat_loss
                if MIN is None:
                    MIN = crucible._heat_loss
                else:
                    MIN = min(crucible._heat_loss, MIN)
            else:
                if MIN is None or crucible._heat_loss < MIN:
                    yield from crucible.run()


def main():
    c = Crucible((0, 0), (0, -1), 4, 0)
    for x in c.run():
        print(x, VISITED)
    print(MIN)


if __name__ == '__main__':

    TEST_INPUT = '''2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533'''

    MAP = []
    VISITED = set()

    MIN = None

    with open("input.txt") as f:
        # for line in f.readlines():
        for line in TEST_INPUT.split("\n"):
            line = line.strip()
            MAP.append(line)

    main()
