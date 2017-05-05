def greeting(name: str) -> str:
    return "Hello, {}!".format(name)


class Greeter(object):
    name: str

    def __init__(self, name: str) -> None:
        self.name = name

    def greet(self) -> str:
        return "Hello, {}!".format(self.name)
