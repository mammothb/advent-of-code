from helper import read_data


def solve(
    grid: list[list[int]],
    nr: int,
    nc: int,
    i: int,
    j: int,
    seen: set[tuple[int, int]],
    result: list[int],
):
    if grid[i][j] == 9:
        seen.add((i, j))
        result[0] += 1
        return
    for next_i, next_j in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
        if not (0 <= next_i < nr and 0 <= next_j < nc):
            continue
        if grid[next_i][next_j] != grid[i][j] + 1:
            continue
        solve(grid, nr, nc, next_i, next_j, seen, result)


def main():
    data = read_data("day10.txt")
    grid = [list(map(int, line)) for line in data.rstrip().split("\n")]
    nr = len(grid)
    nc = len(grid[0])

    result = 0
    result2 = [0]
    for i in range(nr):
        for j in range(nc):
            if grid[i][j] == 0:
                curr: set[tuple[int, int]] = set()
                solve(grid, nr, nc, i, j, curr, result2)
                result += len(curr)
    print(result)
    print(result2[0])


if __name__ == "__main__":
    main()
