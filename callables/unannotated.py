from functools import partial


def double(x):
    return x + x


def compose(f, g):
    return lambda x: f(g(x))


def map_and_double(fn, iterable):
    return compose(partial(map, double), partial(map, fn))(iterable)
