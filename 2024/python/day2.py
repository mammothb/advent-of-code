from pathlib import Path


def is_valid(levels: list[int]) -> bool:
    diff = levels[0] - levels[1]
    if diff == 0:
        return False
    sign = diff // abs(diff)

    n = len(levels)
    for i in range(n - 1):
        diff = levels[i] - levels[i + 1]
        if diff == 0 or diff // abs(diff) != sign or not 1 <= abs(diff) <= 3:
            return False
    return True


def main():
    with open(Path(__file__).resolve().parents[1] / "data" / "day2.txt") as infile:
        result = 0
        result2 = 0
        for line in infile.readlines():
            levels = list(map(int, line.strip().split(" ")))

            if is_valid(levels):
                result += 1
            elif any(
                is_valid(levels[:i] + levels[i + 1 :]) for i, _ in enumerate(levels)
            ):
                result2 += 1

        print(result)
        print(result + result2)


if __name__ == "__main__":
    main()
