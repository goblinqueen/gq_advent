import copy
import multiprocessing
import re
import typing


def process_rule(line):
    global RULES
    m = re.search("(.*){(.*)}", line)
    name, steps = m.groups()
    assert name not in RULES
    out = []
    for step in steps.split(","):
        if ":" in step:
            cond, nex = step.split(":")
        else:
            cond, nex = "True", step
        out.append((cond, nex))
    RULES[name] = out


def exec_rule(name: str, x: int, m: int, a: int, s: int):
    print(f"... ... Running rule {name}")
    global SUM
    rule = RULES[name]
    for rule in rule:
        if eval(rule[0]):
            if rule[1] == "R":
                return
            elif rule[1] == "A":
                SUM += (x + m + a + s)
                return
            else:
                return exec_rule(rule[1], x, m, a, s)
    return


class NotList:
    _start_values = []
    _end_values = []

    def st(self):
        return self._start_values

    def en(self):
        return self._end_values

    def __init__(self, start_values, end_values):
        self._start_values = start_values
        self._end_values = end_values

    def get_sum(self):
        out = 0
        for i, st in enumerate(self._start_values):
            en = self._start_values[i]
            out += ((en*en - (st - 1)*(st-1)) + (en - (st-1))) / 2
        return out

    def set_start(self, var, val):
        self._start_values["xmas".find(var)] = val

    def set_end(self, var, val):
        self._end_values["xmas".find(var)] = val

    def get_nice_naughty(self, rule) -> tuple:  # rule[0]
        if rule == "True":
            return self, NotList((0, 0, 0, 0), (0, 0, 0, 0))
        if ">" in rule:
            var, val = rule.split(">")
            val = int(val)
            if val < self._start_values["xmas".find(var)]:
                return self, NotList((0, 0, 0, 0), (0, 0, 0, 0))
            elif val >= self._end_values["xmas".find(var)]:
                return NotList((0, 0, 0, 0), (0, 0, 0, 0)), self
            else:
                nice = copy.deepcopy(self)
                nice.set_start(var, val + 1)
                naughty = copy.deepcopy(self)
                naughty.set_end(var, val)
                return nice, naughty
        if "<" in rule:
            var, val = rule.split("<")
            val = int(val)
            if val > self._end_values["xmas".find(var)]:
                return self, NotList((0, 0, 0, 0), (0, 0, 0, 0))
            elif val <= self._start_values["xmas".find(var)]:
                return NotList((0, 0, 0, 0), (0, 0, 0, 0)), self
            else:
                nice = copy.deepcopy(self)
                nice.set_start(var, val)
                naughty = copy.deepcopy(self)
                naughty.set_end(var, val + 1)
                return nice, naughty
        raise Exception('Unexpected input')


def exec_rule_list(name: str, in_list: NotList):
    print(f"... ... Running rule {name} for {in_list.st()} -- {in_list.en()}")
    global SUM
    rule = RULES[name]
    naughty = in_list
    for rule in rule:
        if not naughty:
            return
        nice, naughty = naughty.get_nice_naughty(rule[0])
        if rule[1] == "R":
            continue
        elif rule[1] == "A":
            SUM += nice.get_sum()
        else:
            exec_rule_list(rule[1], nice)
    return


def process(line):
    print(f"... processing {line}")
    m = re.search("{x=(.*),m=(.*),a=(.*),s=(.*)}", line)
    assert len(m.groups()) == 4
    x, m, a, s = [int(y) for y in m.groups()]
    exec_rule("in", x, m, a, s)
    print(f"... processing {line} done. SUM = {SUM}")
    return


def main():

    with open("input.txt") as f:
        # for line in f.readlines():
        #     line = line.strip()
        for line in TEST_INPUT.split("\n"):
            if line:
                # if line[0] == "{":
                #     m = re.search("{x=(.*),m=(.*),a=(.*),s=(.*)}", line)
                #     assert len(m.groups()) == 4
                #     x, m, a, s = [int(y) for y in m.groups()]
                #     lines.append((x, m, a, s))
                    # process(line)
                if line[0] != "{":
                    process_rule(line)

    exec_rule_list("in", NotList([0, 0, 0, 0], [4000, 4000, 4000, 4000]))
    print(SUM)


if __name__ == '__main__':

    TEST_INPUT = '''px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}'''

    RULES = {}
    SUM = 0

    main()

