# 大规模的分布式集群  导包 现在的环境版本太低了 不支持下载这个包 所以 暂时不能用
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("pyspark_test")

sc = SparkContext(conf=conf)
print(sc.version)

sc.stop()


# 1.如何安装PySpark库
# pip install pyspark

# 2.为什么要构建SparkContext对象作为执行入口
# PySpark的功能都是从SparkContext对象作为开始

# 3. PySpark的编程模型是?
# 数据输入:通过SparkContext完成数据读取
# 数据计算: 读取到的数据转换为RDD对象,调用RDD的成员方法完成计算
# 数据输出:调用RDD的数据输出相关成员方法,将结果输出到list、元组、字典、文本文件、数据库等
