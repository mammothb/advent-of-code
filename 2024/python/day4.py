import collections
from pathlib import Path


def search(data: list[str], nr: int, nc: int, i: int, j: int) -> int:
    if data[i][j] != "X":
        return 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    chars = "MAS"
    result = 0
    for di, dj in directions:
        next_i = i
        next_j = j
        for k in range(3):
            next_i += di
            next_j += dj
            if not (0 <= next_i < nr and 0 <= next_j < nc):
                break
            if data[next_i][next_j] != chars[k]:
                break
        else:
            result += 1
    return result


def search2(data: list[str], nr: int, nc: int, i: int, j: int) -> int:
    if data[i][j] != "A":
        return 0
    directions = [[(-1, -1), (1, 1)], [(-1, 1), (1, -1)]]
    result = 0
    for d in directions:
        counter = collections.defaultdict(int)
        for di, dj in d:
            next_i = i + di
            next_j = j + dj
            if not (0 <= next_i < nr and 0 <= next_j < nc):
                break
            counter[data[next_i][next_j]] += 1
        else:
            if counter["M"] == 1 and counter["S"] == 1:
                result += 1

    return int(result == 2)


def main():
    with open(Path(__file__).resolve().parents[1] / "data" / "day4.txt") as infile:
        data = [line.strip() for line in infile.readlines()]
    nr = len(data)
    nc = len(data[0])
    result = 0
    result2 = 0
    for i in range(nr):
        for j in range(nc):
            result += search(data, nr, nc, i, j)
            result2 += search2(data, nr, nc, i, j)
    print(result)
    print(result2)


if __name__ == "__main__":
    main()
