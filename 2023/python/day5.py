import functools
import itertools
from collections.abc import Iterable
from dataclasses import dataclass

from aoc_helper.io import IoOutputType, read_data


@dataclass
class Map:
    mappings: list[tuple[int, int, int]]

    @classmethod
    def from_block(cls, block: str) -> "Map":
        mappings: list[tuple[int, int, int]] = []
        for line in block.split("\n")[1:]:
            mapping = map(int, line.split(" "))
            mappings.append((next(mapping), next(mapping), next(mapping)))

        return cls(mappings=mappings)


def lookup(seed: int, mapping: Map) -> int:
    for dest, src, size in mapping.mappings:
        offset = seed - src
        if 0 <= offset < size:
            return dest + offset
    return seed


def lookup2(
    seeds: Iterable[tuple[int, ...]], mapping: Map
) -> Iterable[tuple[int, ...]]:
    for seed, seed_size in seeds:
        while seed_size > 0:
            for dest, src, size in mapping.mappings:
                offset = seed - src
                if 0 <= offset < size:
                    size = min(size - offset, seed_size)
                    seed += size
                    seed_size -= size
                    yield dest + offset, size
                    break
            else:
                yield seed, seed_size
                break


def main():
    data = read_data("day5.txt", IoOutputType.BLOCK)
    seeds = map(int, data[0].split(" ")[1:])
    maps = [Map.from_block(block) for block in data[1:]]
    result = min(functools.reduce(lookup, maps, seed) for seed in seeds)
    print(result)

    seeds = map(int, data[0].split(" ")[1:])
    print(min(functools.reduce(lookup2, maps, itertools.batched(seeds, n=2)))[0])


if __name__ == "__main__":
    main()
