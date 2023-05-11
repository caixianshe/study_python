# json  [] 列表  {key：value}字典
# 在python中 就是{"name":"张三","age":18} 这个就是json 也就是字典
# 或者[{"name":"张三","age":18},{"name":"李四","age":19}] 列表 但是列表内必须是元组

"""
演示json与python之间的相互转换
json.dumps
json.loads
# 注意 json字符串 希望里面的用双引号引起来  否则会报 json.decoder.JSONDecodeError
"""
import json

# 准备列表
list_json = [{"name": "张三", "age": 18}, {"name": "李四", "age": 19}, {"name": "王五", "age": 19}]
# 将列表转为json json.dumps
json_str = json.dumps(list_json, ensure_ascii=False)  # 如果不加ensure_ascii=False 默认汉字将用aci码表表示
print(f"转换之后的类型为:{type(json_str)}")
print(f"转换之后的结果为:{json_str}")

# 将字典转换为json格式的字符串 json.dumps
dirt_json = {"name": "张三", "age": 18}
json_dirt = json.dumps(dirt_json, ensure_ascii=False)
print(f"转换之后的类型为:{type(json_dirt)}")
print(f"转换之后的结果为:{json_dirt}")

# 将json数据转换为python数据 json.loads
json_list_one = '[{"name": "张三", "age": 18}, {"name": "李四", "age": 19}, {"name": "王五", "age": 19}]'
python_date = json.loads(json_list_one)
print(f"转换之后的类型为:{type(python_date)}")
print(f"转换之后的结果为:{python_date}")

# demo = "[{'name': '张三', 'age': 18}, {'name': '李四', 'age': 19}, {'name': '王五', 'age': 19}]"
# demo1 = json.loads(demo)
# print(f"转换之后的类型为:{type(demo1)}")
# print(f"转换之后的结果为:{demo1}")


# 新目标===开发可视化图表使用的技术栈是:
# Echarts框架的Python版本:  PyEcharts包
# 官方示例：https://gallery.pyecharts.org/#/README
