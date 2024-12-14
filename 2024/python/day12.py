from helper import read_data


def solve(
    grid: dict[complex, str],
    seen: set[complex],
    node: complex,
    color: str,
    prev_d: complex,
) -> tuple[int, int, int]:
    if grid[node] != color:
        if (
            grid[node + prev_d * 1j] == color
            or grid[node - prev_d + prev_d * 1j] != color
        ):
            return 0, 1, 1
        return 0, 1, 0
    if node in seen:
        return 0, 0, 0
    seen.add(node)
    area = 1
    perimeter = 0
    side = 0
    for d in (1, -1, 1j, -1j):
        a, p, s = solve(grid, seen, node + d, color, d)
        area += a
        perimeter += p
        side += s
    return area, perimeter, side


def main():
    data = read_data("day12.txt")
    lines = data.rstrip().split("\n")
    nr = len(lines)
    nc = len(lines[0])

    grid: dict[complex, str] = {}
    for i, row in enumerate(lines):
        for j, col in enumerate(row):
            grid[i + j * 1j] = col
    for i in range(-1, nr + 1):
        grid[i - 1 * 1j] = "#"
        grid[i + nc * 1j] = "#"
    for j in range(-1, nc + 1):
        grid[-1 + j * 1j] = "#"
        grid[nr + j * 1j] = "#"
    seen: set[complex] = set()

    result = 0
    result2 = 0
    for node in grid:
        if node not in seen and grid[node] != "#":
            area, perimeter, side = solve(grid, seen, node, grid[node], 1)
            result += area * perimeter
            result2 += area * side
    print(result)
    print(result2)


if __name__ == "__main__":
    main()
