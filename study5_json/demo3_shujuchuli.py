# 通过json模块 对数据进行处理  []列表 ()元组
# 弄个地图
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

map = Map()
# 准备数据
data = [
    ("北京市", 99),
    ("浙江省", 199),
    ("上海市", 299),
    ("安徽省", 399)
]
# 添加数据
map.add("测试地图", data, "china")
# 设置全局
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 9, "label": "1-9", "color": "#CCFFFF"},
            {"min": 10, "max": 99, "label": "10-99", "color": "#FF6666"},
            {"min": 100, "max": 500, "label": "100-500", "color": "#990033"}

        ]
    )
)
# 绘制地图
map.render()
