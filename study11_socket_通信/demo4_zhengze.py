#
# 字符               功能
# .                 匹配任意1个字符(除了\n)，\.匹配点本身
# []                匹配[]中列举的字符
# \d                匹配数字，即0-9
# \D                匹配非数字
# \s                匹配空白，即空格、tab键
# \S                匹配非空白
# \w                匹配单词字符，即a-Z、A-Z、 0-9、_
# \W                匹配非单词字符


# 数量匹配:
# 字符                功能
# *                 匹配前一个规则的字符出现0至无数次
# +                 匹配前一个规则的字符出现1至无数次
# ?                 匹配前一个规则的字符出现0次或1次
# {m}               匹配前一个规则的字符出现m次
# {m,}              匹配前一个规则的字符出现最少m次
# {m,n}             匹配前一个规则的字符出现m到n次


# 边界匹配:
# 字符                功能
# ^                 匹配字符串开头
# $                 匹配字符串结尾
# \b                匹配一个单词的边界
# \B                匹配非单词边界


# 分组匹配:
# 字符                功能
# |                 匹配左右任意一个表达式
# ()                将括号中字符作为一个分组

import re

s = "caicai 12  ! ni - * / zhen de hao shuai a  QAQ 11321"
# 注意此时的r作用是表明转义字符无效 当做字符串进行处理
# 任务一：找出全部的数字
result = re.findall(r"\d", s)
print(result)

# 任务二：找出特殊字符
result2 = re.findall(r"\W", s)
print(result2)

# 任务三：找出所有的单词  不想找到数字
# result3=re.findall(r"\w",s)
result3 = re.findall("[a-zA-Z]", s)
print(result3)

# 如果我只想要找出我指定的字符
result4 = re.findall("[czAQ]", s)
print(result4)
