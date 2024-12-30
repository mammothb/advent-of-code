import functools
import itertools

from aoc_helper.io import IoOutputType, read_data


def solve(field: str, record: tuple[int, ...]) -> int:
    @functools.cache
    def dp(i_field: int, i_record: int, result: int = 0) -> int:
        n_field = len(field)
        n_record = len(record)
        if i_field >= n_field:
            return int(i_record == n_record)

        if field[i_field] in ".?":
            result += dp(i_field + 1, i_record)

        if i_record == n_record:
            return result

        for i in range(i_field, i_field + record[i_record]):
            if i >= n_field:
                break
            if field[i] == ".":
                break
        else:
            if (i := i_field + record[i_record]) >= n_field or field[i] != "#":
                result += dp(i + 1, i_record + 1)

        return result

    return dp(0, 0)


def main():
    data = read_data("day12.txt", IoOutputType.LINE)
    result = 0
    result2 = 0
    for parts in map(lambda l: l.rstrip().split(" "), data):
        record = tuple(map(int, parts[1].split(",")))
        result += solve(parts[0], record)
        result2 += solve("?".join(itertools.repeat(parts[0], 5)), record * 5)
    print(result)
    print(result2)


if __name__ == "__main__":
    main()
