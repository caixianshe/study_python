# distinct 空参去重

from pyspark import SparkConf, SparkContext
import os

os.environ["PYSPARK_PYTHON"] = "C:/Users/czj/AppData/Local/Programs/Python/Python310/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_pypark")

sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5, 1, 2, 3, 5, 7, 89, 7])

rdd_distinct = rdd.distinct()
print(rdd_distinct.collect())

sc.stop()

# [2, 4, 1, 3, 5, 7, 89]
# 只能去重 但是顺序不做保证