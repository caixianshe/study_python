# demo1的练习 使用构造方法 创建10个学生对象并打印学生信息

class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        print(f"学生的信息为：姓名：{name}，年龄：{age}，性别：{gender}")


i = 0
while i < 10:
    print("请输入学生姓名")
    n1 = input()
    print("请输入学生年龄")
    a1 = input()
    print("请输入学生性别")
    g1 = input()
    student = Student(n1, a1, g1)
    i += 1
