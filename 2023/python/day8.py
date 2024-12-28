import math
import re

from aoc_helper.io import IoOutputType, read_data

NODE_PATTERN = re.compile(r"(\w+) = \((\w+), (\w+)\)")


def count_cycle(start: str, graph: dict[str, dict[str, str]], movements: str) -> int:
    n = len(movements)
    result = 0
    i = 0
    curr = start
    while not curr.endswith("Z"):
        curr = graph[curr][movements[i]]
        result += 1
        i = (i + 1) % n
    return result


def main():
    data = read_data("day8.txt", IoOutputType.BLOCK)
    graph: dict[str, dict[str, str]] = {}
    for line in data[1].split("\n"):
        res = NODE_PATTERN.search(line)
        assert res is not None
        root = res.group(1)
        left = res.group(2)
        right = res.group(3)
        graph[root] = {"L": left, "R": right}

    n = len(data[0])
    result = 0
    i = 0
    curr = "AAA"
    while curr != "ZZZ":
        curr = graph[curr][data[0][i]]
        result += 1
        i = (i + 1) % n
    print(result)

    starts = [node for node in graph if node.endswith("A")]
    print(math.lcm(*[count_cycle(start, graph, data[0]) for start in starts]))


if __name__ == "__main__":
    main()
