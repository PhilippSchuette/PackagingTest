# This is a stub file for MyPy static type checking of the module `module1`

from typing import List


class Employee:
    def __init__(self, id: int, first: str, last: str) -> None: ...


def func1() -> str: ...


def func2() -> List[float]: ...


def func3() -> str: ...


def add(x: float, y: float) -> float: ...


def subtract(x: float, y: float) -> float: ...


def divide(x: float, y: float) -> float: ...


def multiply(x: float, y: float) -> float: ...
