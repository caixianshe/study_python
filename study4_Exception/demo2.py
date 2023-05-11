# 异常具有传递性

def fun1():
    print("fun1开始了")
    1 / 0
    print("fun1结束了")


def fun2():
    print("fun2开始了")
    fun1()
    print("fun2结束了")


def main():
    fun2()


main()
