import functools
import operator
from dataclasses import dataclass

from aoc_helper.constants import DIRS_8
from aoc_helper.io import IoOutputType, read_data

Coord = tuple[int, int]


@dataclass
class Number:
    value: int
    coords: list[Coord]

    def append(self, digit: int, coord: Coord):
        self.value = self.value * 10 + digit
        self.coords.append(coord)


def is_part(grid: list[list[str]], number: Number) -> bool:
    nr = len(grid)
    nc = len(grid[0])
    for i, j in number.coords:
        for di, dj in DIRS_8:
            next_i = i + di
            next_j = j + dj
            if not (0 <= next_i < nr and 0 <= next_j < nc):
                continue
            if grid[next_i][next_j].isdigit():
                continue
            if grid[next_i][next_j] == ".":
                continue
            return True
    return False


def find_ratio(
    i: int,
    j: int,
    coord_to_num: dict[Coord, tuple[Coord, ...]],
    num_to_part: dict[tuple[Coord, ...], Number],
) -> int:
    found: set[tuple[Coord, ...]] = set()
    for di, dj in DIRS_8:
        next_i = i + di
        next_j = j + dj
        if (next_i, next_j) not in coord_to_num:
            continue
        found.add(coord_to_num[(next_i, next_j)])
    return (
        0
        if len(found) != 2
        else functools.reduce(
            operator.mul, (num_to_part[num].value for num in found), 1
        )
    )


def main():
    data = read_data("day3.txt", IoOutputType.GRID)
    nr = len(data)
    nc = len(data[0])
    result = 0
    coord_to_num: dict[Coord, tuple[Coord, ...]] = {}
    num_to_part: dict[tuple[Coord, ...], Number] = {}
    for i in range(nr):
        j = 0
        while j < nc:
            if data[i][j].isdigit():
                number = Number(value=int(data[i][j]), coords=[(i, j)])
                k = j
                while k + 1 < nc and data[i][k + 1].isdigit():
                    k += 1
                    number.append(int(data[i][k]), (i, k))
                if is_part(data, number):
                    result += number.value
                    num = tuple(number.coords)
                    for coord in number.coords:
                        coord_to_num[coord] = num
                    num_to_part[num] = number
                j = k
            j += 1
    print(result)

    result2 = 0
    for i in range(nr):
        for j in range(nc):
            if data[i][j] == "*":
                result2 += find_ratio(i, j, coord_to_num, num_to_part)

    print(result2)


if __name__ == "__main__":
    main()
