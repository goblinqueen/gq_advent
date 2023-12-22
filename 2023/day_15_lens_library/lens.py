def h(string):
    res = 0
    for ch in string:
        res = res + ord(ch)
        res = res * 17
        res = res % 256
    return res


def main():
    boxes = {}

    with open("input.txt") as f:
        for line in f.readlines()[0].split(","):
        # for line in TEST_INPUT.split(","):
            line = line.strip()
            assert line.count("=") + line.count("-") == 1
            if "-" in line:
                label = line[:-1]
                try:
                    boxes[h(label)].pop(label)
                except KeyError:
                    pass
            elif "=" in line:
                label, value = line.split("=")
                boxes[h(label)] = boxes.get(h(label), {})
                boxes[h(label)][label] = value

    res = 0
    for box_num, box in boxes.items():
        for i, kv in enumerate(box.items()):
            label, value = kv
            res += (box_num + 1) * (i+1) * int(value)
    print(res)





if __name__ == '__main__':
    TEST_INPUT = '''rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'''
    main()
    # print(h("HASH"))