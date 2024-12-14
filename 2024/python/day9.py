from dataclasses import dataclass

from helper import read_data


@dataclass
class Item:
    pos: int
    size: int

    @property
    def val(self) -> int:
        return (2 * self.pos + self.size - 1) * self.size // 2


def main():
    data = read_data("day9.txt")
    data = data.rstrip()
    disk: list[str] = []
    free = False
    idx = 0
    for c in data:
        for _ in range(int(c)):
            disk.append("." if free else str(idx))
        free = not free
        if not free:
            idx += 1

    l = 0
    r = len(disk) - 1
    while l < r:
        if disk[l] == "." and disk[r] != ".":
            disk[l] = disk[r]
            disk[r] = "."
            l += 1
            r -= 1
        elif disk[l] != ".":
            l += 1
        elif disk[r] == ".":
            r -= 1

    result = 0
    for i, n in enumerate(disk):
        if n == ".":
            break
        result += i * int(n)
    print(result)

    items: list[Item] = []
    pos = 0
    for size in map(int, data):
        items.append(Item(pos, size))
        pos += size

    for file in items[::-2]:
        for free in items[1::2]:
            if free.pos <= file.pos and free.size >= file.size:
                file.pos = free.pos
                free.pos += file.size
                free.size -= file.size
    result2 = sum(index * item.val for index, item in enumerate(items[::2]))
    print(result2)


if __name__ == "__main__":
    main()
