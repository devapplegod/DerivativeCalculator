class ConstFn:
    def __init__(self, constant, function):
        self.constant = constant
        self.function = function

    def derivative(self):
        return ConstFn(self.constant, self.function.derivative())

    def __str__(self):
        return f"{self.constant} * {self.function}"
