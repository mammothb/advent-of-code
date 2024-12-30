import collections
import functools

from aoc_helper.io import IoOutputType, read_data


def hash_char(curr: int, c: str) -> int:
    return ((curr + ord(c)) * 17) % 256


def hash_word(word: str) -> int:
    return functools.reduce(hash_char, word, 0)


def main():
    data = read_data("day15.txt", IoOutputType.STRING)
    result = 0
    boxes: collections.defaultdict[int, dict[str, int]] = collections.defaultdict(dict)
    for part in data.rstrip().split(","):
        result += hash_word(part)

        if "-" in part:
            label = part[:-1]
            _ = boxes[hash_word(label)].pop(label, None)
        elif "=" in part:
            label, focal_length = part.split("=")
            boxes[hash_word(label)][label] = int(focal_length)
    print(result)
    print(
        sum(
            (i + 1) * j * focal_length
            for i, box in boxes.items()
            for j, focal_length in enumerate(box.values(), 1)
        )
    )


if __name__ == "__main__":
    main()
