from helper import read_data


def main():
    data = read_data("day11.txt")
    data = list(map(int, data.rstrip().split(" ")))

    stones = data.copy()
    for _ in range(25):
        curr: list[int] = []
        for stone in stones:
            if stone == 0:
                curr.append(1)
            else:
                stone_str = str(stone)
                n = len(stone_str)
                if n % 2 == 0:
                    curr.append(int(stone_str[: n // 2]))
                    curr.append(int(stone_str[n // 2 :]))
                else:
                    curr.append(stone * 2024)
        stones = curr
    print(len(stones))

    counter = {num: 1 for num in data}
    for _ in range(75):
        curr: dict[int, int] = {}
        for num in list(counter.keys()):
            if num == 0:
                curr[1] = curr.get(1, 0) + counter[num]
            else:
                stone_str = str(num)
                n = len(stone_str)
                if n % 2 == 0:
                    left = int(stone_str[: n // 2])
                    right = int(stone_str[n // 2 :])
                    curr[left] = curr.get(left, 0) + counter[num]
                    curr[right] = curr.get(right, 0) + counter[num]
                else:
                    curr[num * 2024] = curr.get(num * 2024, 0) + counter[num]
        counter = curr
    print(sum(counter.values()))


if __name__ == "__main__":
    main()
