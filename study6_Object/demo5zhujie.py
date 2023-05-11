# 注解  这种注解一般都不写一般都是在一眼看不出类型的情况下写出来
# 注意： 类型注解只是提醒作用 不会影响程序的执行结果 同时如果你数据类型和匹配类型不一样 程序启动也不会报错
# 语法1 变量:类型
# 语法2 在注释中 #type:类型


import json
import random
from typing import List, Tuple, Dict

var_1: int = 10
var_2: str = "shauige"
var_3: bool = True


# 类对象类型注解
class Student:
    pass


stu: Student = Student()

# 基础容器类型注解  这种注解一般都不写一般都是在一眼看不出类型的情况下写出来
# my_list: list = [1, 2, 3]
# my_tuple: tuple = (1, 2, 3)
# my_dict: dict = {"itheimo": 666}
# 容器类型详细注解
my_list: List[int] = [1, 2, 3]
my_tuple: Tuple[int, str, bool] = (1, "itheima", True)
my_dict: Dict[str, int] = {"itheima": 666}

# 在注释中进行类型注解
var_1 = random.randint(1, 10)  # type: int
var_2 = json.loads('{"name": "zhangsan"}')  # type: dict[str, str]


def deuc():
    return 10


var_3 = deuc()  # type: int
