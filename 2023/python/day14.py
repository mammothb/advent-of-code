import copy

from aoc_helper.io import IoOutputType, read_data


def roll_west(grid: list[list[str]]):
    nr = len(grid)
    nc = len(grid[0])
    for i in range(nr):
        idx = 0
        for j in range(nc):
            if grid[i][j] == "#":
                idx = j + 1
            elif grid[i][j] == "O":
                tmp = grid[i][idx]
                grid[i][idx] = grid[i][j]
                grid[i][j] = tmp
                idx += 1


def roll_east(grid: list[list[str]]):
    nr = len(grid)
    nc = len(grid[0])
    for i in range(nr):
        idx = nc - 1
        for j in range(nc - 1, -1, -1):
            if grid[i][j] == "#":
                idx = j - 1
            elif grid[i][j] == "O":
                tmp = grid[i][idx]
                grid[i][idx] = grid[i][j]
                grid[i][j] = tmp
                idx -= 1


def roll_north(grid: list[list[str]]):
    nr = len(grid)
    nc = len(grid[0])
    for j in range(nc):
        idx = 0
        for i in range(nr):
            if grid[i][j] == "#":
                idx = i + 1
            elif grid[i][j] == "O":
                tmp = grid[idx][j]
                grid[idx][j] = grid[i][j]
                grid[i][j] = tmp
                idx += 1


def roll_south(grid: list[list[str]]):
    nr = len(grid)
    nc = len(grid[0])
    for j in range(nc):
        idx = nr - 1
        for i in range(nr - 1, -1, -1):
            if grid[i][j] == "#":
                idx = i - 1
            elif grid[i][j] == "O":
                tmp = grid[idx][j]
                grid[idx][j] = grid[i][j]
                grid[i][j] = tmp
                idx -= 1


ROLLS = [roll_north, roll_west, roll_south, roll_east]


def serialize(grid: list[list[str]]) -> str:
    return "".join("".join(row) for row in grid)


def deserialize(state: str, nc: int) -> list[list[str]]:
    result: list[list[str]] = []
    for i in range(0, len(state), nc):
        result.append(list(state[i : i + nc]))
    return result


def get_cycles(grid: list[list[str]]) -> tuple[dict[str, int], int]:
    grid_copy = copy.deepcopy(grid)
    seen: dict[str, int] = {}
    while True:
        grid_state = serialize(grid_copy)
        if grid_state in seen:
            return seen, seen[grid_state]
        seen[grid_state] = len(seen)
        for roll in ROLLS:
            roll(grid_copy)


def main():
    data = read_data("day14.txt", IoOutputType.GRID)
    nr = len(data)
    nc = len(data[0])

    rolled_grid = copy.deepcopy(data)
    roll_north(rolled_grid)
    print(sum(row.count("O") * (nr - i) for i, row in enumerate(rolled_grid)))

    cycle_grid = copy.deepcopy(data)
    cycles, cycle_start = get_cycles(cycle_grid)
    idx_to_state = {
        i - cycle_start: state for state, i in cycles.items() if i >= cycle_start
    }
    spun_grid = deserialize(
        idx_to_state[(1000000000 - cycle_start) % len(idx_to_state)], nc
    )
    print(sum(row.count("O") * (nr - i) for i, row in enumerate(spun_grid)))


if __name__ == "__main__":
    main()
