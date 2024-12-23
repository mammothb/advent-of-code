import collections

from helper import read_data


def print_grid(grid: list[list[str]]):
    for row in grid:
        print("".join(row))


def corrupt_grid(lines: list[str], n: int, num_step: int) -> list[list[str]]:
    grid = [["."] * n for _ in range(n)]

    for step, line in enumerate(lines, 1):
        x, y = tuple(map(int, line.split(",")))
        grid[y][x] = "#"
        if step == num_step:
            break
    return grid


def solve(grid: list[list[str]]) -> int | None:
    n = len(grid)
    queue = collections.deque([(0, 0, 0)])
    seen = set([(0, 0)])
    while queue:
        n_queue = len(queue)
        for _ in range(n_queue):
            i, j, num_step = queue.popleft()
            if i == n - 1 and j == n - 1:
                return num_step
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                next_i = i + di
                next_j = j + dj
                if not (0 <= next_i < n and 0 <= next_j < n):
                    continue
                if grid[next_i][next_j] == "#":
                    continue
                if (next_i, next_j) in seen:
                    continue
                seen.add((next_i, next_j))
                queue.append((next_i, next_j, num_step + 1))


def main():
    data = read_data("day18.txt")
    lines = data.rstrip().split("\n")

    grid = corrupt_grid(lines=lines, n=71, num_step=1024)
    print(solve(grid))

    l = 1024
    r = len(lines)
    while l <= r:
        mid = l + (r - l) // 2
        grid = corrupt_grid(lines, 71, mid)
        if solve(grid) is not None:
            l = mid + 1
        else:
            r = mid - 1
    print(lines[r])


if __name__ == "__main__":
    main()
