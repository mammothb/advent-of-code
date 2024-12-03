import re
from pathlib import Path

mul_exp = re.compile(r"mul\((\d+),(\d+)\)")


def solve(line: str) -> int:
    result = 0
    for num1, num2 in re.findall(mul_exp, line):
        result += int(num1) * int(num2)
    return result


def main():
    with open(Path(__file__).resolve().parents[1] / "data" / "day3.txt") as infile:
        result = 0
        result2 = 0
        data = "do()" + infile.read().replace("\n", " ") + "don't()"
        result = solve(data)
        data = "".join(re.findall(r"do\(\)(.*?)don't\(\)", data))
        result2 = solve(data)

        print(result)
        print(result2)


if __name__ == "__main__":
    main()
