# 演示地图模块
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

line = Line()
line.add_xaxis(["中国", "英国", "美国"])
line.add_yaxis("GDP", [30, 20, 10])

# 更改全局配置选项
# 设置全局配置项set_global_opts来设置,
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    # 工具箱
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
    # 剩下的全局配置项可以在 https://pyecharts.org/#/zh-cn/global_options 找
)

line.render()
