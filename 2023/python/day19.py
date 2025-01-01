import functools
import operator
import re
from collections.abc import Iterable
from dataclasses import dataclass
from typing import Callable

from aoc_helper.io import IoOutputType, read_data

PART_PAT = re.compile(r"(\w)=(\d+),(\w)=(\d+),(\w)=(\d+),(\w)=(\d+)")
RULE_PAT = re.compile(r"([xmas])(<|>)(\d+):(\w+)")
WORKFLOW_PAT = re.compile(r"(\w+)\{(.+)\}")


@dataclass
class Rule:
    dest: str
    category: str | None = None
    compare: Callable[[int, int], bool] | None = None
    target: int | None = None

    @property
    def condition(self) -> tuple[str, str, int]:
        assert (
            self.category is not None
            and self.compare is not None
            and self.target is not None
        )
        return self.category, "<" if self.compare == operator.lt else ">", self.target

    @property
    def inverse_condition(self) -> tuple[str, str, int]:
        assert (
            self.category is not None
            and self.compare is not None
            and self.target is not None
        )
        if self.compare == operator.gt:
            return self.category, "<", self.target + 1
        return self.category, ">", self.target - 1

    def evaluate(self, part: dict[str, int]) -> str | None:
        if self.category is None or self.compare is None or self.target is None:
            return self.dest
        if self.compare(part[self.category], self.target):
            return self.dest

    @classmethod
    def create(cls, expr: str) -> "Rule":
        res = RULE_PAT.search(expr)
        if res is None:
            return cls(expr)
        return cls(
            dest=res.group(4),
            category=res.group(1),
            compare=operator.lt if res.group(2) == "<" else operator.gt,
            target=int(res.group(3)),
        )


def parse_part(s: str) -> dict[str, int]:
    res = PART_PAT.search(s)
    assert res is not None
    return {
        res.group(1): int(res.group(2)),
        res.group(3): int(res.group(4)),
        res.group(5): int(res.group(6)),
        res.group(7): int(res.group(8)),
    }


def sort_part(workflow: dict[str, list[Rule]], part: dict[str, int]) -> str:
    node = "in"
    while node not in "AR":
        for rule in workflow[node]:
            if (next_node := rule.evaluate(part)) is not None:
                node = next_node
                break
    return node


def add_constraint(
    constraint: dict[str, tuple[int, int]], category: str, op: str, target: int
) -> dict[str, tuple[int, int]] | None:
    low, high = constraint[category]
    if op == ">":
        if target >= high:
            return
        low = target + 1
    else:
        if target <= low:
            return
        high = target - 1
    result = constraint.copy()
    result[category] = (low, high)
    return result


def trace_paths(
    workflow: dict[str, list[Rule]],
    workflow_name: str,
    constraint: dict[str, tuple[int, int]],
) -> Iterable[dict[str, tuple[int, int]]]:
    for rule in workflow[workflow_name]:
        if rule.category is None or rule.compare is None or rule.target is None:
            cons_true = constraint
        else:
            cons_true = add_constraint(constraint, *rule.condition)
            cons_false = add_constraint(constraint, *rule.inverse_condition)
            assert cons_false is not None
            constraint = cons_false
        if cons_true is not None:
            if rule.dest == "A":
                yield cons_true
            elif rule.dest != "R":
                yield from trace_paths(workflow, rule.dest, cons_true)


def main():
    data = read_data("day19.txt", IoOutputType.BLOCK)
    workflow: dict[str, list[Rule]] = {}
    for line in data[0].split("\n"):
        res = WORKFLOW_PAT.search(line)
        assert res is not None
        workflow_name = res.group(1)
        workflow_rules = [Rule.create(part) for part in res.group(2).split(",")]
        workflow[workflow_name] = workflow_rules
    result = 0
    for line in data[1].split("\n"):
        part = parse_part(line.rstrip())
        if sort_part(workflow, part) == "A":
            result += sum(part.values())
    print(result)
    result2: int = 0
    for path in trace_paths(workflow, "in", {c: (1, 4000) for c in "xmas"}):
        result2 += functools.reduce(
            operator.mul, (high - low + 1 for low, high in path.values())
        )
    print(result2)


if __name__ == "__main__":
    main()
