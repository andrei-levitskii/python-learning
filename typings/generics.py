# this is <python3.12 syntax
from __future__ import annotations

from typing import Callable, Generic, Protocol, TypeVar


class MultInt(Protocol):
    def __mul__(self: T, x: int) -> T: ...


T = TypeVar("T", bound=MultInt)


def double(x: T) -> T:
    return x * 2


In = TypeVar("In")
Out = TypeVar("Out")


def my_map(fn: Callable[[In], Out], lst: list[In]) -> list[Out]:
    ret = []
    for thing in lst:
        ret.append(fn(thing))
    return ret


class FDict(Generic[In, Out]):
    def __init__(self, dct: dict[In, Out]) -> None:
        self._dct = dct

    def __getitem__(self, k: In) -> Out:
        return self._dct[k]


def main() -> None:
    print(my_map(lambda x: str(x), [1, 2, 3]))
    # reveal_type(my_map(lambda x: str(x), [1, 2, 3]))
    d = FDict({"1": 2})
    # reveal_type(d["1"])


if __name__ == "__main__":
    main()
