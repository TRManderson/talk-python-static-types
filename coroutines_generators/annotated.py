from typing import Generator, Awaitable, TypeVar, Sequence, List


def fib_seq(first: int, second: int) -> Generator[int, None, None]:
    yield first
    yield second
    while True:
        first, second = second, (first + second)
        yield second


T = TypeVar('T')
async def promise_dot_all(awaitables: Sequence[Awaitable[T]]) -> List[T]:
    result = []
    for item in awaitables:
        result.append(await item)
    return result


# reveal_type(fib_seq)
# reveal_type(promise_dot_all)
