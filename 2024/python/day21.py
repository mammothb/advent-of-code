import collections
from typing import Literal, overload

from helper import read_data

CoordType = tuple[int, int]


def parse_pad(
    pad: str, coord_to_key: dict[CoordType, str], key_to_coord: dict[str, CoordType]
):
    for i, line in enumerate(pad.split(" ")):
        for j, val in enumerate(line):
            if val == "#":
                continue
            coord_to_key[(i, j)] = val
            key_to_coord[val] = (i, j)


def step(
    start: str,
    end: str,
    coord_to_key: dict[CoordType, str],
    key_to_coord: dict[str, CoordType],
) -> str:
    start_i, start_j = key_to_coord[start]
    end_i, end_j = key_to_coord[end]
    di = end_i - start_i
    dj = end_j - start_j
    if di > 0:
        move_i = "v" * di
    elif di < 0:
        move_i = "^" * -di
    else:
        move_i = ""
    if dj > 0:
        move_j = ">" * dj
    elif dj < 0:
        move_j = "<" * -dj
    else:
        move_j = ""
    if dj > 0 and (end_i, start_j) in coord_to_key:
        return f"{move_i}{move_j}A"
    if (start_i, end_j) in coord_to_key:
        return f"{move_j}{move_i}A"
    return f"{move_i}{move_j}A"


@overload
def get_route(
    path: str,
    coord_to_key: dict[CoordType, str],
    key_to_coord: dict[str, CoordType],
    as_counter: Literal[True],
) -> collections.Counter[str]: ...
@overload
def get_route(
    path: str,
    coord_to_key: dict[CoordType, str],
    key_to_coord: dict[str, CoordType],
    as_counter: Literal[False],
) -> str: ...
def get_route(
    path: str,
    coord_to_key: dict[CoordType, str],
    key_to_coord: dict[str, CoordType],
    as_counter: bool,
) -> str | collections.Counter[str]:
    result: list[str] = []
    start = "A"
    for end in path:
        result.append(step(start, end, coord_to_key, key_to_coord))
        start = end
    if as_counter:
        return collections.Counter(result)
    return "".join(result)


def main():
    data = read_data("day21.txt")
    lines = data.rstrip().split("\n")
    num_coord_to_key: dict[CoordType, str] = {}
    num_key_to_coord: dict[str, CoordType] = {}
    dir_coord_to_key: dict[CoordType, str] = {}
    dir_key_to_coord: dict[str, CoordType] = {}
    parse_pad("789 456 123 #0A", num_coord_to_key, num_key_to_coord)
    parse_pad("#^A <v>", dir_coord_to_key, dir_key_to_coord)

    num_routes = [
        get_route(line, num_coord_to_key, num_key_to_coord, False) for line in lines
    ]
    dir_routes = [
        get_route(route, dir_coord_to_key, dir_key_to_coord, False)
        for route in num_routes
    ]
    dir_routes2 = [
        get_route(route, dir_coord_to_key, dir_key_to_coord, False)
        for route in dir_routes
    ]
    result = sum(len(route) * int(code[:-1]) for route, code in zip(dir_routes2, lines))
    print(result)

    route_counters = [collections.Counter([route]) for route in num_routes]
    for _ in range(25):
        new_routes: list[collections.Counter[str]] = []
        for counter in route_counters:
            new_counter: collections.Counter[str] = collections.Counter()
            for route, count in counter.items():
                tmp_counter = get_route(route, dir_coord_to_key, dir_key_to_coord, True)
                for k in tmp_counter:
                    tmp_counter[k] *= count
                new_counter += tmp_counter
            new_routes.append(new_counter)
        route_counters = new_routes
    result2 = sum(
        sum(len(k) * v for k, v in route.items()) * int(code[:-1])
        for route, code in zip(route_counters, lines)
    )
    print(result2)


if __name__ == "__main__":
    main()
