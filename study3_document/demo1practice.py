# 读取word.txt文件 统计it黑马出现的次数
t = open("F:\workspace\python-study\word.txt", 'r', encoding="utf-8")
print(f"数据类型为:{type(t)}")

# 方式一
read = t.read()
print(type(read))
count = read.count("itheima")
print(count)

# 方式二：
# numbers = 0
# for x in t:
#     # strip 作用是剔除 开头和结尾的空格以及换行符
#     x_strip = x.strip()
#     # print(x_strip)
#     split = x_strip.split(" ")
#     for s in split:
#         if s == "itheima":
#             numbers += 1
# print(f"itheima出现的次数为：{numbers}次")

# 记得要关闭文件
t.close()
