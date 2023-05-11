# flatMap算子
# 功能:对rdd执行map操作,然后进行解除嵌套操作.
# 与map的区别就是 多了一层解除嵌套的操作

# eg：嵌套list
a1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 解除嵌套的列表
a2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

from pyspark import SparkConf, SparkContext
import os

# 设置python执行路径 因为是多线程的情况下 有的线程不一定能找到位置
os.environ['PYSPARK_PYTHON'] = "C:/Users/czj/AppData/Local/Programs/Python/Python310/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("spark_test_2")
sc = SparkContext(conf=conf)

add1 = sc.parallelize(["张三 李四 王五", "吃饭 学习 打游戏", "王者 吃鸡 逃离"])
# add2 = add1.map(lambda x: x.split(" "))#[['张三', '李四', '王五'], ['吃饭', '学习', '打游戏'], ['王者', '吃鸡', '逃离']]
# 此时想要把里面全部单个取出
add2 = add1.flatMap(lambda x: x.split(" "))  # [['张三', '李四', '王五'], ['吃饭', '学习', '打游戏'], ['王者', '吃鸡', '逃离']]

print(add2.collect())

sc.stop()
