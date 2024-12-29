from typing import Protocol, TypeVar

T = TypeVar("T")
Numeric = complex | float | int


class Subtractable(Protocol):
    def __sub__(self, other: T) -> T: ...
