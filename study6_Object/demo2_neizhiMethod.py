# 类里面的内置方法（也叫魔术方法）
# __init__  构造方法
# __str__   字符串方法
# __lt__    小于大于符号比较
# __le__    小于等于、大于等于符号比较
# __eq__    等于符号比较

class Student:
    # __init__  构造方法
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # __str__   字符串方法
    def __str__(self):
        return f"Student类对象,名字:{self.name}，年龄：{self.age}，性别：{self.gender}"

    # __lt__    小于大于符号比较
    def __lt__(self, other):
        return self.age > other

    # __le__    小于等于、大于等于符号比较
    def __le__(self, other):
        return self.age >= other

    # __eq__    等于符号比较
    def __eq__(self, other):
        return self.name == other


student1 = Student("小可爱", 18, "男")
print(student1)  # <__main__.Student object at 0x027513D0>
print(str(student1))  # <__main__.Student object at 0x01EC0870>
# 如果想输出对象 此时可以采用__str__内置方法(加上这个之后)  输出的结果为：Student类对象,名字:小可爱，年龄：18，性别：男

student2 = Student("小可爱", 11, "男")

print(student1 > student2)  # True

print(student1 >= student2)  # True

print(student1 == student2)  # True
