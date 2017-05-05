def parse_int(string):
    try:
        return int(string)
    except ValueError: # parse error
        return None


def bytes_to_char_values(data):
    return [chr(val) for val in data]


trm_data = {
    'name': 'Tom Manderson',
    'website': 'https://trm.io',
    'email': 'me@trm.io',
}


def add_one(x):
    if isinstance(x, str):
        return x + '1'
    elif isinstance(x, int):
        return x + 1


def ignore_x(x):
    return x