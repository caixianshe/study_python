from demo7_file import Text_read, Json_read, FileReader
# 构造柱状图
from pyecharts.charts import Bar
# 构建一些可选项
from pyecharts.options import *
# 设置主题 控制图表的颜色
from pyecharts.globals import ThemeType

text_read = Text_read("F:\workspace\python-study/2011年1月销售数据.txt")
json_read = Json_read("F:\workspace\python-study/2011年2月销售数据JSON.txt")

textDate = text_read.read_date()  # 1009条
jsonDate = json_read.read_date()  # 978条

allList = textDate + jsonDate

dict_list = {}
for x in allList:
    if x.date in dict_list:
        dict_list[x.date] += x.money
    else:
        # 如果不存在的话就新建 k v的形式
        dict_list[x.date] = x.money

# print(dict_list)

# 可视化图表的开发
bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))  # 在这里设置主题颜色  init_opts=InitOpts(theme=ThemeType.LIGHT)

bar.add_xaxis(list(dict_list.keys()))  # x轴数据
bar.add_yaxis("销售额", list(dict_list.values()), label_opts=LegendOpts(is_show=False))  # y轴数据  label_opts=LegendOpts(is_show=False) 设置不显示数
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")
)

# 生成柱状图
bar.render("销售数据统计图.html")
