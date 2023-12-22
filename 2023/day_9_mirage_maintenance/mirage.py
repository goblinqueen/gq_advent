INPUT_TEST = '''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45'''


def get_diffs(in_list):
    return [in_list[i + 1] - in_list[i] for i in range(len(in_list) - 1)]


def get_next_value(in_list):
    curr_list = in_list
    lasts = []
    firsts = []
    while set(curr_list) != {0}:
        lasts.append(curr_list[-1])
        firsts.append(curr_list[0])
        curr_list = get_diffs(curr_list)
    j = 0
    for i in reversed(range(len(firsts))):
        j = firsts[i] - j
    return j


def main():
    out = 0
    with open("input.txt") as f:
        for line in f.readlines():
        # for line in INPUT_TEST.split("\n"):
            line = [int(x) for x in line.strip().split(" ")]
            out += get_next_value(line)

        print(out)


if __name__ == "__main__":
    main()
