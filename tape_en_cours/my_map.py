from typing import Callable, Iterator, TypeVar, List

E = TypeVar("E")
S = TypeVar("S")


def my_map(f: Callable[[E], S], data: Iterator[E]) -> List[S]:
    res = []
    for i in data:
        res.append(f(i))
    return res


def my_lazy_map(
    func: Callable[[T_in], T_out], iterable: Iterable[T_in]
) -> Iterable[T_out]:
    for item in iterable:
        yield func(item)


def my_filter(
    func: Callable[[T_in], bool], iterable: Iterable[T_in]
) -> Iterable[T_out]:
    for item in iterable:
        if func(item):
            yield item
