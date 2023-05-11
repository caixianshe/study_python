# 案例通过读取文件 统计单词出现的个数 最后使用sortBy 进行排序

from pyspark import SparkConf, SparkContext
import os

os.environ["PYSPARK_PYTHON"] = "C:/Users/czj/AppData/Local/Programs/Python/Python310/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("pyspark_test_1")
sc = SparkContext(conf=conf)

text_rdd = sc.textFile("F:/workspace/python-study/t1.txt")
# map是有嵌套的  用flatMap 解除嵌套 ()里传入的是规则

resource_raa = text_rdd.flatMap(lambda x: x.split(" "))
# 此时已经解套 使用map把他们变成k-v的形式 然后使用reduceByKey 让value做累加计算出现的次数
end = resource_raa.map(lambda x: (x, 1))

end_rdd = end.reduceByKey(lambda x, y: x + y)

# 此时我想要对结果进行降序排列 根据函数确定排序的规则 如果出现多个值 可以采用下面的方法进行设置 ascending为true时是升序
# numPartitions是全局排序 涉及到分布式 没学 所以我们现在设置为1就可以了
rdd_sort_by = end_rdd.sortBy(lambda a: a[1], ascending=False, numPartitions=1)

print(rdd_sort_by.collect())

sc.stop()

# [('itheima', 7), ('python', 6), ('itcast', 4), ('spark', 4), ('pyspark', 3)]
