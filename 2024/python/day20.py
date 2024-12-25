from collections.abc import Generator

from helper import read_data


def solve(track: list[tuple[int, int]], max_dist: int) -> Generator[int]:
    for t1, (i, j) in enumerate(track):
        for t2 in range(t1 + 3, len(track)):
            next_i, next_j = track[t2]
            dist = abs(next_i - i) + abs(next_j - j)
            if dist <= max_dist and t2 - t1 > dist:
                yield t2 - t1 - dist


def main():
    data = read_data("day20.txt")
    grid = data.rstrip().split("\n")

    i, j = next(
        (i, j)
        for i, row in enumerate(grid)
        for j, cell in enumerate(row)
        if cell == "S"
    )
    track = [(-1, -1), (i, j)]
    while grid[i][j] != "E":
        i, j = next(
            (next_i, next_j)
            for next_i, next_j in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1))
            if (next_i, next_j) != track[-2] and grid[next_i][next_j] != "#"
        )
        track.append((i, j))
    track = track[1:]

    print(sum(1 for saved in solve(track, 2) if saved >= 100))
    print(sum(1 for saved in solve(track, 20) if saved >= 100))


if __name__ == "__main__":
    main()
