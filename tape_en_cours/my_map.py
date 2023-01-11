from typing import Callable, Iterator, TypeVar, List

E = TypeVar("E")
S = TypeVar("S")


def my_map(f: Callable[[E], S], data: Iterator[E]) -> List[S]:
    d0 = next(data)
    d1 = next(data)
    return [f(data[0]), f(data[1])]
