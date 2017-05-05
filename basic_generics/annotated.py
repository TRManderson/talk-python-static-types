from typing import List, Union, Optional, Any


def parse_int(string: str) -> Optional[int]:
    try:
        return int(string)
    except ValueError: # parse error
        return None


def bytes_to_char_values(data: bytes) -> List[int]:
    return [val for val in data]


trm_data = {
    'name': 'Tom Manderson',
    'website': 'https://trm.io',
    'email': 'me@trm.io',
}
# reveal_type(trm_data)


def add_one(x: Union[int, str]) -> None:
    if isinstance(x, str):
        print(x + '1')
    elif isinstance(x, int):
        print(x + 1)


def ignore_x(x: Any) -> None:
    return x