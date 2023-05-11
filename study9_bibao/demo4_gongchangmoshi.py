# 工厂模式 创建的都不是同一个对象

# 当需要大量创建一个类的实例的时候，可以使用工厂模式.。
# 即，从原生的使用类的构造去创建对象的形式
# 迁移到，基于工厂提供的方法去创建对象的形式.


# 使用工厂类的GET_Person()方法去创建具体的类对象
# 优点:
# 大批量创建对象的时候有统一的入口,易于代码维护
# 当发生修改，仅修改工厂类的创建方法即可
# 符合现实世界的模式,即由工厂来制作产品(对象)

class People:
    pass


class Student(People):
    pass


class Worker(People):
    pass


class Teacher(People):
    pass


class PeopleFactory:
    def get_person(self, p_type):
        if p_type == 'S':
            print("学生")
            return Student()
        elif p_type == 'W':
            print("工作者")
            return Worker()
        else:
            print("老师")
            return Teacher()


# 统一的入口
worker = PeopleFactory().get_person("W")
worker2 = PeopleFactory().get_person("W")
# stu = PeopleFactory().get_person("S")
# teacher = PeopleFactory().get_person("T")
print(worker)
print(worker2)
