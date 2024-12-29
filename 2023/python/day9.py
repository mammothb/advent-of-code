from aoc_helper.algorithm import pairwise_differences
from aoc_helper.io import IoOutputType, read_data


def get_next_value(nums: list[int]) -> int:
    diffs = [pairwise_differences(nums, reverse=True)]
    while not all(d == 0 for d in diffs[-1]):
        diffs.append(pairwise_differences(diffs[-1], reverse=True))

    last = 0
    while diffs:
        prev_diffs = diffs.pop()
        last += prev_diffs[-1]

    return nums[-1] + last


def get_prev_value(nums: list[int]) -> int:
    diffs = [pairwise_differences(nums, reverse=True)]
    while not all(d == 0 for d in diffs[-1]):
        diffs.append(pairwise_differences(diffs[-1], reverse=True))

    first = 0
    while diffs:
        prev_diffs = diffs.pop()
        first = prev_diffs[0] - first

    return nums[0] - first


def main():
    data = read_data("day9.txt", IoOutputType.LINE)
    result = 0
    result2 = 0
    for line in data:
        result += get_next_value(list(map(int, line.rstrip().split())))
        result2 += get_prev_value(list(map(int, line.rstrip().split())))
    print(result)
    print(result2)


if __name__ == "__main__":
    main()
