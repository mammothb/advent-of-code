import re

from helper import read_data


def main():
    data = read_data("day13.txt")
    result = 0
    result2 = 0
    for block in data.rstrip().split("\n\n"):
        btn_a, btn_b, prize = block.split("\n")
        match_a = re.match(r"Button A: X\+(\d+), Y\+(\d+)", btn_a)
        assert match_a is not None
        a_x = int(match_a.group(1))
        a_y = int(match_a.group(2))
        match_b = re.match(r"Button B: X\+(\d+), Y\+(\d+)", btn_b)
        assert match_b is not None
        b_x = int(match_b.group(1))
        b_y = int(match_b.group(2))
        match_p = re.match(r"Prize: X=(\d+), Y=(\d+)", prize)
        assert match_p is not None
        p_x = int(match_p.group(1))
        p_y = int(match_p.group(2))
        p_x2 = int(match_p.group(1)) + 10000000000000
        p_y2 = int(match_p.group(2)) + 10000000000000

        den = a_x * b_y - b_x * a_y
        if den == 0:
            continue
        a = (p_x * b_y - b_x * p_y) / den
        b = (a_x * p_y - p_x * a_y) / den
        if a == int(a) and b == int(b):
            result += 3 * int(a) + int(b)

        a2 = (p_x2 * b_y - b_x * p_y2) / den
        b2 = (a_x * p_y2 - p_x2 * a_y) / den
        if a2 == int(a2) and b2 == int(b2):
            result2 += 3 * int(a2) + int(b2)

    print(result)
    print(result2)


if __name__ == "__main__":
    main()
