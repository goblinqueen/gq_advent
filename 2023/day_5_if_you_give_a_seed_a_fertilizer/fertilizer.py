KEYS = ['seed-to-soil map:',
        'soil-to-fertilizer map:',
        'fertilizer-to-water map:',
        'water-to-light map:',
        'light-to-temperature map:',
        'temperature-to-humidity map:',
        'humidity-to-location map:']


def parse_input():
    out_seeds = []
    out_ranges = {}
    current_key = None
    with open("input_test.txt") as f:
        for line in f.readlines():
            line = line.strip()
            if line.startswith('seeds: '):
                out_seeds = [int(x) for x in line[len('seeds: '):].split()]
            elif line.endswith(" map:"):
                current_key = line.strip()
            elif line:
                dest, src_start, l = [int(x) for x in line.split()]
                assert src_start not in out_ranges.get(current_key, {})
                d = out_ranges.get(current_key, {})
                d[src_start] = (dest, l)
                out_ranges[current_key] = d

    return out_seeds, out_ranges


def get_soil(seed, key_name):
    soils = ranges[key_name]
    for seeds_start in sorted(soils.keys()):
        if seeds_start > seed:
            return seed
        else:
            soils_start, j = soils[seeds_start]
            if seed < seeds_start + j:
                return soils_start + j - (seeds_start + j - seed)
    return seed


def apply_mask_2(seed_list, mask):
    seed = {}
    for i in range(len(seed_list) // 2):
        seed[seed_list[2*i]] = seed_list[2*i + 1]

    start_nodes = list(seed.keys()) + list(mask.keys())
    seed_ends = [x + seed[x] - 1 for x in seed]
    mask_ends = [x + mask[x][1] - 1 for x in mask]
    end_nodes = seed_ends + mask_ends

    in_seed = 0
    curr_mask = False

    prev_node = None

    out = []

    node_list = sorted(start_nodes + end_nodes)
    for node in node_list:
        if node in seed.keys():
            assert not in_seed
            in_seed = True
        if node in seed_ends:
            assert in_seed
            in_seed = False
            if curr_mask:
                out += [prev_node + curr_mask, node + curr_mask]  # [range start, range end)
            else:
                out += [prev_node, node]

        if node in mask.keys():
            assert not curr_mask
            curr_mask = mask[node][0] - node

        if node in mask_ends:
            assert curr_mask
            curr_mask = False

        prev_node = node

    out_ = {}
    for i in range(len(out) // 2):
        out_[out[2*i]] = out[2*i + 1]

    print(out)
    in_range = 0
    prev_node = None
    for node in out:
        if node in out_.keys():
            in_range += 1
        else:
            in_range += -1

        prev_node = node

    return None


def apply_mask(seed_list, mask):
    total_out = []
    for i in range(len(seed_list)//2):
        seed = seed_list[2*i]
        r = seed_list[2*i + 1]
        out = set()
        for seeds_start in sorted(mask.keys()):
            if seeds_start > seed + r:
                if not out:
                    out.add((seed, r))
            else:
                soils_start, j = mask[seeds_start]

                if seeds_start + j - 1 < seed:
                    continue
                if seed < seeds_start:
                    out.add((seed, seeds_start - seed))
                if seeds_start + j > seed + r:
                    out.add((soils_start + seed - seeds_start, seeds_start + j - seed - r))
                else:
                    out.add((soils_start + seed - seeds_start, seeds_start + j - seed))
                    out.add((seeds_start + j, seed + r - seeds_start - j))
        if not out:
            out.add((seed, r))
        total_out += [item for sublist in list(out) for item in sublist]
    return total_out


# def plant():
#     out = 0
#     for i in range(len(seeds) // 2):
#         seed, r = seeds[2*i], seeds[2*i + 1]
#         stage_result = seed
#         for key_name in KEYS:
#             stage_result = get_min_soil(stage_result, r, key_name, ranges)
#         if out:
#             out = min(stage_result, out)
#         else:
#             out = stage_result
#         break
#     print(out)


if __name__ == "__main__":
    seeds, ranges = parse_input()

    # for key_name in KEYS:
    #     seeds = apply_mask(seeds, ranges[key_name])
    #     print(key_name, seeds)
    # print(seeds)

    print(seeds, ranges[KEYS[1]])
    print()
    print(apply_mask_2([57, 69, 81, 94], ranges[KEYS[1]]))

    # in_seeds = [seeds[0], seeds[1]]
    # for key_name in KEYS:
