def greeting(name):
    return "Hello, {}!".format(name)


class Greeter(object):
    def __init__(self, name):
        self.name = name

    def greet(self):
        return "Hello, {}!".format(self.name)
