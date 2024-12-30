from typing import Protocol, TypeVar

Coord = tuple[int, int]
Numeric = complex | float | int

T = TypeVar("T")


class Subtractable(Protocol):
    def __sub__(self, other: T) -> T: ...
