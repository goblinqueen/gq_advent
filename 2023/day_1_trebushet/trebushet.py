DIGITS = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def is_nth_letter(char, n, subset):
    out = [], []  # words where it's the nth letter, words where it's also the last letter
    for i in subset:
        if len(DIGITS[i]) >= n and DIGITS[i][n-1] == char:
            out[0].append(i)
            if n == len(DIGITS[i]):
                out[1].append(i)
    return out


def find_numbers(s):
    out = []  # We can just calculate the result on the go, but this list is very small, so storing is fine
    candidates = {}
    for char in s:
        try:
            out.append(int(char))
            continue
        except ValueError:
            pass
        # move an index up
        prev_candidates = candidates.copy()
        candidates = {1: is_nth_letter(char, 1, range(1, 10))[0]}  # there are no 1-letter digit names
        # process candidates from previous runs
        for n in prev_candidates:
            lookup = is_nth_letter(char, n+1, prev_candidates[n])
            for res in lookup[1]:
                out.append(res)
            if lookup[0]:
                candidates[n+1] = lookup[0]
    return out


def main():
    with open("input.txt") as f:
        total = 0
        for line in f.readlines():
            nums = find_numbers(line)
            total += nums[0]*10 + nums[-1]
        print(total)


if __name__ == '__main__':
    main()
    # print(find_numbers("rkzlnmzgnk91zckqprrptnthreefourtwo"))
    # print(is_nth_letter("o", 3, [2, 3]))

