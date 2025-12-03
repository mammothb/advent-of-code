from helper import read_data


def main():
    data = read_data("day2.txt")
    count = 0
    for part in data.strip().split(","):
        l, r = map(int, part.split("-"))
        min_len = len(str(l))
        max_len = len(str(r))
        for length in range(min_len, max_len + 1):
            seen = set()
            for repeat in range(2, length + 1):
                if length % repeat != 0:
                    continue
                unit_len = length // repeat
                start = 10 ** (unit_len - 1)
                end = 10**unit_len - 1
                for half in range(start, end + 1):
                    n = int(str(half) * repeat)
                    if n in seen:
                        continue
                    if n < l:
                        continue
                    if n > r:
                        break
                    seen.add(n)
                    count += n
    print(count)


if __name__ == "__main__":
    main()
