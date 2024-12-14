import copy

from helper import read_data


def check(positions: list[list[int]]) -> bool:
    seen: set[tuple[int, int]] = set()
    for x, y in positions:
        if (x, y) in seen:
            return False
        seen.add((x, y))
    return True


def main():
    data = read_data("day14.txt")
    lines = data.rstrip().split("\n")
    positions: list[list[int]] = []
    velocities: list[list[int]] = []
    for line in lines:
        p, v = line.split(" ")
        positions.append(list(map(int, p[2:].split(","))))
        velocities.append(list(map(int, v[2:].split(","))))
    positions_copy = copy.deepcopy(positions)

    ny = 103
    nx = 101
    for _ in range(100):
        for i, (v_x, v_y) in enumerate(velocities):
            x = (positions[i][0] + v_x + nx) % nx
            y = (positions[i][1] + v_y + ny) % ny
            positions[i] = [x, y]
    result = [[0, 0], [0, 0]]
    for x, y in positions:
        if x == nx // 2 or y == ny // 2:
            continue
        result[int(x / nx * 2)][int(y / ny * 2)] += 1
    print(result[0][0] * result[0][1] * result[1][0] * result[1][1])

    result2 = 0
    while True:
        result2 += 1
        if check(positions_copy):
            print(result2)
            break
        for i, (v_x, v_y) in enumerate(velocities):
            x = (positions_copy[i][0] + v_x + nx) % nx
            y = (positions_copy[i][1] + v_y + ny) % ny
            positions_copy[i] = [x, y]


if __name__ == "__main__":
    main()
