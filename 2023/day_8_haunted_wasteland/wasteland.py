import math

from sympy import primefactors


def read_graph():
    is_header = True
    out_path = None
    out = {}
    with open("input.txt") as f:
        for line in f.readlines():
            line = line.strip()
            if out_path is None:
                out_path = line
                continue
            elif is_header:
                is_header = False
                continue

            value, children = line.split(" = ")
            assert value not in out
            out[value] = children[1:-1].split(', ')

    return out_path, out


def traverse_path(curr_value):
    i = 0
    while curr_value[-1] != 'Z':
        for move in path:
            assert move in 'LR'
            curr_value = graph[curr_value][int(move == 'R')]
        i += 1
    return i


if __name__ == "__main__":
    path, graph = read_graph()
    factors = set()
    for start_node in [x for x in graph.keys() if x[-1] == 'A']:
        factors.update(set(primefactors(traverse_path(start_node))))
    print(math.prod(factors) * len(path))



