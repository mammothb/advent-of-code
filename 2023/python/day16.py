import collections
from dataclasses import dataclass

from aoc_helper.constants import Dirs4
from aoc_helper.io import IoOutputType, read_data
from aoc_helper.types import Coord

DIDJ_TO_DIR = {
    (0, 1): Dirs4.E,
    (-1, 0): Dirs4.N,
    (0, -1): Dirs4.W,
    (1, 0): Dirs4.S,
}


@dataclass
class Beam:
    coord: Coord
    direction: Dirs4

    @property
    def next_position(self) -> Coord:
        di, dj = self.direction.value
        return self.coord[0] + di, self.coord[1] + dj

    @property
    def orientation(self) -> tuple[Coord, Dirs4]:
        return self.coord, self.direction

    def is_in_bounds(self, nr: int, nc: int) -> bool:
        return 0 <= self.coord[0] < nr and 0 <= self.coord[1] < nc

    @classmethod
    def bend(cls, i: int, j: int, direction: Dirs4) -> "Beam":
        di, dj = direction.value
        return cls((i + di, j + dj), direction)

    @classmethod
    def turn_trbl(cls, i: int, j: int, direction: Dirs4) -> "Beam":
        di, dj = direction.value
        di, dj = -dj, -di
        return cls((i + di, j + dj), DIDJ_TO_DIR[(di, dj)])

    @classmethod
    def turn_tlbr(cls, i: int, j: int, direction: Dirs4) -> "Beam":
        di, dj = direction.value
        di, dj = dj, di
        return cls((i + di, j + dj), DIDJ_TO_DIR[(di, dj)])


def solve(grid: list[list[str]], initial_beams: list[Beam]) -> int:
    nr = len(grid)
    nc = len(grid[0])
    result = 0
    for beam in initial_beams:
        queue = collections.deque([beam])
        energized: set[Coord] = set()
        seen: set[tuple[Coord, Dirs4]] = set()
        while queue:
            n_queue = len(queue)
            for _ in range(n_queue):
                beam = queue.popleft()
                i, j = beam.coord
                if not (0 <= i < nr and 0 <= j < nc):
                    continue
                if beam.orientation in seen:
                    continue
                seen.add(beam.orientation)
                energized.add(beam.coord)

                match grid[i][j]:
                    case ".":
                        queue.append(Beam(beam.next_position, beam.direction))
                    case "|":
                        if beam.direction in (Dirs4.N, Dirs4.S):
                            queue.append(Beam(beam.next_position, beam.direction))
                        if (b := Beam.bend(i, j, Dirs4.N)).is_in_bounds(nr, nc):
                            queue.append(b)
                        if (b := Beam.bend(i, j, Dirs4.S)).is_in_bounds(nr, nc):
                            queue.append(b)
                    case "-":
                        if beam.direction in (Dirs4.E, Dirs4.W):
                            queue.append(Beam(beam.next_position, beam.direction))
                        if (b := Beam.bend(i, j, Dirs4.W)).is_in_bounds(nr, nc):
                            queue.append(b)
                        if (b := Beam.bend(i, j, Dirs4.E)).is_in_bounds(nr, nc):
                            queue.append(b)
                    case "/":
                        if (b := Beam.turn_trbl(i, j, beam.direction)).is_in_bounds(
                            nr, nc
                        ):
                            queue.append(b)
                    case "\\":
                        if (b := Beam.turn_tlbr(i, j, beam.direction)).is_in_bounds(
                            nr, nc
                        ):
                            queue.append(b)
                    case _:
                        raise ValueError
        result = max(result, len(energized))
    return result


def main():
    data = read_data("day16.txt", IoOutputType.GRID)
    # data = read_data("day16_easy.txt", IoOutputType.GRID)
    print(solve(data, [Beam((0, 0), Dirs4.E)]))
    nr = len(data)
    nc = len(data[0])
    initial_beams: list[Beam] = []
    for i in range(nr):
        initial_beams.append(Beam((i, 0), Dirs4.E))
        initial_beams.append(Beam((i, nc - 1), Dirs4.W))
    for j in range(nc):
        initial_beams.append(Beam((0, j), Dirs4.S))
        initial_beams.append(Beam((nr - 1, j), Dirs4.N))

    print(solve(data, initial_beams))


if __name__ == "__main__":
    main()
