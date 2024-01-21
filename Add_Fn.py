

class AddFn:
    def __init__(self, functions):
        self.functions = functions

    def derivative(self):
        parts = []
        for function in self.functions:
            parts.append(function.derivative())
        return AddFn(parts)

    def __str__(self):
        string = ""
        for function in self.functions:
            string = string + f"{function} + "
        return f"({string[:-3]})"
