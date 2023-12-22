#  12 red cubes, 13 green cubes, and 14 blue cubes
CONFIG = {'red': 12, 'green': 13, 'blue': 14}


def split_line(line):
    game_id, games = line.strip().split(":")
    game_id = int(game_id[5:])
    out = []
    for game in games.split(";"):
        out_game = []
        for draw in game.split(","):
            out_game.append(draw.split())
        out.append(out_game)
    return game_id, out


def part_1():
    with open("input.txt") as file:
        total = 0
        good = True
        for line in file.readlines():
            game_id, games = split_line(line)
            for game in games:
                for ct, col in game:
                    if int(ct) > CONFIG[col]:
                        good = False
            if good:
                total += game_id
            good = True
        print(total)


def part_2():
    with open("input.txt") as file:
        total = 0
        for line in file.readlines():
            power = {'red': 0, 'green': 0, 'blue': 0}
            game_id, games = split_line(line)
            for game in games:
                for ct, col in game:
                    if int(ct) > power[col]:
                        power[col] = int(ct)
            total += power['red'] * power['blue'] * power['green']
        print(total)


if __name__ == "__main__":
    part_2()
