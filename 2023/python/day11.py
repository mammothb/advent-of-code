from aoc_helper.bit import band_pass
from aoc_helper.io import IoOutputType, read_data
from aoc_helper.types import Coord


def find_expansion(grid: list[list[str]]) -> tuple[int, int]:
    nr = len(grid)
    nc = len(grid[0])
    row = (1 << nr) - 1
    col = (1 << nc) - 1
    for i in range(nr):
        for j in range(nc):
            if grid[i][j] == "#":
                row &= ~(1 << i)
                col &= ~(1 << j)
    return row, col


def get_distance(
    src: Coord, dest: Coord, row_mask: int, col_mask: int, age: int = 1
) -> int:
    i1 = min(src[0], dest[0])
    i2 = max(src[0], dest[0])
    j1 = min(src[1], dest[1])
    j2 = max(src[1], dest[1])
    i_mask = band_pass(row_mask, i1, i2)
    j_mask = band_pass(col_mask, j1, j2)
    return i2 - i1 + j2 - j1 + i_mask.bit_count() * age + j_mask.bit_count() * age


def get_galaxies(grid: list[list[str]]) -> list[Coord]:
    nr = len(grid)
    nc = len(grid[0])
    result: list[Coord] = []
    for i in range(nr):
        for j in range(nc):
            if grid[i][j] == "#":
                result.append((i, j))
    return result


def main():
    data = read_data("day11.txt", IoOutputType.GRID)
    # data = read_data("day11_easy.txt", IoOutputType.GRID)
    row_mask, col_mask = find_expansion(data)
    galaxies = get_galaxies(data)
    n = len(galaxies)
    result = 0
    result2 = 0
    for i in range(n):
        result += sum(
            get_distance(galaxies[i], galaxies[j], row_mask, col_mask)
            for j in range(i + 1, n)
        )
        result2 += sum(
            get_distance(galaxies[i], galaxies[j], row_mask, col_mask, age=999999)
            for j in range(i + 1, n)
        )
    print(result)
    print(result2)


if __name__ == "__main__":
    main()
