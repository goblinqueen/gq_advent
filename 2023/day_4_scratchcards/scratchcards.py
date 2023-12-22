def part_1():
    with open("input.txt") as f:
        total = 0
        for line in f.readlines():
            winning, current = line.strip().split(": ")[1].split(" | ")
            score = pow(2, sum([x in [int(x) for x in winning.split()] for x in [int(x) for x in current.split()]])-1)
            if score >= 1:
                total += score
        print(total)


def part_2():
    with open("input.txt") as f:
        repeats = {}
        i = 0
        total = 0
        for line in f.readlines():
            i += 1  # current card number
            count = repeats.get(i, 0) + 1
            print(f"{100*i/216:.2f}% processing {i} {count} times")
            total += count
            winning, current = line.strip().split(": ")[1].split(" | ")
            score = sum([x in [int(x) for x in winning.split()] for x in [int(x) for x in current.split()]])
            for i_won in range(1, score + 1):
                repeats[i + i_won] = repeats.get(i + i_won, 0) + count
        print(total)


if __name__ == '__main__':
    part_2()  # 30
