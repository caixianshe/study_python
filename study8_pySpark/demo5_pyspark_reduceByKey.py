# reduceByKey算子
# 根据k分组 然后对v进行两两计算 v是两两相加 加完之后与第三个相加

from pyspark import SparkConf, SparkContext
import os


os.environ['PYSPARK_PYTHON'] = "C:/Users/czj/AppData/Local/Programs/Python/Python310/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("spark_test_2")
sc = SparkContext(conf=conf)

rdd1 = sc.parallelize([("男", 99), ("女", 50), ("男", 98), ("女", 49)])

# 两两计算的逻辑
rdd2 = rdd1.reduceByKey(lambda a, b: a + b)

print(rdd2.collect())

sc.stop()


# [('男', 197), ('女', 99)]