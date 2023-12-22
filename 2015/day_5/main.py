def is_nice(line):
    if len([x for x in line if x in "aeiou"]) < 3:
        return False
    if sum([line[i] == line[i+1] for i in range(len(line)-1)]) == 0:
        return False
    if len([x for x in ["ab", "cd", "pq", "xy"] if x in line]) > 0:
        return False
    return True


def is_nice_2(line):
    check_1 = False
    for i in range(len(line)-3):
        checking = line[i:i+2]
        if checking in line[i+2:]:
            check_1 = True
            break
    check_2 = False
    for i in range(len(line) - 2):
        if line[i] == line[i + 2]:
            check_2 = True
            break
    return check_1 and check_2


def main():
    out = 0
    with open("input.txt") as f:
        for line in f.readlines():
            line = line.strip()
            if is_nice_2(line):
                out += 1
    print(out)


if __name__ == '__main__':
    main()
    # print(is_nice_2("qjhvhtzxzqqjkmpb"))
