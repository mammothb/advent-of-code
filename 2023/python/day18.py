import re

from aoc_helper.io import IoOutputType, read_data

DIRS = {
    "R": (0, 1),
    "U": (-1, 0),
    "L": (0, -1),
    "D": (1, 0),
    "0": (0, 1),
    "3": (-1, 0),
    "2": (0, -1),
    "1": (1, 0),
}


def solve(lines: list[str]) -> int:
    i = 0
    j = 0
    perimeter = 0
    area = 0
    for line in lines:
        d, step, _ = line.rstrip().split(" ")
        step = int(step)
        di, dj = DIRS[d]
        i += di * step
        j += dj * step
        perimeter += step
        area += j * di * step
    return area + perimeter // 2 + 1


def solve2(lines: list[str]) -> int:
    pattern = re.compile(r"\(#([\d\w]+)\)")
    i = 0
    j = 0
    perimeter = 0
    area = 0
    for line in lines:
        _, _, rgb = line.rstrip().split(" ")
        res = pattern.search(rgb)
        assert res is not None
        d = res.group(1)[-1]
        step = int(res.group(1)[:-1], 16)

        step = int(step)
        di, dj = DIRS[d]
        i += di * step
        j += dj * step
        perimeter += step
        area += j * di * step
    return area + perimeter // 2 + 1


def main():
    data = read_data("day18.txt", IoOutputType.LINE)
    print(solve(data))
    print(solve2(data))


if __name__ == "__main__":
    main()
