class HelloStream:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Hello, {}!".format(self.name)

    def __repr__(self):
        return self.__str__()
