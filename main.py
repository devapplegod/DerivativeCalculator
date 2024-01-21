from Add_Fn import AddFn
from Const_Fn import ConstFn
from Multiple_Fn import MultipleFn
from Power_Fn import PowerFn
from X_Fn import XFn


func = ConstFn(123, XFn())  # f(x) = 123x
func2 = PowerFn(100, XFn())  # f(x) = x^100
func3 = ConstFn(9, PowerFn(4, ConstFn(2, XFn())))  # f(x) = 9*(2x)^4
func4 = MultipleFn([ConstFn(4, XFn()), PowerFn(3, XFn()), ConstFn(4, XFn())])
func5 = AddFn([ConstFn(69, XFn()), PowerFn(4, AddFn([XFn(), PowerFn(2, XFn())]))])
print(func5)
print(func5.derivative())
#for fn in func4.derivative().functions:
    #for f in fn.functions:
        #print(f)
    #print()
