from pyspark import SparkConf, SparkContext

# local[*]  中间不可以 local [*] 有空格的话就会报错
conf = SparkConf().setMaster("local[*]").setAppName("spark_test_2")

sc = SparkContext(conf=conf)

# 这些是读取数据容器
# add1 = sc.parallelize([1, 2, 3, 4])  # 列表
# add2 = sc.parallelize((1, 2, 3, 4))  # 元组
# add3 = sc.parallelize("abcdefgh")  # 字符串
# add4 = sc.parallelize({1, 2, 3, 4})  # 集合
# add5 = sc.parallelize({"姓名": "张三", "性别": "男"})  # 字典

# 读取文件 用textFile
add6 = sc.textFile("F:/workspace/python-study/test.txt")

# 打印的话不能直接打印add 而是通过collect()
# print(add1.collect())
# print(add2.collect())
# print(add3.collect())
# print(add4.collect())
# print(add5.collect())
print(add6.collect())

sc.stop()
