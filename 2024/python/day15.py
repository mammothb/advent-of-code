import copy

from helper import read_data


def get_direction(move: str) -> tuple[int, int]:
    match move:
        case "^":
            di = -1
            dj = 0
        case ">":
            di = 0
            dj = 1
        case "<":
            di = 0
            dj = -1
        case "v":
            di = 1
            dj = 0
        case _:
            raise ValueError
    return di, dj


def solve1(grid: list[list[str]], movement: str):
    nr = len(grid)
    nc = len(grid[0])
    start: tuple[int, int] | None = None
    for i in range(nr):
        if start is not None:
            break
        for j in range(nc):
            if start is not None:
                break
            if grid[i][j] == "@":
                start = (i, j)
    assert start is not None

    i = start[0]
    j = start[1]
    for index, move in enumerate(movement):
        di, dj = get_direction(move)
        next_i = i + di
        next_j = j + dj
        if not (0 <= next_i < nr and 0 <= next_j < nc):
            continue
        if grid[next_i][next_j] == "#":
            continue
        if grid[next_i][next_j] == "O":
            next_i2 = next_i
            next_j2 = next_j
            while 0 <= next_i2 + di < nr and 0 <= next_j2 + dj < nc:
                next_i2 += di
                next_j2 += dj
                if grid[next_i2][next_j2] != "O":
                    break
            if grid[next_i2][next_j2] == "#":
                continue
            grid[next_i2][next_j2] = "O"
            grid[next_i][next_j] = "."
            grid[i][j] = "."
            grid[next_i][next_j] = "@"
            i = next_i
            j = next_j
        else:
            grid[i][j] = "."
            grid[next_i][next_j] = "@"
            i = next_i
            j = next_j

    result = 0
    for i in range(nr):
        for j in range(nc):
            if grid[i][j] == "O":
                result += i * 100 + j
    print(result)


def solve2(grid: list[list[str]], movement: str):
    nr = len(grid)
    nc = len(grid[0])
    start: tuple[int, int] | None = None
    for i in range(nr):
        if start is not None:
            break
        for j in range(nc):
            if start is not None:
                break
            if grid[i][j] == "@":
                start = (i, j)
    assert start is not None

    i = start[0]
    j = start[1]
    for index, move in enumerate(movement):
        di, dj = get_direction(move)
        up_down = di != 0
        if up_down:
            next_i = i + di
            next_j = j + dj
            if not (0 <= next_i < nr and 0 <= next_j < nc):
                continue
            if grid[next_i][next_j] == "#":
                continue
            if grid[next_i][next_j] == ".":
                grid[next_i][next_j] = "@"
                grid[i][j] = "."
                i = next_i
                j = next_j
                continue

            rows: list[set[tuple[int, int]]] = []
            if grid[next_i][next_j] == "[":
                curr = [(next_i, next_j), (next_i, next_j + 1)]
            else:
                curr = [(next_i, next_j), (next_i, next_j - 1)]
            rows.append(set(curr))
            while True:
                next_row: list[tuple[int, int]] = []
                wall = False
                empty = True
                for tmp_i, tmp_j in curr:
                    tmp_i2 = tmp_i + di
                    tmp_j2 = tmp_j + dj
                    if grid[tmp_i2][tmp_j2] == "#":
                        wall = True
                        break
                    if grid[tmp_i2][tmp_j2] == "[":
                        next_row.extend([(tmp_i2, tmp_j2), (tmp_i2, tmp_j2 + 1)])
                        empty = False
                    elif grid[tmp_i2][tmp_j2] == "]":
                        next_row.extend([(tmp_i2, tmp_j2), (tmp_i2, tmp_j2 - 1)])
                        empty = False
                rows.append(set(next_row))
                curr = next_row

                if wall:
                    break
                if empty:
                    while rows:
                        row = rows.pop()
                        for tmp_i, tmp_j in row:
                            grid[tmp_i + di][tmp_j + dj] = grid[tmp_i][tmp_j]
                            grid[tmp_i][tmp_j] = "."

                    grid[next_i][next_j] = "@"
                    grid[i][j] = "."
                    i = next_i
                    j = next_j
                    break
        else:
            next_i = i + di
            next_j = j + dj
            if not (0 <= next_i < nr and 0 <= next_j < nc):
                continue
            if grid[next_i][next_j] == "#":
                continue
            if grid[next_i][next_j] == ".":
                grid[next_i][next_j] = "@"
                grid[i][j] = "."
                i = next_i
                j = next_j
                continue
            next_i2 = next_i
            next_j2 = next_j
            while 0 <= next_i2 + di < nr and 0 <= next_j2 < nc:
                next_i2 += di
                next_j2 += dj
                if grid[next_i2][next_j2] not in "[]":
                    break

            if grid[next_i2][next_j2] == "#":
                continue
            while next_i2 != next_i or next_j2 != next_j:
                grid[next_i2][next_j2] = grid[next_i2 - di][next_j2 - dj]
                next_i2 -= di
                next_j2 -= dj
            grid[next_i][next_j] = "@"
            grid[i][j] = "."
            i = next_i
            j = next_j

    result = 0
    for i in range(nr):
        for j in range(nc):
            if grid[i][j] == "[":
                result += i * 100 + j
    print(result)


def main():
    data = read_data("day15.txt")
    blocks = data.rstrip().split("\n\n")

    grid = [list(line) for line in blocks[0].split("\n")]
    grid2: list[list[str]] = []
    for row in grid:
        grid2.append([])
        for col in row:
            if col == "#":
                grid2[-1].extend(["#", "#"])
            elif col == "O":
                grid2[-1].extend(["[", "]"])
            elif col == ".":
                grid2[-1].extend([".", "."])
            elif col == "@":
                grid2[-1].extend(["@", "."])

    movement = "".join(blocks[1].split("\n"))
    solve1(grid, movement)
    solve2(grid2, movement)


if __name__ == "__main__":
    main()
