# 目标一：初识对象
# 设计一个类 对比生活中的登记表
# 第一步 创建一个对象
# class Student:
#     name: None
#     age: None
#     gender: None
#
#     # 如果要想访问类中的其他成员变量 必须要使用self
#     def si_Hi(self):
#         print(f"hi 大家好 我是{self.name}")
#
#     def study_test(self, t1, t2, t3):
#         print(f"hi 大家好 我是{self.name}，一般我学习{t1}，{t2}，{t3}")


# 第二步 给对象赋值
# s1 = Student()
# s1.name = "张三"
# s1.age = 18
# s1.gender = "男"

# 第三步 打印
# # print(s1)  <__main__.Student object at 0x007E1350>
# s1.si_Hi()
# s1.study_test("语文", "数学", "英语")
#
# print(s1.name)
# print(s1.age)
# print(s1.gender)


# 可以看到，在方法定义的参数列表中，有一个: self关键字
# self关键字是成员方法定义的时候，必须填写的。
# 它用来表示类对象自身的意思
# 当我们使用类对象调用方法的是，self会自动被python传入
# 在方法内部，想要访问类的成员变量,必须使用self

# 目标二：类和对象
# 此时设计一个闹钟类
# class Clock:
#     id = None
#     price = None
#
#     # 此时让它响铃
#     def ring(self):
#         import winsound
#         winsound.Beep(2000, 3000)
#
#
# clock = Clock()
# clock.ring()
# clock.id = "10001"
# clock.price = "2399"
# print(clock.id)
# print(clock.price)


# 目标三：构造方法的名称 __init__
class Student1:
    # name = None
    # age = None
    # gender = None

    def __init__(self, name, age, gender):
        # 写反了
        # name = self.name
        # age = self.age
        # gender = self.gender

        # 如果上面没写 name = None这种 此时这里就是初始化 写了的话就是赋值
        self.name = name
        self.age = age
        self.gender = gender
        print("此时我执行了")


student_1 = Student1("小可爱", 18, "男")
# print(student_1.name)
# print(student_1.age)
# print(student_1.gender)
