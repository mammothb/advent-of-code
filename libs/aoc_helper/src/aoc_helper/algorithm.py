import itertools
from collections.abc import Iterable
from typing import TypeVar

from aoc_helper.types import Numeric, Subtractable

T = TypeVar("T", bound=Numeric | Subtractable)


def pairwise_differences(nums: Iterable[T], reverse: bool = False) -> list[T]:
    return [b - a if reverse else a - b for a, b in itertools.pairwise(nums)]
