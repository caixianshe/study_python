# 复写父类成员和调用父类成员（相当于java中的重写）
# 如果不想使用python中的父类成员或者方法 可以重新在子类中重写
class Student:
    name = "小男孩"
    age = 20

    def study(self):
        print("学习")


class Boy(Student):
    name = "小小"

    def study(self):
        print("学习唱跳rap")

        # # 此时我还是想调用父类的这个名字
        # print(Student.name)
        # # 此时我还是线稿调用父类的方法 注意 self也是要带的
        # Student.study(self)

        # 方式二：可以使用super去调用父类的东西 这里不需要传self
        super().study()
        print(super().name)


boy = Boy()
# print(boy.name)
# print(boy.age)
boy.study()

