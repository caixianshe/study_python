# 元组 tuple 元组一旦定义完成 就不支持修改

# 目标一：定义元组
t1 = (1, "元组", True)
# 目标二： 定义空元组
t2 = ()
t3 = tuple()

print("# ===定义元组===")
print(f"元组一{t1}")
print(f"定义的类型是{type(t1)}")
print("# ===定义空元组===")
print(f"元组二{t2}")
print(f"定义的类型是{type(t2)}")
print(f"元组三{t3}")
print(f"定义的类型是{type(t3)}")

# 目标三 定义单个元素  注意 如果不加逗号 则表示字符串类型
t4 = ("hello",)
print(f"t4的类型是{type(t4)}")

# 目标四 元组的嵌套
t5 = (("张三", "李四", "王五"), (1, 2, 3, "你真帅"),)
print(f"t5的类型是{type(t5)},值为{t5}")

# 目标五 下标索引 去取内容
index = t5[1][3]
print(f"我想找到下标为1,3的值为{index}")

# 目标六 元组操作 通过指定元素查找下标
t6 = (1, 2, 3, "你真帅",)
num = t6.index("你真帅")
print(f"你真帅所在的位置是：{num} 类型是{type(t6)}")

# 目标七 元组操作 统计某个元素出现的次数
t7 = (1, 2, 3, "你真帅", "你真帅", "你真帅", "你真帅",)
count = t7.count("你真帅")
print(f"统计你真帅的频率{count}")

# 目标八 元组操作 统计元组的长度 len
i1 = len(t7)
i2 = len(t5)
print(f"t7的长度为{i1}")
print(f"t5的长度为{i2}")

# 目标九 元组的while遍历
index = 0
while index < len(t7):
    print(t7[index])
    index += 1

print("华丽的分割线==========")
# 目标十 元组的for遍历
for x in t7:
    print(x)

# 注意 元组内的元素 是不可以修改的 测试
# t7[0] = "张三"
# print(t7)

# 虽然元素不可以修改 但是有特例 比如在元组里面嵌套一个list列表 列表里的内容是可以修改的
a2 = (1, 2, 3, [4, 5, 6])
print(f"a2修改前的内容是{a2}")
a2[3][0] = 7
a2[3][1] = 8
a2[3][2] = 9
print(f"a2修改后的内容是{a2}")
