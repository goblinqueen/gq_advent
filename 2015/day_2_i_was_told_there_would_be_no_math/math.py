def get_surface(lg, w, h):
    return 2*lg*w + 2*w*h + 2*h*lg


def get_slack(lg, w, h):
    d = [lg, w, h]
    d.remove(max(d))
    return d[0] * d[1]


def get_bow(lg, w, h):
    return lg * w * h


def get_ribbon(lg, w, h):
    d = [lg, w, h]
    d.remove(max(d))
    return 2 * d[0] + 2 * d[1]


def main():
    with open("input.txt") as f:
        total = 0
        for line in f.readlines():
            lg, w, h = [int(x) for x in line.strip().split("x")]
            total += get_bow(lg, w, h)
            total += get_ribbon(lg, w, h)
        print(total)


if __name__ == '__main__':
    main()
