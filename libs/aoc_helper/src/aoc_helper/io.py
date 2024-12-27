import inspect
from enum import Enum, auto
from pathlib import Path
from typing import Literal as L
from typing import overload


class IoOutputType(Enum):
    STRING = auto()
    LINE = auto()
    BLOCK = auto()


@overload
def read_data(file_name: str) -> str: ...
@overload
def read_data(file_name: str, output_type: L[IoOutputType.STRING]) -> str: ...
@overload
def read_data(
    file_name: str, output_type: L[IoOutputType.LINE] | L[IoOutputType.BLOCK]
) -> list[str]: ...
def read_data(
    file_name: str, output_type: IoOutputType = IoOutputType.STRING
) -> str | list[str]:
    caller_file = inspect.stack()[1].filename
    with open(Path(caller_file).resolve().parents[1] / "data" / file_name) as infile:
        match output_type:
            case IoOutputType.STRING:
                return infile.read()
            case IoOutputType.LINE:
                return infile.readlines()
            case IoOutputType.BLOCK:
                return infile.read().rstrip().split("\n\n")
