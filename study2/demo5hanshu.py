# 函数进阶
# 目标一：函数如何返回多个返回值  返回值不受限制

def test_demo():
    return 1, "hello", True


x, y, z = test_demo()
print(x)
print(y)
print(z)


# 目标二：函数的多种传参方式 位置参数、关键字参数、缺省参数、不定长参数（有两种）
# 位置参数 以前学习的函数就是位置参数
def study_def(name, age, like):
    print(f"姓名是{name}，年龄是{age}，爱好为:{like}")


print("====位置参数====")
study_def("张三", 18, "学习")


# 关键字参数 可以与位置参数混用 位置参数在前 关键字参数在后
def study_def_two(name, age, like):
    print(f"姓名是{name}，年龄是{age}，爱好为:{like}")


print("====关键字参数====")
study_def_two("李四", like="玩游戏", age=20)


# 缺省参数 如果你没有传默认为 你写的参数 如果你传参了 按照传参的为准
def study_def_three(name, age, like="爱学习"):
    print(f"姓名是{name}，年龄是{age}，爱好为:{like}")


print("====缺省参数====")
study_def_three("李四", age=20)
study_def_three("王五", 18, "打游戏")


# 不定长参数
# 第一种情况：位置不定长，*号
# 不定长-----位置不定长，*号
# 不定长定义的形式参数会作为元组存在，接收不定长数量的参数传入 *args 规范上那么写
def study_def_four(*args):
    print(f"args参数的类型是: {type(args)}， 内容是:{args}")


study_def_four(1, 2, 3, 4, 5, "张三", True)  # 传入的参数个数不受限制


# 第二种情况：关键字不定长，**号  这种是k-value的形式 结果为字典形式  **kwargs 规范上那么写
def study_def_five(**kwargs):
    print(f"args参数的类型是: {type(kwargs)}，内容是:{kwargs}")


study_def_five(name="张三", age=22, dream="考上哈佛")


# 目标三：函数作为参数传递
# 传递的是数据 ===数据不确定的 但是逻辑是确定的
def add1(a1, a2):
    result_add = a1 + a2
    print(f"结果是{result_add}")


# 传递的是代码执行的逻辑  ===数据是固定的 但是不清楚逻辑
def add_test(add1):
    return add1(2, 3)


add_test(add1)

# 目标四 lambda匿名函数  #这里匿名函数针对的是代码的执行逻辑 而不是传递的数据
# 也是采用上面的传递参数方式 不过在调用的时候 我们采用匿名函数的方式
test = add_test(lambda a1, a2: a1 + a2)
print(test)

# add1(1, 2)
