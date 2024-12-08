from pathlib import Path


def read_data(file_name: str) -> str:
    with open(Path(__file__).resolve().parents[1] / "data" / file_name) as infile:
        return infile.read()
