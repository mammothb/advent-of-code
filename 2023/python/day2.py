import re
from dataclasses import dataclass, field

from aoc_helper.io import IoOutputType, read_data


@dataclass
class Draw:
    blue: int = 0
    green: int = 0
    red: int = 0


@dataclass
class Game:
    id: int
    draws: list[Draw] = field(default_factory=list)


def is_valid(draw: Draw, max_blue: int, max_green: int, max_red: int) -> bool:
    return draw.blue <= max_blue and draw.green <= max_green and draw.red <= max_red


def find_min_possible(draws: list[Draw]) -> Draw:
    result = Draw(
        blue=max(draw.blue for draw in draws),
        green=max(draw.green for draw in draws),
        red=max(draw.red for draw in draws),
    )
    return result


def parse_game(s: str) -> Game:
    result = re.search(r"^Game (\d+): (.*)$", s)
    assert result is not None
    game = Game(int(result.group(1)))
    for cubes in result.group(2).split("; "):
        draw = Draw()
        for cube in cubes.split(", "):
            n, color = cube.split(" ")
            setattr(draw, color, int(n))
        game.draws.append(draw)
    return game


def main():
    data = read_data("day2.txt", IoOutputType.LINE)
    result = 0
    result2 = 0
    for line in data:
        game = parse_game(line.rstrip())
        if all(
            is_valid(draw, max_blue=14, max_green=13, max_red=12) for draw in game.draws
        ):
            result += game.id
        bag = find_min_possible(game.draws)
        result2 += bag.blue * bag.green * bag.red
    print(result)
    print(result2)


if __name__ == "__main__":
    main()
