# #
# Python正则表达式,使用re模块,并基于re模块中三个基础方法来做正则匹配。
# 分别是: match. search. findall三个基础方法
# re.match(匹配规则， 被匹配字符串)
# 从被匹配字符串开头进行匹配，匹配成功返回匹配对象(包含匹配的信息)，匹配不成功返回空。

import re

# match  从头匹配 如果开始不是就会返回None
s1 = "1caicai ni zhen ke ai"
s = "caicai ni zhen ke ai"
result = re.match("caicai", s)
result2 = re.match("caicai", s1)

# 前面是匹配的规则 后面是对象
print(result)
# print(result.group())
# print(result.span())
print(result2)


# search(匹配规则，被匹配字符串)
# 搜索整个字符串,找出匹配的。从前向后,找到第一个后,就停止,不会继续向后
result3 = re.search("cai", s1)
print(result3)

# findall 全部匹配
result4 = re.findall("cai", s1)
print(result4)
