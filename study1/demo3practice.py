# demo3的练习

name = "张三"
stock_prodk = 19.99
stock_code = "10086"
xishu = 1.2
day = 7
print(f"姓名：{name}，股票代码：{stock_code}，当前股价{stock_prodk}")
print("每日增长的系数%f，经过%d天的增长后，股价达到了：%.2f" % (xishu, day, stock_prodk * xishu ** day))
