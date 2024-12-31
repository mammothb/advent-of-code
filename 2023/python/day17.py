import heapq

from aoc_helper.constants import DIRS_4
from aoc_helper.io import IoOutputType, read_data


def solve(grid: list[list[int]], min_step: int, max_step: int) -> int:
    nr = len(grid)
    nc = len(grid[0])
    seen: set[tuple[int, int, int]] = set()
    costs: dict[tuple[int, int, int], int] = {}
    h = [(0, 0, 0, -1)]
    while h:
        cost, i, j, banned_dir = heapq.heappop(h)
        if i == nr - 1 and j == nc - 1:
            return cost
        if (i, j, banned_dir) in seen:
            continue
        seen.add((i, j, banned_dir))
        for d, (di, dj) in enumerate(DIRS_4):
            if d == banned_dir or (d + 2) % 4 == banned_dir:
                continue
            cost_increase = 0
            for step in range(1, max_step + 1):
                next_i = i + di * step
                next_j = j + dj * step
                if not (0 <= next_i < nr and 0 <= next_j < nc):
                    continue
                cost_increase += grid[next_i][next_j]
                if step < min_step:
                    continue
                next_cost = cost + cost_increase
                if costs.get((next_i, next_j, d), float("inf")) <= next_cost:
                    continue
                costs[(next_i, next_j, d)] = next_cost
                heapq.heappush(h, (next_cost, next_i, next_j, d))
    raise RuntimeError


def main():
    data = read_data("day17.txt", IoOutputType.GRID)
    # data = read_data("day17_easy.txt", IoOutputType.GRID)
    grid = [list(map(int, row)) for row in data]
    print(solve(grid, 1, 3))
    print(solve(grid, 4, 10))


if __name__ == "__main__":
    main()
