import math
import re
from enum import Enum, auto
from typing import NotRequired, TypedDict

from helper import read_data


class ResponseType(Enum):
    NOOP = auto()
    JUMP = auto()
    OUTPUT = auto()


class Register(TypedDict):
    A: int
    B: int
    C: int


class Response(TypedDict):
    type: ResponseType
    value: NotRequired[int]


def combo_operand(register: Register, operand: int) -> int:
    match operand:
        case 0 | 1 | 2 | 3:
            return operand
        case 4:
            return register["A"]
        case 5:
            return register["B"]
        case 6:
            return register["C"]
        case _:
            raise ValueError("Bad operand")


def do_operation(register: Register, opcode: int, operand: int) -> Response:
    match opcode:
        case 0:
            numerator = register["A"]
            denominator = math.pow(2, combo_operand(register, operand))
            register["A"] = int(numerator / denominator)
        case 1:
            left = register["B"]
            right = operand
            register["B"] = left ^ right
        case 2:
            register["B"] = combo_operand(register, operand) % 8
        case 3:
            if register["A"] == 0:
                return Response(type=ResponseType.NOOP)
            return Response(type=ResponseType.JUMP, value=operand)
        case 4:
            left = register["B"]
            right = register["C"]
            register["B"] = left ^ right
        case 5:
            return Response(
                type=ResponseType.OUTPUT, value=combo_operand(register, operand) % 8
            )
        case 6:
            numerator = register["A"]
            denominator = math.pow(2, combo_operand(register, operand))
            register["B"] = int(numerator / denominator)
        case 7:
            numerator = register["A"]
            denominator = math.pow(2, combo_operand(register, operand))
            register["C"] = int(numerator / denominator)
        case _:
            raise ValueError("Bad opcode")
    return Response(type=ResponseType.NOOP)


def solve_part1(register: Register, program: list[int]) -> str:
    result: list[int] = []
    n = len(program)
    i = 0
    while i < n - 1:
        response = do_operation(register, program[i], program[i + 1])
        match response["type"]:
            case ResponseType.OUTPUT:
                assert "value" in response
                result.append(response["value"])
            case ResponseType.JUMP:
                assert "value" in response
                i = response["value"]
                continue
            case _:
                pass
        i += 2
    return ",".join(map(str, result))


def solve_part2(
    register: Register, program: list[int], offset: int, curr: int
) -> int | None:
    for i in range(8):
        candidate = curr * 8 + i
        register_copy = register.copy()
        register_copy["A"] = candidate

        if solve_part1(register_copy, program.copy()) == ",".join(
            map(str, program[offset:])
        ):
            if offset == 0:
                return candidate
            result = solve_part2(register, program, offset - 1, candidate)
            if result is not None:
                return result


def main():
    data = read_data("day17.txt")

    res_a = re.search(r"Register A: (.*)\n", data)
    res_b = re.search(r"Register B: (.*)\n", data)
    res_c = re.search(r"Register C: (.*)\n", data)
    res_p = re.search(r"Program: (.*)\n", data)
    assert res_a is not None
    assert res_b is not None
    assert res_c is not None
    assert res_p is not None

    register = Register(
        A=int(res_a.group(1)),
        B=int(res_b.group(1)),
        C=int(res_c.group(1)),
    )
    program = list(map(int, res_p.group(1).split(",")))

    print(solve_part1(register.copy(), program.copy()))
    print(solve_part2(register.copy(), program.copy(), len(program) - 1, 0))


if __name__ == "__main__":
    main()
