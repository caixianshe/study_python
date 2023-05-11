# 第五天 随机数
import random

# 包括1 10
number = random.randint(1, 10)
if number > 8:
    print("非常不错")
elif number > 6:
    print("刚好及格")
else:
    print("你还需要努力啊")
print(number)

print("===========================================")
# 目标二 循环语句 while
i = 0
sum_number = 0
while i < 100:
    i += 1
    sum_number += i
    # print("我喜欢你", i)
print(sum_number)

# 目标三：补充两个知识点 输出不换行 以及\t制表符
print("Hello", end="")
print("World")

print("Hello\tWorld")
print("hioo\tnihao")

