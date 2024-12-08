import collections

from helper import read_data


def main():
    data = read_data("day8.txt")
    lines = data.rstrip().split("\n")
    nr = len(lines)
    nc = len(lines[0])
    freq_to_locs: dict[str, list[tuple[int, int]]] = collections.defaultdict(list)
    for i in range(nr):
        for j in range(nc):
            if lines[i][j] != ".":
                freq_to_locs[lines[i][j]].append((i, j))

    antinodes: set[tuple[int, int]] = set()
    for locs in freq_to_locs.values():
        n = len(locs)
        for k1 in range(n):
            for k2 in range(k1 + 1, n):
                di = locs[k2][0] - locs[k1][0]
                dj = locs[k2][1] - locs[k1][1]

                i_a1 = locs[k1][0] - di
                j_a1 = locs[k1][1] - dj
                if 0 <= i_a1 < nr and 0 <= j_a1 < nc:
                    antinodes.add((i_a1, j_a1))
                i_a2 = locs[k2][0] + di
                j_a2 = locs[k2][1] + dj
                if 0 <= i_a2 < nr and 0 <= j_a2 < nc:
                    antinodes.add((i_a2, j_a2))
    print(len(antinodes))

    antinodes2: set[tuple[int, int]] = set()
    for locs in freq_to_locs.values():
        n = len(locs)
        for k1 in range(n):
            for k2 in range(k1 + 1, n):
                added = False
                di = locs[k2][0] - locs[k1][0]
                dj = locs[k2][1] - locs[k1][1]

                i_a1 = locs[k1][0] - di
                j_a1 = locs[k1][1] - dj
                while 0 <= i_a1 < nr and 0 <= j_a1 < nc:
                    antinodes2.add((i_a1, j_a1))
                    added = True
                    i_a1 -= di
                    j_a1 -= dj

                i_a2 = locs[k2][0] + di
                j_a2 = locs[k2][1] + dj
                while 0 <= i_a2 < nr and 0 <= j_a2 < nc:
                    antinodes2.add((i_a2, j_a2))
                    added = True
                    i_a2 += di
                    j_a2 += dj
                if added:
                    antinodes2.add(locs[k1])
                    antinodes2.add(locs[k2])
    print(len(antinodes2))


if __name__ == "__main__":
    main()
