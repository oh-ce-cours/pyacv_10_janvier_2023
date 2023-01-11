from typing import Callable, Iterator, TypeVar, List

E = TypeVar("E")
S = TypeVar("S")


def my_map(f: Callable[[E], S], data: Iterator[E]) -> List[S]:
    res = []
    for i in data:
        res.append(f(i))
    return res


def my_lazy_map(func: Callable[[E], S], iterable: Iterator[E]) -> Iterator[S]:
    for item in iterable:
        yield func(item)


def my_filter(func: Callable[[E], bool], iterable: Iterator[E]) -> Iterator[E]:
    for item in iterable:
        if func(item):
            yield item


a = 1_000_000
b = 0.000_000_3

print(locals())
