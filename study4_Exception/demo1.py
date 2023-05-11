# 简单的认识异常

# 读取一个不存在的文件 会报异常 FileNotFoundError
# t = open("D:/a", "r", encoding="utf-8")
# read = t.read()
# print(read)
# t.close()

# 什么是异常：所谓的异常就是程序在运行过程中出现的错误

# 目标二：异常的捕获 处理
# try:
# except:
# try:
#     t = open("F:\workspace\python-study/study2.txt", "r", encoding="utf-8")
#
# except:
#     t = open("F:\workspace\python-study/study2.txt", "w", encoding="utf-8")
#     t.write("你好啊")
#
# t.flush()
# # 在写入的模式下不可读
# read = t.read()
# print(read)
# t.close()

# 目标三： 捕获 指定异常 并作出处理  多个异常出现时 第一个异常出现后进行捕货处理 后面的就不会执行
# try:
#     # t = open("F:\workspace\python-study/study2.txt", "r", encoding="utf-8")
#     # 如果是1/0异常就不会进行捕获处理 而是直接打印出来了
#     1 / 0
# # as a可以不写 a为异常对象 也就是异常信息
# except FileNotFoundError as a:
#     print(f"系统错误 错误类型为'FileNotFoundError'")
#     print(a)

# 目标四： 捕获 多个异常 并作出处理 异常类型用元组给包裹起来
# try:
#     t = open("F:\workspace\python-study/study2.txt", "r", encoding="utf-8")
#     1 / 0
# except (ZeroDivisionError, FileNotFoundError) as a:
#     print("系统错误 错误类型为'FileNotFoundError'或者是'ZeroDivisionError' ")

# 目标五： 捕获所有的异常（比如用在 不知道会出现什么异常的情况）  Exception 或者 except后面什么都不写
# try:
#     t = open("F:\workspace\python-study/study2.txt", "r", encoding="utf-8")
#     1 / 0
# # except Exception as b:
# #     print("出现错误")
#
# except:
#     print("出现错误")

# 目标六：如果没有出现异常的时候 else 这个可以加可以不加
# try:
#     print("hello")
# except:
#     print("出现错误")
# else:
#     print("好开心啊")

# 目标七: 不管有没有出现异常 我都要执行的代码 finally
try:
    # print("hello")
    1 / 0
except:
    print("出现错误")
else:
    print("好开心啊")
finally:
    print("不管你成不成功，我一定要出现")

