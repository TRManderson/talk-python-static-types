from typing import TypeVar, Dict, List, Tuple, AnyStr

T = TypeVar('T')
S = TypeVar('S')


def identity(x: T) -> T:
    return x


def make_list(x: T) -> List[T]:
    return [x]


def make_dict(k: T, v: S) -> Dict[T, S]:
    return {k: v}


def concat_strings_with_inf(str1: AnyStr, str2: AnyStr) -> Tuple[AnyStr, int]:
    result = str1 + str2
    return result, len(result)
