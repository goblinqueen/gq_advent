def main():

    visited = set()

    santa = (0, 0)
    robo_santa = (0, 0)
    visited.add(santa)
    with open("input.txt") as f:
        for line in f.readlines():
            for i, ch in enumerate(line.strip()):
                assert ch in "><v^"
                if i % 2:
                    house = santa
                else:
                    house = robo_santa
                if ch == "<":
                    house = (house[0] - 1, house[1])
                elif ch == ">":
                    house = (house[0] + 1, house[1])
                elif ch == "^":
                    house = (house[0], house[1] - 1)
                elif ch == "v":
                    house = (house[0], house[1] + 1)
                visited.add(house)
                if i % 2:
                    santa = house
                else:
                    robo_santa = house

    print(len(visited))


if __name__ == '__main__':
    main()
