import collections

from helper import read_data


def solve2(graph: dict[str, set[str]]) -> set[str]:
    def dfs(
        clique: set[str],
        candidates: set[str],
        seen: set[str],
        graph: dict[str, set[str]],
        best: set[str],
    ):
        if len(candidates) == 0 and len(seen) == 0:
            if len(clique) > len(best):
                best.clear()
                for node in clique:
                    best.add(node)
            return
        for node in list(candidates):
            clique.add(node)
            dfs(clique, candidates & graph[node], seen & graph[node], graph, best)
            clique.remove(node)
            candidates.remove(node)
            seen.add(node)

    result: set[str] = set()
    dfs(set(), set(graph), set(), graph, result)
    return result


def main():
    data = read_data("day23.txt")
    graph: dict[str, set[str]] = collections.defaultdict(set)
    for line in data.rstrip().split("\n"):
        a, b = line.split("-")
        graph[a].add(b)
        graph[b].add(a)
    seen: set[tuple[str, ...]] = set()
    result = 0
    for node in graph:
        for next_node in graph[node]:
            for next_next_node in graph[next_node]:
                nodes = tuple(sorted([node, next_node, next_next_node]))
                if nodes in seen:
                    continue
                if node in graph[next_next_node] and any(
                    n.startswith("t") for n in nodes
                ):
                    result += 1
                seen.add(nodes)
    print(result)

    result2 = solve2(graph)
    print(",".join(sorted(list(result2))))


if __name__ == "__main__":
    main()
