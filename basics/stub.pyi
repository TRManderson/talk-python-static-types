def greeting(name: str) -> str: ...


class Greeter(object):
    name: str
    def __init__(self, name: str) -> None: ...
    def greet(self) -> str: ...
