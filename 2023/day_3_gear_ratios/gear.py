SYMBOLS = ['#', '$', '%', '&', '*', '+', '-', '/', '=', '@']  # Generated from input
DIGITS = [str(i) for i in range(10)]


def has_adj_symbols(x, y):
    assert matrix[x][y] in DIGITS
    out = False
    stars = set()  # coordinates of adjacent stars
    for x_adj in range(-1, 2):
        for y_adj in range(-1, 2):
            try:
                if matrix[x + x_adj][y + y_adj] in SYMBOLS:
                    out = True
                    if matrix[x + x_adj][y + y_adj] == "*":
                        stars.add((x + x_adj, y + y_adj))
            except IndexError:
                pass
    return out, stars


def is_last_digit(x, y):
    assert matrix[x][y] in DIGITS
    try:
        return not matrix[x][y+1] in DIGITS
    except IndexError:
        return True  # Is last digit of line


def main():
    out_1 = 0
    cur_num = ""
    cur_ok = False
    curr_stars = set()
    stars = {}
    for x in range(len(matrix)):
        line = matrix[x]
        for y in range(len(line)):
            ch = matrix[x][y]
            if ch in DIGITS:
                cur_ok = cur_ok or has_adj_symbols(x, y)[0]
                curr_stars = curr_stars.union(has_adj_symbols(x, y)[1])
                if cur_num is not None:
                    cur_num += ch
                    if is_last_digit(x, y):
                        if cur_ok:
                            out_1 += int(cur_num)
                            for star in curr_stars:
                                stars[star] = stars.get(star, []) + [int(cur_num)]
                        cur_num = ""
                        cur_ok = False
                        curr_stars = set()
    out_2 = 0
    for star in stars:
        if len(stars[star]) == 2:
            out_2 += stars[star][0] * stars[star][1]
    print(out_1, out_2)


if __name__ == "__main__":
    with open("input.txt") as f:
        matrix = [line.strip() for line in f.readlines()]

    main()
