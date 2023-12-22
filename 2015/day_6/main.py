def light(start, end, op):
    assert op in ["off", "on", "toggle"]
    global FRAME
    i_start, j_start = [int(x) for x in start.split(",")]
    i_end, j_end = [int(x) for x in end.split(",")]
    for i in range(i_start, i_end + 1):
        for j in range(j_start, j_end + 1):
            if op == "on":
                FRAME[i][j] = FRAME[i][j] + 1
            elif op == 'off':
                FRAME[i][j] = max(FRAME[i][j]-1, 0)
            elif op == "toggle":
                # FRAME[i][j] = 0 if FRAME[i][j] == 1 else 1
                FRAME[i][j] = FRAME[i][j] + 2


def main():
    with open("input.txt") as f:
        for line in f.readlines():
        # for line in ["turn on 0,0 through 999,999"]:
            line = line.strip().split()
            assert line[-2] == "through"
            if len(line) == 5:
                op = line[1]
            else:
                op = line[0]
            start, end = line[-3], line[-1]
            light(start, end, op)


def draw():
    for line in FRAME:
        print(line)


if __name__ == '__main__':
    FRAME = [[0 for col in range(1000)] for row in range(1000)]
    main()
    print(sum([sum(x) for x in FRAME]))
    # draw()
