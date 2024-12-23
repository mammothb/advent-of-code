import collections

from helper import read_data


def solve(towels: list[str], design: str, memo: dict[str, int]) -> int:
    if design in memo:
        return memo[design]
    result = 0
    if not design:
        result = 1
    for towel in towels:
        if design.startswith(towel):
            result += solve(towels, design[len(towel) :], memo)
    memo[design] = result
    return result


def main():
    data = read_data("day19.txt")
    # data = read_data("day19_easy.txt")
    parts = data.rstrip().split("\n\n")
    towels = parts[0].split(", ")
    designs = parts[1].split("\n")

    memo: dict[str, int] = {}
    result = 0
    result2 = 0
    for design in designs:
        ways = solve(towels, design, memo)
        if ways > 0:
            result += 1
        result2 += ways

    print(result)
    print(result2)


if __name__ == "__main__":
    main()
