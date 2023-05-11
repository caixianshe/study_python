# 数据容器set集合
# 列表可修改、 支持重复元素且有序
# 元组、字符串不可修改、支持重复元素且有序
# 集合 不支持元素的重复、无序
# 列表为[] 元组为() 字符串为"" 集合为{} 字典{key：value}

my_set = {"张三", "李四", "王五", "李四", "李四", "李四", "李四"}
# test_set = {}
test_set = set()  # 定义空集合
print(f"my_set的值为:{my_set}，元素类型为{type(my_set)}")
print(f"test_set的值为:{test_set}，元素类型为{type(test_set)}")

# 以为set集合是无序的 所以不支持索引下标访问 但是集合和列表一样 支持修改
# 添加一个元素 add
my_set = {"张三", "李四"}
my_set.add("set集合")
print(f"my_set集合后的元素为{my_set}")

# 取出一个元素 pop 因为没有索引 所以只能随机取
pop = my_set.pop()
print(f"取出后的元素结果为{my_set}，被取出的元素为{pop}")

# 清空集合 clear  注意 清空之后是没有返回值的 下面是错误示范
# set_clear = my_set.clear()
my_set.clear()
print(f"清空后的set集合元素为：{my_set}")  # set()表示空集合

# 取两个集合的差集 以set1为基准 取出set1集合有的 而set2集合没有的
set1 = {1, 2, 3}
set2 = {1, 5, 7}
set_difference = set1.difference(set2)
print(f"两个集合的差集为{set_difference}，取出后set1为：{set1}set2为：{set2}")

# 消除两个集合的差集 以前面为基准 消除前者有的  而后者没有的元素  同时 也没有返回值
# difference_update = set1.difference_update(set2)  #错误示范
set1.difference_update(set2)
print(f"消除后set1为：{set1}set2为：{set2}")

# 两个集合合并为一个集合
set_union = set1.union(set2)
print(f"合并后的集合为{set_union}，合并后的set1：{set1}，set2：{set2}")

# 统计集合元素数量
i = len(set_union)  # 注意 这里的元素个数是去重后的元素个数 因为set集合只能存储不同的元素
print(f"集合的数量有{i}个")

# 集合的遍历 没有索引 所以不能采用while循环遍历
for x in set_union:
    print(f"元素为：{x}")

# 课后练习
# 定义一个列表
my_set = ["张三", "李四", "王五", "李四", "李四", "李四", "李四"]
result_set = set()
for x in my_set:
    result_set.add(x)
print(f"列表的值为{my_set}")
print(f"最后遍历添加到空集合的结果为{result_set}")
