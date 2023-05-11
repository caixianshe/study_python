# 案例通过读取文件 统计单词出现的个数

from pyspark import SparkConf, SparkContext
import os

os.environ["PYSPARK_PYTHON"] = "C:/Users/czj/AppData/Local/Programs/Python/Python310/python.exe"

# conf = SparkConf.setMaster("local[*]").setAppName("pyspark_test_1")
# 注意是SparkConf()是有()的
conf = SparkConf().setMaster("local[*]").setAppName("pyspark_test_1")
sc = SparkContext(conf=conf)

text_rdd = sc.textFile("F:/workspace/python-study/t1.txt")

# map是有嵌套的  用flatMap 解除嵌套 ()里传入的是规则
resource_raa = text_rdd.flatMap(lambda x: x.split(" "))
# ['itheima', 'itheima', 'itcast', 'itheima', 'spark', 'python', 'spark', 'python', 'itheima', 'itheima', 'itcast', 'itcast', 'itheima', 'python', 'python', 'python', 'spark', 'pyspark', 'pyspark', 'itheima', 'python', 'pyspark', 'itcast', 'spark']

# 此时已经解套 使用map把他们变成k-v的形式 然后使用reduceByKey 让value做累加计算出现的次数
end = resource_raa.map(lambda x: (x, 1))
#[('itheima', 1), ('itheima', 1), ('itcast', 1), ('itheima', 1), ('spark', 1), ('python', 1), ('spark', 1), ('python', 1), ('itheima', 1), ('itheima', 1), ('itcast', 1), ('itcast', 1), ('itheima', 1), ('python', 1), ('python', 1), ('python', 1), ('spark', 1), ('pyspark', 1), ('pyspark', 1), ('itheima', 1), ('python', 1), ('pyspark', 1), ('itcast', 1), ('spark', 1)]

end_rdd = end.reduceByKey(lambda x, y: x + y)
print(end_rdd.collect())

sc.stop()
# [('itcast', 4), ('python', 6), ('itheima', 7), ('spark', 4), ('pyspark', 3)]
