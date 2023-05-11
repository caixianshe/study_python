# 导入自定义的模块

# 导入方式一：
# import sum_add
# 导入方式二：
# from sum_add import number_add

# sum_add.number_add(1, 3)


# 导入两个自定义的模块 出现两个相同的函数时 后者会把前者给覆盖掉
# sum_add和sum_add2都有number_add函数 但是使用的却是后者

# from sum_add2 import number_add
#
# number_add(1, 2)


# 学习目标2 ： __main__ 变量  现在在 sum_add 中想要测试 添加 number_add(1,3) 再导入sum_add包之后就会出现结果
#
# import sum_add


# 学习目标3 ：__all__ 变量  它的值是一个列表[]
# 当我们使用from 模块 import*的时候 * 就是模块中的__all__  如果模块中没有定义它 默认都可以使用 如果定义了 那么就只能使用对应的__all__
from sum_add3 import *

testA(2, 2)
# testB(3, 2)
