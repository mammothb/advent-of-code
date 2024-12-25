import collections

from helper import read_data


def read_block(lines: list[str]) -> list[int]:
    nr = len(lines)
    nc = len(lines[0])
    result = [nr - 1 - [lines[i][j] for i in range(nr)].count(".") for j in range(nc)]
    return result


class TrieNode:
    def __init__(self):
        self.children: dict[int, TrieNode] = {}
        self.count = 0
        self.is_end = False

    def insert(self, word: list[int]):
        root = self
        for c in word:
            if c not in root.children:
                root.children[c] = TrieNode()
            root = root.children[c]
        root.count += 1
        root.is_end = True

    def find(self, word: list[int]):
        result = 0
        queue: collections.deque[TrieNode] = collections.deque([self])
        for c in word:
            n_queue = len(queue)
            for _ in range(n_queue):
                node = queue.popleft()
                for pin in node.children:
                    if c + pin <= 5:
                        queue.append(node.children[pin])
        result = sum(node.count for node in queue)
        return result


def main():
    data = read_data("day25.txt")
    locks: list[list[int]] = []
    keys: list[list[int]] = []
    for block in data.rstrip().split("\n\n"):
        lines = block.split("\n")
        if all(c == "#" for c in lines[0]):
            locks.append(read_block(lines))
        else:
            keys.append(read_block(lines))

    root = TrieNode()
    for key in keys:
        root.insert(key)

    result = 0
    for lock in locks:
        result += root.find(lock)
    print(result)


if __name__ == "__main__":
    main()
