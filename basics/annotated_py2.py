def greeting(name):
    # type: (str) -> str
    return "Hello, {}!".format(name)


class Greeter(object):
    name = None  # type: str

    def __init__(self, name):
        # type: (str) -> None
        self.name = name

    def greet(self) -> str:
        # type: () -> str
        return "Hello, {}!".format(self.name)
