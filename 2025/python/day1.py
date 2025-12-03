from helper import read_data


def main():
    data = read_data("day1.txt")
    # data = read_data("day1_test.txt")
    curr = 50
    count = 0
    count2 = 0
    for line in (line for line in data.split("\n") if line):
        d = -1 if line[0] == "L" else 1
        num = int(line[1:])

        count2 += num // 100
        num %= 100

        prev = curr
        curr += d * num
        if prev != 0 and (curr > 100 or curr < 0):
            count2 += 1

        curr %= 100
        if curr == 0:
            count += 1
            count2 += 1

    print(count)
    print(count2)


if __name__ == "__main__":
    main()
