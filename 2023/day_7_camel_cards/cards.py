import functools

CARDS = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

COMBINATIONS = [
    [5],
    [1, 4],
    [2, 3],
    [1, 1, 3],
    [1, 2, 2],
    [1, 1, 1, 2],
    [1, 1, 1, 1, 1]
]

TEST_IN = '''
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
'''


def get_combination(hand):
    out = []
    curr_card = None
    curr_count = 0
    jokers = 0
    for card in sorted(hand):
        if card == 'J':
            jokers += 1
            continue
        if card != curr_card:
            if curr_card is not None:
                out.append(curr_count)
                curr_count = 0
            curr_card = card
        curr_count += 1
    out.append(curr_count)
    out = sorted(out)
    out[-1] = out[-1] + jokers
    # if jokers > 1:
    #     print(hand)
    #     print(out)
    #     for i in range(jokers):
    #         if len(out) > 1:
    #             out[-1] = out[-1] + 1
    #             out[0] = out[0] - 1
    #             out = sorted([x for x in out if x > 0])
    #     print(out)
    return COMBINATIONS.index(out)


def compare_hands(hand_1, hand_2):
    hand_1 = hand_1[0]
    hand_2 = hand_2[0]
    if get_combination(hand_1) != get_combination(hand_2):
        return - get_combination(hand_1) + get_combination(hand_2)
    for i in range(5):
        if CARDS.index(hand_1[i]) != CARDS.index(hand_2[i]):
            return - CARDS.index(hand_1[i]) + CARDS.index(hand_2[i])
    return 0


def main():
    hands = []
    with open("input.txt") as f:
        for line in f.readlines():
            line = line.strip()
    # for line in TEST_IN.split("\n"):
            if not line:
                continue
            print(line.split()[0], get_combination(line.split()[0]))
            hands.append(line.split())

    ranked = sorted(hands, key=functools.cmp_to_key(compare_hands))
    print(sum([(i + 1) * int(ranked[i][1]) for i in range(len(ranked))]))


if __name__ == "__main__":
    main()
