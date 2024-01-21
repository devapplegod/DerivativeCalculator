from Const_Fn import ConstFn
from Multiple_Fn import MultipleFn


class PowerFn:
    def __init__(self, constant, function):
        self.constant = constant
        self.function = function

    def derivative(self):
        # print(PowerFn(self.constant-1, self.function))
        return MultipleFn([ConstFn(self.constant, PowerFn(self.constant-1, self.function)), self.function.derivative()])

    def __str__(self):
        return f"({self.function})^{self.constant}"
