# 第二天
# 数据类型有：
# 不可变数据类型 Number数字类型 Boolean布尔类型 String字符串类型 Tuple元组类型  四种
# 可变数据类型  list列表 Set集合 Dictionary字典类型

# 目标一：数据类型转换
#  int(temp) float(temp) str(temp)

# 把数字类型转换为字符串  同时把值显示出来
temp = str(5.6)
print(type(temp), temp)

# 把字符串类型转换为数字  同时把值显示出来
result = int("11")
print(type(result), result)

a = float("5.4")
print(type(a), a)

# a2 = int("黑马程序员")
# print(type(a2), a2)
# 此时就报错了
# 万物皆可转字符串加上引号就可以 字符串转数字 必须保证 字符串内容是数字才可以
# 整数转浮点数 是可以的 浮点数转整数也是可以的 但是会损失精度


# 目标二：标识符
# 不可以数字开头 不推荐使用中文 区分大小写

