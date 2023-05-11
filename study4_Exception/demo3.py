# 导入模块
# 基本语法:
# import 模块名
# import模块名1,模块名2
# 模块名.功能名()

# [from 模块名] import [模块|类|变量|函数|*] [as 别名] 带[]表明可有可无的

# import time
#
# # eg 调用time模块中的sleep函数
# print("你好")
# # 时间单位是秒
# time.sleep(2)
# print("你怎么那么帅")

# 使用from 导入time的sleep功能(函数) time模块中的其他函数都没导入进来 同时不需要点了  直接写函数就可以了
# from time import sleep
# print("你好")
# sleep(3)
# print("你好帅")

# 使用*导入全部功能 和 import 模块名 基本上一样 但是不需要使用.的形式去调用。
from time import *
print("你好")
sleep(3)
print("你好帅")
