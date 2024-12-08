from helper import read_data

DIRS = ((-1, 0), (0, 1), (1, 0), (0, -1))


def solve(grid: list[list[str]], nr: int, nc: int, start: tuple[int, int]) -> int:
    i = start[0]
    j = start[1]
    seen: set[tuple[int, int]] = set()
    curr_dir = 0
    while 0 <= i < nr and 0 <= j < nc:
        seen.add((i, j))
        di = DIRS[curr_dir][0]
        dj = DIRS[curr_dir][1]
        if not (0 <= i + di < nr and 0 <= j + dj < nc):
            break
        while grid[i + di][j + dj] == "#":
            curr_dir = (curr_dir + 1) % 4
            di = DIRS[curr_dir][0]
            dj = DIRS[curr_dir][1]
        i += di
        j += dj
    return len(seen)


def solve2(grid: list[list[str]], nr: int, nc: int, start: tuple[int, int]) -> int:
    i = start[0]
    j = start[1]
    seen: set[tuple[int, int, int]] = set()
    curr_dir = 0
    while 0 <= i < nr and 0 <= j < nc:
        pos = (i, j, curr_dir)
        if pos in seen:
            return True
        seen.add(pos)
        di = DIRS[curr_dir][0]
        dj = DIRS[curr_dir][1]
        if not (0 <= i + di < nr and 0 <= j + dj < nc):
            break
        while grid[i + di][j + dj] == "#":
            curr_dir = (curr_dir + 1) % 4
            di = DIRS[curr_dir][0]
            dj = DIRS[curr_dir][1]
        i += di
        j += dj
    return False


def main():
    data = read_data("day6.txt")
    grid = list(map(list, data.rstrip().split("\n")))
    nr = len(grid)
    nc = len(grid[0])

    start: tuple[int, int] | None = None
    for i in range(nr):
        for j in range(nc):
            if grid[i][j] == "^":
                start = (i, j)
                break
        if start is not None:
            break
    assert start is not None
    result = solve(grid, nr, nc, start)
    print(result)

    result2 = 0
    for i in range(nr):
        for j in range(nc):
            if grid[i][j] != ".":
                continue
            grid[i][j] = "#"
            if solve2(grid, nr, nc, start):
                result2 += 1
            grid[i][j] = "."
    print(result2)


if __name__ == "__main__":
    main()
