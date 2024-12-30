from aoc_helper.io import IoOutputType, read_data


def diff_rows(grid: list[list[str]], l: int, r: int) -> int:
    nr = len(grid)
    return sum(grid[i][l] != grid[i][r] for i in range(nr))


def diff_cols(grid: list[list[str]], t: int, b: int) -> int:
    nc = len(grid[0])
    return sum(grid[t][j] != grid[b][j] for j in range(nc))


def solve(grid: list[list[str]]) -> int:
    nr = len(grid)
    nc = len(grid[0])
    for j in range(nc - 1):
        if diff_rows(grid, j, j + 1) == 0 and all(
            diff_rows(grid, l, r) == 0
            for l, r in zip(range(j - 1, -1, -1), range(j + 2, nc))
        ):
            return j + 1
    for i in range(nr - 1):
        if diff_cols(grid, i, i + 1) == 0 and all(
            diff_cols(grid, t, b) == 0
            for t, b in zip(range(i - 1, -1, -1), range(i + 2, nr))
        ):
            return (i + 1) * 100

    raise RuntimeError


def solve2(grid: list[list[str]]) -> int:
    nr = len(grid)
    nc = len(grid[0])
    for j in range(nc - 1):
        if (
            sum(
                diff_rows(grid, l, r)
                for l, r in zip(range(j, -1, -1), range(j + 1, nc))
            )
            == 1
        ):
            return j + 1
    for i in range(nr - 1):
        if (
            sum(
                diff_cols(grid, t, b)
                for t, b in zip(range(i, -1, -1), range(i + 1, nr))
            )
            == 1
        ):
            return (i + 1) * 100

    raise RuntimeError


def main():
    data = read_data("day13.txt", IoOutputType.BLOCK)
    result = 0
    result2 = 0
    for block in data:
        grid = [list(line) for line in block.split("\n")]
        result += solve(grid)
        result2 += solve2(grid)
    print(result)
    print(result2)


if __name__ == "__main__":
    main()
