import collections
import heapq

from helper import read_data


def dijkstra(
    grid: list[list[str]], nr: int, nc: int, starts: list[tuple[int, int, str]]
) -> dict[tuple[int, int, str], float | int]:
    directions = {"E": (0, 1), "W": (0, -1), "N": (-1, 0), "S": (1, 0)}
    costs: dict[tuple[int, int, str], float | int] = collections.defaultdict(
        lambda: float("inf")
    )
    h: list[tuple[float | int, int, int, str]] = []
    for i, j, direction in starts:
        costs[(i, j, direction)] = 0
        h.append((costs[(i, j, direction)], i, j, direction))
    heapq.heapify(h)

    while h:
        curr_cost, i, j, curr_dir = heapq.heappop(h)
        if curr_cost > costs[(i, j, curr_dir)]:
            continue
        for next_dir in "EWNS".replace(curr_dir, ""):
            next_cost = curr_cost + 1000
            if next_cost < costs[(i, j, next_dir)]:
                costs[(i, j, next_dir)] = next_cost
                heapq.heappush(h, (costs[(i, j, next_dir)], i, j, next_dir))
        di, dj = directions[curr_dir]
        next_i = i + di
        next_j = j + dj
        if not (0 <= next_i < nr and 0 <= next_j < nc):
            continue
        if grid[next_i][next_j] == "#":
            continue
        next_cost = curr_cost + 1
        if next_cost < costs[(next_i, next_j, curr_dir)]:
            costs[(next_i, next_j, curr_dir)] = next_cost
            heapq.heappush(
                h, (costs[(next_i, next_j, curr_dir)], next_i, next_j, curr_dir)
            )
    return costs


def main():
    data = read_data("day16.txt")
    grid = [list(line) for line in data.rstrip().split("\n")]
    nr = len(grid)
    nc = len(grid[0])

    start = None
    end = None
    for i in range(nr):
        for j in range(nc):
            if grid[i][j] == "S":
                start = (i, j)
                break
            if grid[i][j] == "E":
                end = (i, j)
                break
        if start is not None and end is not None:
            break
    assert start is not None
    assert end is not None

    costs = dijkstra(grid, nr, nc, [(start[0], start[1], "E")])
    result = min(costs[(end[0], end[1], direction)] for direction in "EWNS")
    print(result)

    costs2 = dijkstra(
        grid, nr, nc, [(end[0], end[1], direction) for direction in "EWNS"]
    )
    flip = {"E": "W", "W": "E", "N": "S", "S": "N"}
    result2: set[tuple[int, int]] = set()
    for i in range(nr):
        for j in range(nc):
            for direction in "EWNS":
                from_start = (i, j, direction)
                from_end = (i, j, flip[direction])
                if costs[from_start] + costs2[from_end] == result:
                    result2.add((i, j))
    print(len(result2))


if __name__ == "__main__":
    main()
