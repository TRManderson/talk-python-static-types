def fib_seq(first, second):
    yield first
    yield second
    while True:
        first, second = second, (first + second)
        yield second

async def promise_dot_all(*args):
    result = []
    for arg in args:
        result.append(await arg)
    return result