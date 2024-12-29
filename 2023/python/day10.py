import collections
from typing import NamedTuple

from aoc_helper.constants import DIRS_4
from aoc_helper.io import IoOutputType, read_data

Coord = tuple[int, int]

R, U, L, D = ((0, 1), (-1, 0), (0, -1), (1, 0))
CONNECTIONS = ("-J7", "|F7", "-FL", "|LJ")


def follow_loop(grid: list[list[str]], start: Coord) -> set[Coord]:
    matches: list[Coord] = []
    for (di, dj), candidates in zip(DIRS_4, CONNECTIONS):
        i = start[0] + di
        j = start[1] + dj
        if grid[i][j] in candidates:
            matches.append((di, dj))
    match_set = set(matches)
    if match_set == {U, D}:
        start_pipe = "|"
    elif match_set == {L, R}:
        start_pipe = "-"
    elif match_set == {U, L}:
        start_pipe = "J"
    elif match_set == {U, R}:
        start_pipe = "L"
    elif match_set == {D, L}:
        start_pipe = "7"
    elif match_set == {D, R}:
        start_pipe = "F"
    else:
        raise RuntimeError

    i, j = start
    di, dj = matches[0]
    seen = set([(i, j)])
    while True:
        i += di
        j += dj
        seen.add((i, j))

        if grid[i][j] in "L7":
            di, dj = dj, di
        elif grid[i][j] in "FJ":
            di, dj = -dj, -di
        elif grid[i][j] == "S":
            break

    grid[start[0]][start[1]] = start_pipe

    return seen


def get_area(grid: list[list[str]], loop: set[Coord]) -> int:
    result = 0
    for i, row in enumerate(grid):
        inside = 0
        for j, cell in enumerate(row):
            if (i, j) in loop:
                inside ^= int(cell in "|F7")
            else:
                result += inside
    return result


def main():
    data = read_data("day10.txt", IoOutputType.GRID)
    nr = len(data)
    nc = len(data[0])
    start = None
    for i in range(nr):
        for j in range(nc):
            if data[i][j] == "S":
                start = (i, j)
                break
        if start is not None:
            break
    assert start is not None
    main_loop = follow_loop(data, start)
    print((len(main_loop) + 1) // 2)
    print(get_area(data, main_loop))


if __name__ == "__main__":
    main()
