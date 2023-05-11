# 第一天
# 目标一：学习注释
# 一个整数
35
# 一个浮点数
36.6
# 一个字符串
'HelloWorld'

"""多行注释  英文模式下 shift+引号 """
print("HelloWorld")

# 目标二：变量
# 定义一个钱包 里面有50元
money = 50
print("钱包里有：", money)
# 此时花费10元买冰淇淋
money = money - 10
print("钱包里有：", money, "元")

# 目标三：数据类型转换
# 查看数据是什么类型用 type()
print(type("HelloWorld"))  # 结果为<class 'str'>  str代表字符串类型
# 还可以用变量储存结果
string_temp = type("HelloWorld")
print(string_temp)
# 还可以
print(type(money))


