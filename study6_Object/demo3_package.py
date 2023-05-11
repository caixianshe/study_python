# 目标一：封装 语法 不管是成员方法还是成员变量 定义的时候只要在前面加上__就变成私有的了
# 私有的成员方法 成员变量

# 注意 此时使用__is_5g_enable为布尔类型 所以可以当做if的判断条件
class Phone:
    __is_5g_enable = True
    name="手机"

    def __check_5g(self):
        # if self.__is_5g_enable == "True":
        if self.__is_5g_enable:
            print("5g开启")
        # elif self.__is_5g_enable == "False":
        #     print("5g关闭，使用4g网络")
        else:
            print("5g关闭，使用4g网络")

    def call_by_5g(self):
        self.__check_5g()
        print("正在通话")


# phone = Phone()
# phone.call_by_5g()


# 目标二：继承(单继承)  语法：class 子类(父类)
# 注意1： 在继承的时候 是不能继承私有的东西
# 注意2： 在继承的时候 如果两个函数或者变量同名 我们采取的是左边的优先级最高 不是采取覆盖的形式
class Phone2023:
    name = "苹果"
    IMEI = None

    def call_by_4g(self):
        print("4g手机")


class Phone2024(Phone2023):
    IMEI = "10001"
    name = "2024手机"

    def call_by_5g(self):
        print("5g手机")


phone2024 = Phone2024()
print(phone2024.name)
print(phone2024.IMEI)
phone2024.call_by_5g()


# 目标三：多继承 语法：class(类1,类2,类3)
# pass的作用占位语句 是空的 里面啥也没有 可以保证在语法上面不报错
class happyList(Phone, Phone2024):
    pass


a = happyList()
a.call_by_5g()
name = a.name
print(f"这个name为:{name}")
