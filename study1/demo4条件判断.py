# 第四天
# 目标一: 数据输入input 语句
# print("你好！ 你叫什么名字")
# name = input()
# print("哇哦 原来你就是%s" % name)

# 其实这种方式写 感觉有点怪怪的 可以换一种简洁的写法
# name1 = input("你好！ 你的名字叫什么啊")
# print("哦 %s你好啊" % name1)
# 同时input接收的类型都是字符串类型 如果想要接收钱 后面可以采用类型转换
# money = input("你还有多少钱啊")
# money = int(money)
# # print("我现在还有%d元", type(money) % money)  #这里有个错误 因为，把整个语句分开了 所以语法整个都不对了
# print("我现在还有%d元" % money, type(money))

# 比较运算符 == != > < >= <=
# 布尔类型比较  bool 布尔类型
num1 = 10
num2 = 20
num3 = 10 > 20
print(f"num1>num2?{num1 > num2}")
print(f"num1的类型为{type(num3)}")

print("===========================================")

# 目标二 if语句的基本格式  注意：不要省略 同时if后的输出语句前面要注意缩进 没有缩进 记得加四个空格 如果没有缩进表示后面的语句与if平机
age = 10
if age > 18:
    print("你已经成年了")
    print("即将上大学")
print("时间过的好快啊")

# 目标三 if else语句  else代码块中 同样需要四个空格作为缩进
age_1 = 10
if age_1 >= 18:
    print("你已经成年了")
else:
    print("你还没有成年 请转身离开")
print("好烦啊")

print("===========================================")
# 目标四：多条件判断 if elif else  当然 else也可以省略 如果print前面有空格是不做输出的
age_2 = -1
if 0 < age_2 < 18:
    print("你现在是未成年")
elif 18 <= age_2 <= 30:
    print("你现在是青年")
elif 30 < age_2:
    print("你现在已经步入老年")
else:
    print("你输入的年龄有误")
