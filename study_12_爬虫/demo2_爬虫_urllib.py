# https://www.bilibili.com/video/BV1Db4y1m7Ho?p=70&vd_source=8ad96aba75f23d4a5862ddb7d26aedcb 学习爬虫的连接 尚硅谷的
#  urllib的四个方法
import urllib.request

# #使用urllib来获取百度首页的源码

# (1)定义一个url就足你要访问的地址
# 注意 因为百度有反扒 所以下面的连接 没用请求定制是不可以的
url = 'http://www.baidu.com'

# (2)模拟浏微器向服务器发送请求响应响应
response = urllib.request.urlopen(url)

# (3)获取响应中的页面的源码
# Read方法返回的是字节形式的二进制数据
# 我们要将二进制数据转换成为字符串
# 此时我们要采用 decode("加上编码格式")  进行解码（解码就是从二进制转换为字符串的这个过程）
content = response.read().decode('utf-8')

print(content)
