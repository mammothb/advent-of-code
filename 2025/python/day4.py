from collections import deque
from collections.abc import Generator

from helper import read_data


def parse_grid(data: str) -> list[list[str]]:
    return [list(row) for row in data.strip().split("\n")]


def neighbors(i: int, j: int, nr: int, nc: int) -> Generator[tuple[int, int]]:
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            if di == 0 and dj == 0:
                continue
            next_i = i + di
            next_j = j + dj
            if 0 <= next_i < nr and 0 <= next_j < nc:
                yield next_i, next_j


def main():
    data = read_data("day4.txt")
    grid = parse_grid(data)
    nr = len(grid)
    nc = len(grid[0])
    cost = [[0] * nc for _ in range(nr)]

    count = 0
    for i in range(nr):
        for j in range(nc):
            if grid[i][j] != "@":
                continue
            cost[i][j] = sum(
                1
                for next_i, next_j in neighbors(i, j, nr, nc)
                if grid[next_i][next_j] == "@"
            )
            if cost[i][j] < 4:
                count += 1
    print(count)


def main2():
    data = read_data("day4.txt")
    grid = parse_grid(data)
    nr = len(grid)
    nc = len(grid[0])

    cost = [[0] * nc for _ in range(nr)]
    accessible = [[False] * nc for _ in range(nr)]
    q: deque[tuple[int, int]] = deque()

    for i in range(nr):
        for j in range(nc):
            if grid[i][j] != "@":
                continue
            cost[i][j] = sum(
                1
                for next_i, next_j in neighbors(i, j, nr, nc)
                if grid[next_i][next_j] == "@"
            )
            if cost[i][j] < 4:
                accessible[i][j] = True
                q.append((i, j))

    removed = 0
    seen: set[tuple[int, int]] = set()
    while q:
        i, j = q.popleft()
        if (i, j) in seen:
            continue
        seen.add((i, j))
        removed += 1
        grid[i][j] = "."

        for next_i, next_j in neighbors(i, j, nr, nc):
            if grid[next_i][next_j] == "@" and (next_i, next_j) not in seen:
                cost[next_i][next_j] -= 1
                if cost[next_i][next_j] < 4 and not accessible[next_i][next_j]:
                    accessible[next_i][next_j] = True
                    q.append((next_i, next_j))

    print(removed)


if __name__ == "__main__":
    main()
    main2()
