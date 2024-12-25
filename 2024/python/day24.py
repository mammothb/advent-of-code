import itertools

from helper import read_data


class TreeNode:
    def __init__(self, key: str, val: int | None):
        self.key = key
        self.val = val
        self.l: TreeNode | None = None
        self.r: TreeNode | None = None


def eval_expr(a: int, b: int, expr: str) -> int:
    match expr:
        case "AND":
            return a & b
        case "OR":
            return a | b
        case "XOR":
            return a ^ b
        case _:
            raise ValueError


def get_number(wires: dict[str, int], prefix: str) -> str:
    number = "".join(
        map(
            lambda x: str(x[1]),
            sorted(
                [(k, v) for k, v in wires.items() if k.startswith(prefix)], reverse=True
            ),
        )
    )
    return number


def main():
    data = read_data("day24.txt")
    data = read_data("day24_easy_2.txt")
    parts = data.rstrip().split("\n\n")
    wires: dict[str, int] = {}
    for line in parts[0].split("\n"):
        wire, value = line.split(": ")
        wires[wire] = int(value)
    missing = True
    while missing:
        missing = False
        for line in parts[1].split("\n"):
            expr, output = line.split(" -> ")
            a, gate, b = expr.split(" ")
            if a not in wires or b not in wires:
                missing = True
                continue
            wires[output] = eval_expr(wires[a], wires[b], gate)
    result = get_number(wires, "z")
    print(int(result, base=2))

    wires2: dict[str, int] = {}
    for line in parts[0].split("\n"):
        wire, value = line.split(": ")
        wires2[wire] = int(value)
    x_str = get_number(wires2, "x")
    y_str = get_number(wires2, "y")
    x_val = int(x_str, base=2)
    y_val = int(y_str, base=2)
    expected = f"{x_val + y_val:b}"
    print(expected)
    print(result)

    leaves = {}
    gates = {}
    for line in parts[1].split("\n"):
        expr, output = line.split(" -> ")
        a, gate, b = expr.split(" ")
        gates[(a, gate, b)] = output
        leaves[output] = (a, b)

    roots = []
    for i, val in enumerate(reversed(result)):
        key = f"z{i:02}"
        if key in wires:
            print(key)


if __name__ == "__main__":
    main()
