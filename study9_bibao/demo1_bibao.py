# 学习目标一：闭包
# 定义双层嵌套函数,内层函数可以访问外层函数的变量
# 将内存函数作为外层函数的返回，此内层函数就是闭包函数

# def outer(logo):
#     def inner(msg):
#         print(f"<{logo}>{msg}<{logo}>")
#
#     return inner
#
#
# # 先调用外面的函数
# f = outer("aaa")
# # f返回值是一个inner函数 然后再次赋值相当于再次调用inner函数
# f("dd")


# 局部变量和全局变量  局部变量的值 不会影响全局变量的值
# 如果想要影响 则要使用global关键字
# global是声明 某个值为全局变量   ---------前面学的 study1->demo7hanshu

# 私有方法 私有函数在study6_Object->demo3_package
# 封装 语法 不管是成员方法还是成员变量 定义的时候只要在前面加上__就变成私有的了  ---------前面学的

# 内部函数要想使用外部变量要使用nonlocal修饰

# 学习目标二：# 内部函数要想使用外部变量要使用nonlocal修饰
# def outer(num1):
#     def inner(num2):
#         # 内部函数要想使用外部变量要使用nonlocal修饰
#         nonlocal num1
#         num1 += num2
#         print(num1)
#
#     return inner
#
#
# f1 = outer(10)
# f1(10)
# f1(10)


# 学习目标三：存钱取钱练习atm
def outer(money1=0):
    def inner(money2, condition):
        nonlocal money1
        if condition:
            money1 += money2
            print(f"存钱+{money2}，余额{money1}")
        else:
            money1 -= money2
            print(f"取钱+{money2}，余额{money1}")

    return inner


f = outer()
f(100, condition=True)
f(200, condition=True)
f(300, condition=True)
f(400, condition=True)
f(500, condition=False)
