def number_add(x, y):
    print(x + y)


# 当我们右键运行的时候 __name__就会设置成__main__ 也就是说 if判断就为true了
if __name__ == '__main__':
    number_add(1, 3)
