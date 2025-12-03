from helper import read_data


def main():
    data = read_data("day3.txt")
    count = 0
    for line in data.strip().split("\n"):
        n = len(line)
        suffix_max = [0] * n
        suffix_max[-1] = -1
        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(int(line[i + 1]), suffix_max[i + 1])
        large = 0
        for i in range(n - 1):
            if suffix_max[i] == -1:
                continue
            if (candidate := int(line[i]) * 10 + suffix_max[i]) > large:
                large = candidate
        count += large
    print(count)


def main2():
    data = read_data("day3.txt")
    count = 0
    k = 12
    for line in data.strip().split("\n"):
        n = len(line)
        to_remove = n - k
        stack = []
        for d in line:
            while stack and to_remove > 0 and stack[-1] < d:
                stack.pop()
                to_remove -= 1
            stack.append(d)
        large = int("".join(stack[:k]))
        count += large
    print(count)


if __name__ == "__main__":
    main()
    main2()
