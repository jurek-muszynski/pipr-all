from dataclasses import dataclass


@dataclass
class File:
    path: str
    fieldnames: list[str]
    rows: int
    unique_values: dict[str, int]
    count_values: dict[str, dict[str, int]]
