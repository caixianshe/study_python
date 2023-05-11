from demo3_danlimoshi_1 import student

student1 = student
student2 = student

print(id(student1))
print(id(student2))

# 得到的都是同一个对象

# 1.什么是设计模式
# 设计模式就是一种编程套路.
# 使用特定的套路得到特定的效果

# 2.什么是单例设计模式
# 单例模式就是对一个类，只获取其唯一的类实例对象，持续复用它.
# 节省内存
# 节省创建对象的开销
