def main():
    with open("input.txt") as f:
        floor = 0
        for line in f.readlines():
            line = line.strip()
            for i, ch in enumerate(line):
                assert ch in "()"
                if ch == "(":
                    floor += 1
                else:
                    floor += -1
                if floor == -1:
                    print(i)
        print(floor)


if __name__ == '__main__':
    main()