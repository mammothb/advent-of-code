import collections
from pathlib import Path


def main():
    with open(Path(__file__).resolve().parents[1] / "data" / "day1.txt") as infile:
        l_arr: list[int] = []
        r_arr: list[int] = []
        for line in infile.readlines():
            l, r = list(map(int, line.rstrip().split()))
            l_arr.append(l)
            r_arr.append(r)

        l_arr = sorted(l_arr)
        r_arr = sorted(r_arr)
        result = 0
        for l, r in zip(l_arr, r_arr):
            result += abs(l - r)
        print(result)

        counter = collections.Counter(r_arr)
        result2 = 0
        for l in l_arr:
            result2 += l * counter[l]
        print(result2)


if __name__ == "__main__":
    main()
