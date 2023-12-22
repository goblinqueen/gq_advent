import math

TIME_TEST = [7, 15, 30]
DISTANCE_TEST = [9, 40, 200]

TIME = [63, 78, 94, 68]
DISTANCE = [411, 1274, 2047, 1035]


def get_interval(a, b):
    high_root = 1/2 * (math.sqrt(a*a - 4*b) + a)
    if high_root == round(high_root):
        high_root = int(high_root - 1)
    else:
        high_root = math.floor(high_root)
    low_root = 1/2 * (a - math.sqrt(a*a - 4*b))
    if low_root == round(low_root):
        low_root = int(low_root + 1)
    else:
        low_root = math.ceil(low_root)
    return high_root - low_root + 1


def main():
    total = 1
    for i in range(len(TIME)):
        total = total * get_interval(TIME[i], DISTANCE[i])
    print(total)


if __name__ == "__main__":
    print(get_interval(63789468, 411127420471035))
    # main()
