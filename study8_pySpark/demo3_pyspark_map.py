from pyspark import SparkConf, SparkContext
import os

# 'PYSPARK_PYTHON' 这个不是随便写的 写别的会报错
os.environ['PYSPARK_PYTHON'] = "C:/Users/czj/AppData/Local/Programs/Python/Python310/python.exe"
# 这个是分布式的 所以有时候可能找不到路径

conf = SparkConf().setMaster("local[*]").setAppName("spark_test_2")

sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5])


# def func(data):
#     return data * 10
#
#
# # map是对其进行数据处理的
# # 这里是map方法的作用是 会将rdd每一个值 传递给func
# rdd2 = rdd.map(func)


# 采用lambda的方式简化上面定义的方式 支持链式调用
rdd2 = rdd.map(lambda x: x * 10).map(lambda x: x + 5)

print(rdd2.collect())

sc.stop()


# [10, 20, 30, 40, 50]
