import collections

from aoc_helper.io import IoOutputType, read_data


def score(win: set[int], buy: set[int]) -> int:
    result = win & buy
    return 0 if not result else 2 ** (len(result) - 1)


def main():
    data = read_data("day4.txt", IoOutputType.LINE)
    result = 0
    result2 = 0
    copies: collections.deque[int] = collections.deque()
    for line in data:
        parts = line.rstrip().split(":")[-1].split(" | ")
        win = set(map(int, parts[0].split()))
        buy = set(map(int, parts[1].split()))
        result += score(win, buy)

        copy = (copies.popleft() + 1) if copies else 1
        match = len(win & buy)
        for i in range(match):
            if i >= len(copies):
                copies.append(copy)
            else:
                copies[i] += copy
        result2 += 1 + match * copy
    print(result)
    print(result2)


if __name__ == "__main__":
    main()
