# 读取文件 备份到bill.txt.bak文件 测试数据不要

t = open("F:\workspace\python-study/bill.txt", "r", encoding="utf-8")
b = open("F:\workspace\python-study/bill.txt.bak", "a", encoding="utf-8")
for x in t:
    # print(type(x))
    # print(x)

    # strip去除后的结果是字符串 而split切割后的结果为集合
    x_strip = x.strip()  # 去除前后空格和换行符
    if x_strip.split(",")[4] == "测试":
        continue
    b.write(x_strip)  # 注意 只能写入字符串格式 不能写入集合格式
    b.write("\n")

t.close()
b.close()
