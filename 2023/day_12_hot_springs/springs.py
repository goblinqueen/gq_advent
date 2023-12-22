from itertools import combinations


# source: https://towardsdatascience.com/solving-nonograms-with-120-lines-of-code-a7c6e0f627e4
def get_combinations(groups: list, line_len: int) -> list:
    n_groups = len(groups)
    n_empty = line_len - sum(groups) - (len(groups) - 1)
    # print(f"Getting combinations for {n_groups + n_empty}, {n_groups}")
    opts = list(combinations(range(n_groups + n_empty), n_groups))
    ones = [[1] * x for x in groups]
    out = []
    # print(f"{len(opts)} combinations")
    for p in opts:
        selected = [-1] * (len(groups) + n_empty)
        ones_idx = 0
        for val in p:
            selected[val] = ones_idx
            ones_idx += 1
        res_opt = [ones[val] + [-1] if val > -1 else [-1] for val in selected]
        res_opt = [item for sublist in res_opt for item in sublist][:-1]
        out.append(res_opt)
    # print("Got combinations")
    return out


def decode_line(line: str) -> list:
    out = []
    for ch in line:
        assert ch in "?.#"
        if ch == "?":
            out.append(0)
        if ch == ".":
            out.append(-1)
        if ch == "#":
            out.append(1)
    return out


def main():
    res = 0
    with open("input.txt") as f:
        # for line in f.readlines():
        for line in TEST_INPUT.split("\n"):
            # for line in [".??..??...?##. 1,1,3"]:
            #     print(line)
            line, groups = line.strip().split(" ")
            groups = [int(x) for x in groups.split(",")]
            # line = (line + "?") * 5
            # groups = groups * 5
            comb = get_combinations(groups, len(line))
            line = decode_line(line)
            line_res = 0
            for group in comb:
                fits = True
                for i, line_val in enumerate(line):
                    if line_val != 0 and line_val != group[i]:
                        fits = False
                        break
                if fits:
                    line_res += 1
            res += line_res
        print(res)


if __name__ == '__main__':
    TEST_INPUT = '''???.### 1,1,3
    .??..??...?##. 1,1,3
    ?#?#?#?#?#?#?#? 1,3,1,6
    ????.#...#... 4,1,1
    ????.######..#####. 1,6,5
    ?###???????? 3,2,1'''

    main()

    # print(get_combinations([1, 1, 1], 7))
