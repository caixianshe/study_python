# 编码 现在我们基本上默认采用utf-8的编码格式 (ASCII 码中--汉字占2个字节， utf-8中--中文占三个字节  这两种编码英文字母占一个字节，中文符号占两个字节，英文符号占一个字节。)
# 编码格式有 UTF-8  UTF-16 GBK 等 现在默认都是采用utf-8的形式进行编码

#  目标一： 格式 open(文件地址，打开的方式，第三是不是encoding所以采用关键字参数) r读  w写  a追加  如果在w写入的模式下 文件不存在系统会帮我们创建文件
# 打开
import time

t = open("F:\workspace\python-study\测试文本.txt", "r", encoding="UTF-8")
print(type(t))

# 注意 此时是读了10个字节的 但是下次读取全部的时候 是从前面读取前10个字节之后的地方读取的全部 相当于指针
#  简单的说 就是读取上次read读取的地方开始读  如果没有读取过 就从头开始读取
# print(f"读取十个字节：{t.read(10)}")
# print(f"读取全部：{t.read()}")

#   目标二： 读取文件数据   注意 readline 和readlines 是不一样的 前者读取的类型为str 后者为list
# readline = t.readline()
# readlines = t.readlines()
print('===================')
# 注意 readlines 也是从read读取之后的位置读的 read没有读过  那么就从头开始读
# print(f"读取的文件类型为：{type(readlines)}")
# print(f"读取的内容为：{readlines}")

# 目标三 ：读取一行数据 readline  按行读取
# readline = t.readline()
# readline2= t.readline()
# print(f"读取的文件类型为：{type(readline)}")
# print(f"读取第一行：{readline}")
# # 注意 这里是因为你输出的是同一个对象所以不会读取下一行 要重新接着读才会从第一次读取的位置之后读
# # print(f"读取第一行：{readline}")
# print(f"读取第二行：{readline2}")

# 目标四：for循环 读取文件行
# for x in t:
#     # print(t.readline())  # 这种写法不对
#     print(f"读取每一行的数据为{x}")

# 目标五：文件关闭
# t.close()


# 目标六 with open 语法操作文件  执行完里面的语句块之后 会自动的关闭文件
with open("F:\workspace\python-study\测试文本.txt", "r", encoding="UTF-8") as a:
    for x in a:
        print(f"每一行的数据为{x}")
