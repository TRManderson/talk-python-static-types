from functools import partial
from typing import Callable, Iterable, TypeVar

T = TypeVar('T')
S = TypeVar('S')
R = TypeVar('R')


def double(x: T) -> T:
    return x + x


def compose(f: Callable[[S], R], g: Callable[[T], S]) -> Callable[[T], R]:
    return lambda x: f(g(x))


def map_and_double(fn: Callable[[T], R], iterable: Iterable[T]) -> Iterable[R]:
    return compose(partial(map, double), partial(map, fn))(iterable)
