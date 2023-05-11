# 循环遍历取出列表中的每一个元素

# while 循环
list_one = ["今天", "昨天", "明天", "下雨天", "晴天"]

list_two = [1, 2, 3, 4, 5, 6]


def while_list(wh_list):
    index = 0
    while len(wh_list) > index:
        print(f"第{index}个元素是{wh_list[index]}")
        index += 1


# for 循环
def for_list(f_list):
    for x in f_list:
        print(x)


while_list(list_one)
print("============")
while_list(list_two)
print("============")
for_list(list_one)
print("============")
for_list(list_two)
