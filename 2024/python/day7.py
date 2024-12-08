from pathlib import Path


def valid(answer: int, nums: list[int], start: int, n: int, curr: int) -> bool:
    if start == n:
        return curr == answer
    if curr > answer:
        return False
    return valid(answer, nums, start + 1, n, curr + nums[start]) or valid(
        answer, nums, start + 1, n, curr * nums[start]
    )


def valid2(answer: int, nums: list[int], start: int, n: int, curr: int) -> bool:
    if start == n:
        return curr == answer
    if curr > answer:
        return False
    return (
        valid2(answer, nums, start + 1, n, curr + nums[start])
        or valid2(answer, nums, start + 1, n, curr * nums[start])
        or valid2(answer, nums, start + 1, n, int(str(curr) + str(nums[start])))
    )


def main():
    with open(Path(__file__).resolve().parents[1] / "data" / "day7.txt") as infile:
        lines = [line.rstrip() for line in infile.readlines()]
    result = 0
    result2 = 0
    for line in lines:
        answer, parts = line.split(": ")
        answer = int(answer)
        nums = list(map(int, parts.split(" ")))
        if valid(answer, nums, 0, len(nums), 0):
            result += answer
        if valid2(answer, nums, 0, len(nums), 0):
            result2 += answer
    print(result)
    print(result2)


if __name__ == "__main__":
    main()
