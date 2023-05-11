# 数据输出 输出为python对象
# 数据输出
# 1 collect() 把rdd转换成列表的形式输出 返回值是个列表
# 1 reduce() 两两相加把结果结果输出 返回值是个数字
# 3 take() 取前n个元素 组成list返回给你
# 4 count() 统计rdd里有多少条数据 返回值是个数字

from pyspark import SparkConf, SparkContext
import os

os.environ["PYSPARK_PYTHON"] = "C:/Users/czj/AppData/Local/Programs/Python/Python310/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_pypark")

sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5])
rdd_reduce = rdd.reduce(lambda x, y: x + y)
# 与reduceBykey不同 reduce是两两相加
rdd_take = rdd.take(3)
rdd_count = rdd.count()

print(rdd.collect())  # [1, 2, 3, 4, 5]
print(rdd_reduce)  # 15
print(rdd_take)  # [1, 2, 3]
print(rdd_count)  # 5

sc.stop()

#  152 153 没做练习 需要配置hadoop配置依赖等 没有弄
