# 数据容器 字典 dict
# 字典的定义
my_dict1 = {"张三": 18, "李四": 18, "王五": 19}
my_dict2 = {}  # 声明方式一
my_dict3 = dict()  # 声明方式二
print(my_dict1)
print(f"1的值为{my_dict1}，元素类型为{type(my_dict1)}")
print(f"1的值为{my_dict2}，元素类型为{type(my_dict2)}")
print(f"1的值为{my_dict3}，元素类型为{type(my_dict3)}")

# 取出李四的value
my_dict1_value = my_dict1["李四"]
print(f"李四的年龄为{my_dict1_value}")

# 字典和集合一样没有下标 所以不可以使用索引  key和value可以为任意类型 key不可以为字典
# 字典中的key不可以重复 重复添加等同于覆盖掉原有的数据

# 字典的常用操作
my_dict4 = {"张三": 18, "李四": 18, "王五": 19}
# 字典元素的新增
my_dict4["小可爱"] = 20
print(f"my_dict4添加元素后的值为{my_dict4}")

# 更新元素
my_dict4["小可爱"] = 18
print(f"my_dict4更新元素后的值为{my_dict4}")

# 删除元素  pop 移除某个元素
my_dict4_pop = my_dict4.pop("张三")
print(f"my_dict4删除元素后的值为{my_dict4}")

# 清空元素
my_dict4.clear()
print(f"my_dict4清空元素后的值为{my_dict4}")

# 遍历字典
my_dict5 = {"张三": 18, "李四": 18, "王五": 19}
# 方式一：
keys = my_dict5.keys()
# print(key)
for key in keys:
    print(f"key为{key},值为{my_dict5[key]}")

# 方式二：
for x in my_dict5:
    print(f"key为{x},值为{my_dict5[key]}")

# 字典的数量
i = len(my_dict5)
print(i)


