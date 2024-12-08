import collections

from helper import read_data


def valid(graph: dict[str, set[str]], update: list[str]) -> bool:
    seen: set[str] = set()
    for elem in update:
        if len(seen & graph[elem]) > 0:
            return False
        seen.add(elem)
    return True


def fix(graph: dict[str, set[str]], update: list[str]) -> int:
    result: list[str] = []
    update_set = set(update)
    while update_set:
        for elem in list(update_set):
            if len(update_set & graph[elem]) == 0:
                result.append(elem)
                update_set.remove(elem)
    return int(result[len(result) // 2])


def main():
    data = read_data("day5.txt")
    lines = data.rstrip().split("\n")
    orderings: list[tuple[str, str]] = []
    updates: list[list[str]] = []
    for line in lines:
        if not line:
            continue
        try:
            u, v = line.split("|")
            orderings.append((u, v))
        except:
            updates.append(line.split(","))

    graph: dict[str, set[str]] = collections.defaultdict(set)
    for u, v in orderings:
        graph[u].add(v)
    result = 0
    result2 = 0
    for update in updates:
        if valid(graph, update):
            result += int(update[len(update) // 2])
        else:
            result2 += fix(graph, update)
    print(result)
    print(result2)


if __name__ == "__main__":
    main()
