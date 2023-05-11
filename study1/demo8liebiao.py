# 第八天:数据容器
# (list列表 [] ,tuple元组 (,),str字符串 "",set集合{},dict字典 {key：value})  注意：list列表可以被修改  元组 一旦定义完成，就不可以修改并且元组要加逗号 不然就是字符串

# 一种可以容纳多份数据的数据类型
# 容纳的每一份数据称之为1个元素
# 每一个元素，可以是任意类型的数据，如字符串、数字、布尔等。

# 目标一:列表 (定义格式)  [元素一,元素二,元素三]  注意 里面的元素可以存放任意数据类型 支持列表嵌套
name_list = [["张三", "男", 2, True], ["豪宅", "桌子", "板凳", "钥匙"]]
print("# ===列表 (定义格式)===")
print(name_list)  # ['张三', '男', 2, True ,['豪宅', '桌子', '板凳', '钥匙']]
print(type(name_list))  # <class 'list'>

# 目标二：列表的下标索引
name_list = ["张三", "李四", "王五"]
print("# ===列表的下标索引(正向)===")
print(name_list[0])
print(name_list[1])
print(name_list[2])

print("# ===列表的下标索引(反向)===")  # 从最后一个往前推
print(name_list[-1])
print(name_list[-2])
print(name_list[-3])

print("# ===嵌套列表的下标索引===")  # 取李四
name_list = [["张三", "李四", "王五"], ["小可爱", "小天才", "小猪猪"]]
print(name_list[0][1])
print(name_list[0])


# 目标二：列表的常用操作方法
# 函数和方法的区别： 如果将函数定义在class中 那么将函数称之为 方法
# 函数与方法的功能一样，有传入参数 有返回值 只是方法的使用格式不同
# 函数
def add(x, y):
    return x + y


# 方法
class Student:
    def add(self, x, y):
        return x + y


# 两者的调用方式
num = add(1, 2)

student = Student()
student_add = student.add(2, 3)
print("# ===两者的调用方式===")
print(f"函数的调用结果:{num}")
print(f"方法的调用结果:{student_add}")

# 常用方法一：查询元素在列表中的下标位置  语法：列表.index(元素)
mylist = ["张三", "李四", "王五"]
people_num = mylist.index("李四")
print("# ===查询元素在列表中的下标位置===")
print(people_num)

# 方法二：修改特定元素下标的值 语法：列表[元素下标]=新值
mylist[0] = "小可爱"
print("# ===修改后的mylist的值===")
print(mylist)

# 方法三：在指定位置插入元素 语法：列表.insert(插入后的位置，元素)
mylist.insert(1, "大可爱")
print("# ===插入指定位置元素后 mylist的值===")
print(mylist)

# 方法四：追加元素（是在列表的末尾追加元素） 语法：列表.append(元素)
mylist.append("小惊喜")
print("# ===追加元素后 mylist的值===")
print(mylist)

# 方法四 扩展方法二：追加一批元素  语法：列表.extend(列表容器)
super_list = ["ck包包", "迪奥口红", "雅诗兰黛粉底"]
mylist.extend(super_list)
print("# ===追加一批元素后 mylist的值===")
print(mylist)

# 方法五 删除元素 语法一：del 列表[元素下标] 语法二：列表.pop(元素下标) 返回值为删除的元素
# def mylist [2]    #注意删除 是del 不是def
del mylist[2]
print("# ===通过del删除元素后 mylist的值===")
print(mylist)

temp = mylist.pop(2)
print("# ===通过pop删除元素后 mylist的值===")
print(f"通过pop取出元素后的结果：{mylist}，取出的元素是：{temp}")

# 方法六 通过指定元素 删除元素 语法 列表.remove(元素) 注意 当重复的元素有多个的时候 只能删除第一个 后面重复的元素 需要多次调用才可以删除
mylist.remove("雅诗兰黛粉底")
print("# ===通过remove删除元素后 mylist的值===")
print(mylist)

# 方法七：清空列表 语法 列表.clear()
mylist.clear()
print("# ===通过clear清空元素后 mylist的值===")
print(mylist)

# 方法八 统计列表中 某个元素的个数
mylist = ["张三", "李四", "王五", 1, 2, 1]
count = mylist.count(1)
print("# ===某个元素的个数 mylist的数量有===")
print(count)

# 统计列表中有多少个元素 语法 len(列表) len是函数
i = len(mylist)
print(i)
