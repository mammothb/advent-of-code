import re

from aoc_helper.io import IoOutputType, read_data


def main():
    data = read_data("day6.txt", IoOutputType.LINE)
    time_result = re.search(r"Time:\s+(\d+\s+\d+\s+\d+\s+\d+)", data[0])
    dist_result = re.search(r"Distance:\s+(\d+\s+\d+\s+\d+\s+\d+)", data[1])
    assert time_result is not None
    assert dist_result is not None
    times = list(map(int, time_result.group(1).split()))
    distances = list(map(int, dist_result.group(1).split()))

    result = 1
    for time, distance in zip(times, distances):
        speed = 1
        num_ways = 0
        while speed < time:
            if speed * (time - speed) > distance:
                num_ways += 1
            speed += 1
        result *= num_ways
    print(result)

    time = int("".join(map(str, times)))
    distance = int("".join(map(str, distances)))
    l = 1
    r = time - 1
    while l <= r:
        mid = l + (r - l) // 2
        if mid * (time - mid) > distance:
            r = mid - 1
        else:
            l = mid + 1

    start = l
    r = time - 1
    while l <= r:
        mid = l + (r - l) // 2
        if mid * (time - mid) <= distance:
            r = mid - 1
        else:
            l = mid + 1
    print(l - start)


if __name__ == "__main__":
    main()
