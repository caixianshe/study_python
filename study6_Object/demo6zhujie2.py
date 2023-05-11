# 函数形参的注解 以及 函数返回值的注解
from typing import Union, List

# 目标一： 函数形参的注解  语法   : 类型    ctrl +p 会有提示 不写注解是没有提示的
# def sumadd(x: int, y: int):
#     return x + y
#
#
# # def sumadd(x, y):
# #     return x + y
#
# i = sumadd(1, 2)
# print(i)


# 目标二：函数返回值的注解  ->  注意这些都是规范上的  不那么写 不影响什么
# def func(date) -> list:
#     return date
#
#
# func()

# 目标三：Union 可以定义联合类型注解
my_list: List[Union[int, str]] = [1, 2, "我爱学习", "是真的"]
print(my_list)
