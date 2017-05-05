def identity(x):
    return x


def make_list(x):
    return [x]


def make_dict(k, v):
    return {k: v}


def concat_strings_with_inf(str1, str2):
    result = str1 + str2
    return result, len(result)
