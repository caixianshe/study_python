# 数据容器 字符串
# 作为数据容器，字符串有如下特点:
# 只可以存储字符串
# 长度任意(取决于内存大小)
# 支持下标索引
# 允许重复字符串存在
# 不可以修改(增加或删除元素等)
# 支持for循环

# 和前面的字符串基本上一样的 但是字符串也可以作为存储字符的容器
my_str = "wo shi da shuai ge"
# 通过下标索引取出d
str_name = my_str[7]
print(f"7索引所在的元素是d:{str_name}")

# index方法
index = my_str.index("d")
print(f"d所在的位置为{index}")

# replace方法 （字符串是不支持修改的 替换之后是相当于返回新的字符串）
replace_str = my_str.replace("wo", "ni")
print(f"将原有的{my_str}替换为{replace_str}")

# split 分割 把分割后的字符串放到新的列表中
split_list = my_str.split(" ")
print(f"分割前为{my_str}：分割后为{split_list}")

# strip 方法
my_str = "  wo shi da shuai ge  "
strip = my_str.strip()
print(f"原字符串为{my_str}去除字符串前后的空格后为{strip} ")

# 注意 此时的去除的时候不是按照12去除的 是按照字符1 字符2去除的 只要有就会去掉
my_str = "12wo shi da shuai ge21"
str_strip = my_str.strip("12")
print(f"原字符串为{my_str}去除字符串12后为{strip} ")

# 统计字符串中 字符出现的次数
my_str = "12wo shi da shuai ge21"
count = my_str.count("i")
print(f"统计i出现的次数为{count}")

# 统计字符串的长度
str_len = len(my_str)
print(f"字符串为{my_str}长度为{str_len}")
