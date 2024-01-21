from Add_Fn import AddFn


class MultipleFn:
    def __init__(self, functions):
        self.functions = functions

    def derivative(self):
        n = len(self.functions)
        parts = []
        for i in range(n):
            part = []
            for j in range(n):
                if i == j:
                    part.append(self.functions[j].derivative())
                else:
                    part.append(self.functions[j])
            parts.append(MultipleFn(part))
        return AddFn(parts)

    def __str__(self):
        string = ""
        for function in self.functions:
            string = string + f"{function} * "
        return f"{string[:-3]}"
