# 闭包  就是在不改变原有的函数情况下 对其进行添加或者修改其功能
def sleep():
    import time
    star_time = time.time()
    print("睡眠中.....")
    time.sleep(5)
    end_time = time.time()
    print(f"睡眠了{end_time - star_time}")


# sleep()

# 目标一：装饰器
# def outer(func):
#     def inner():
#         print("我睡觉了")
#         func()
#         print("我起来了")
#
#     return inner
#
#
# f1 = outer(sleep)
# f1()

# 目标二：装饰器的语法糖
def outer(func):
    def inner():
        print("我睡觉了")
        func()
        print("我起来了")

    return inner


# @outer和上面的函数名一样就可以了
@outer
def sleep():
    import time
    print("睡眠中.....")
    time.sleep(5)


sleep()  # 采用语法糖 调用sleep函数 但是现在使用的是outer函数 给人的感觉就是还是调用的是sleep函数没有变
