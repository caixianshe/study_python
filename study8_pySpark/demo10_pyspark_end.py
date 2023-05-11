# 练习
import json

from pyspark import SparkConf, SparkContext
import os

os.environ["PYSPARK_PYTHON"] = "C:/Users/czj/AppData/Local/Programs/Python/Python310/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("pyspark_test")
sc = SparkContext(conf=conf)

# 注意文件路径不对 这个要改
file_rdd = sc.textFile("C:/Users/czj/PycharmProjects/pythonProject/orders.txt")

# 解除嵌套
json_rdd = file_rdd.flatMap(lambda x: x.split("|"))

dict_rdd = json_rdd.map(lambda x: json.loads(x))
# 取出城市和销售数据
rdd_map = dict_rdd.map(lambda x: (x["areaName"], int(x["money"])))
# 按照城市分组 按照销售额聚合
# 按照销售额结果进行聚合排序
key = rdd_map.reduceByKey(lambda x, y: x + y).sortBy(lambda x: x[1], ascending=False, numPartitions=1)

# 需求二:全部城市有哪些商品类别在售卖
result2_rdd = dict_rdd.map(lambda x: x["category"]).distinct()

# 需求三:北京市有哪些商品类别在售卖
r = dict_rdd.filter(lambda x: x["areaName"] == "北京").map(lambda x: x["category"]).distinct()

# print(r.collect())

print(f"需求一的结果为：{key.collect()}")
print(f"全部城市有{result2_rdd.collect()}商品类别在售卖")
print(f"北京市有{result2_rdd.collect()}商品类别在售卖")

sc.stop()
