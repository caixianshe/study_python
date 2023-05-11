# filter 过滤
from pyspark import SparkConf, SparkContext
import os

os.environ["PYSPARK_PYTHON"] = "C:/Users/czj/AppData/Local/Programs/Python/Python310/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_pyspark")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5])

# 返回为true的结果保留  通过函数(也可以通过lambda表达式)去控制true or false
rdd_filter = rdd.filter(lambda x: x % 2 == 0)
print(rdd_filter.collect())

sc.stop()

# [2, 4]
