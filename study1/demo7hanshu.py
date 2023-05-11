# 第七天 函数：函数必须先写 如果放在调用方法的后面 会报错/return后面的代码 不在执行
# =========== 目标一：函数， 已经组织好的 具有特定功能的代码块 可重复使用的
# 定义函数：
def see_hi():
    print("你好啊")


# 调用函数
print("# ===定义函数===")
see_hi()


# 函数的使用步骤 ：先定义函数 后调用
# 注意事项：参数和返回值不需要可以省略不写

# =========== 目标二：函数的参数
def add_sum(x, y):
    print(f"{x}+{y}={x + y}")
    # return


print("# ===函数的参数===")
add_sum(5, 2)


# =========== 目标三：函数的返回值定义语法
def add_sum_two(x, y):
    temp = x + y
    return temp
    print("目标三 看看我能不能输出")


result = add_sum_two(5, 8)
print("# ===函数的返回值定义语法===")
print(f"最终的结果是：{result}")


# =========== 目标四：补充函数返回值之None类型
# 如果函数没有使用return语句返回数据 函数有返回值嘛 答案是有的
# Python中有一个特殊的字面量: None,其类型是: <class 'NoneType'>
# 无返回值的函数，实际上就是返回了: None这个字面量
# None表示:空的、无实际意义的意思
# 函数返回的None,就表示，这个函数没有返回什么有意义的内容。
# 也就是返回了空的意思
def see_bye():
    print("下次见")


# 这个波浪线代表可能返回值是个空值
print("# ===返回值之None===")
end = see_bye()
print(f"返回结果是{end}")
print(f"返回结果类型是{type(end)}")


# 应用场景 用在函数无返回值上/用在if中 None等同False


# 目标五：函数的说明文档  打三个引号之后换行就可以了“”“
def add_sum_end(x, y):
    """
    add_sum_end函数可以接收两个参数，对其进行累加求和
    :param x: 参数一 表示其中的一个参数
    :param y: 参数二 表示另一个参数
    :return: 返回两个数之和
    """
    a1 = x + y
    print(f"两个数的和为{a1}")
    return a1


# 把鼠标放到下面的函数上 会显示此函数的说明文档  一般我们写函数的时候 都会把说明文档补齐
add_sum_end(5, 6)


# 目标六：函数的嵌套调用
def a1():
    print("2")


def a2():
    print("# ===函数的嵌套调用===")
    print("1")
    a1()
    print("3")


a2()

# 目标七：局部变量和全局变量  局部变量的值 不会影响全局变量的值
# 如果想要影响 则要使用global关键字
# global是声明 某个值为全局变量
# 内部函数要想使用外部变量要使用nonlocal修饰
name = "张三"


def test1():
    global name         # 设置内部的局部变量为全局变量
    name = "小可爱"
    age = 10
    print(f"年龄是：{age}，姓名为：{name}")


print("# ===函数的局部变量和全局变量===")
test1()
print(f"姓名为：{name}")
# print(f"年龄是{age}，姓名是{name}")
