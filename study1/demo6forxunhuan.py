# 第六天
# 目标一：for循环  for循环理论上无法构建无限循环（被处理的数据不可能无限大）
# for循环无法定义循环条件，只能被动的取出数据处理
# for x in name:  name称为序列类型 ：其中的内容可以一次次依次取出的内容（字符串，元组，列表等）
name = "caizhengjunccc"
i = 0
for x in name:
    if 'c' == x:
        i += 1
    print(f"{x}\t", end="")
print()
print(f"c出现的次数为{i}")

print("===========================================")
# 目标二：range语句
# 语法一：range(num)
# 获取一个从0开始，到num结束的数字序列(不含num本身)
# 如range(5)取得的数据是: [0,1,2,3,4]
num = 5
for x in range(num):
    print(x)

print("===========================================")
# 语法二：range(num1,num2)
# 获得一个从num1开始，到num2结束的数字序列(不含num2本身)
# 如，range(5,10)取得的数据是: [5,6,7,8,9]
for x in range(2, 6):
    print(x)

print("===========================================")
# 语法三：range(num1,num2,step)
# 获得一个从num1开始，到num2结束的数字序列(不含num2本身 )
# 数字之间的步长，以step为准(step默认为1)
# 如，range(5, 10, 2)取得的数据是: [5, 7, 9]

for x in range(3, 15, 2):
    print(x)

print("===========================================")
# demo
temp = 0

x = 0
for x in range(1, 100):
    if x % 2 == 0:
        temp += 1
print(f"偶数一共有{temp}个")
# 此时出现黄色的警告 x可能没有被定义 解决办法 上方对其定义
print(x)
# 注意 for循环中的临时变量 x 规范上只在for循环里面可以用 但实际上 外面也可以访问的到

print("===========================================")
# 目标二： continue break
for d in range(1, 100):
    if d == 10:
        break
    print(d)
