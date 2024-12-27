from typing import Callable

from aoc_helper.io import IoOutputType, read_data

DIGIT = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def is_digit(s: str, check: Callable[[str, str], bool]) -> int | None:
    for k, v in DIGIT.items():
        if check(s, k):
            return v


def main():
    data = read_data("day1.txt", IoOutputType.LINE)
    result = 0
    for line in data:
        n = len(line)
        first = int(next(line[i] for i in range(n) if line[i].isdigit()))
        last = int(next(line[i] for i in reversed(range(n)) if line[i].isdigit()))
        result += first * 10 + last
    print(result)

    result2 = 0
    for line in data:
        n = len(line)
        for i in range(n):
            if line[i].isdigit():
                first = int(line[i])
                break
            elif (val := is_digit(line[i:], str.startswith)) is not None:
                first = val
                break
        else:
            raise ValueError
        for i in reversed(range(n)):
            if line[i].isdigit():
                last = int(line[i])
                break
            elif (val := is_digit(line[: i + 1], str.endswith)) is not None:
                last = val
                break
        else:
            raise ValueError
        result2 += first * 10 + last
    print(result2)


if __name__ == "__main__":
    main()
