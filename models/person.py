from dataclasses import dataclass


@dataclass(init=False)
class Person:
    name: str
    age: int
