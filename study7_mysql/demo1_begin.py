# 导入mysql的包  pymysql包  因为没装mysql
con = Connection(
    host="127.0.0.1",
    port=3306,
    user="账号",  # 账户和密码都是引号引起来的
    password="密码",
    #如果想要自动提交需要开启
    # autocommit=True #设置自动提交
)

# # --1  执行非查询性sql
# #获取游标对象
# cursor = con.cursor()
#
# # 选择数据库
# con.select_db("数据库名字")
#
# #使用游标对象执行sql
# cursor.execute("你写的sql")

# --2  执行查询性sql
# cursor = con.cursor()
# # 选择数据库
# con.select_db("数据库名字")
#
# # 使用游标对象执行sql
# cursor.execute("你写的sql")
#
# # 获取结果 结果是k v的形式 （元组）
# result = cursor.fetchall()
#
# for x in result:
#     print(x)


# --第三种情况插入数据 插入数据的时候 需要我们去手动提交的 也就是commit
# 如果想自动提交那么需要在Connection连接的时候 设置autocommit=True就可以了
cursor = con.cursor()
# 选择数据库
con.select_db("数据库名字")

# 使用游标对象执行sql
cursor.execute("你写的sql")

cursor.commit()
# 关闭连接
con.close()
