import urllib.request

url = "https://www.baidu.com"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)
# 模拟浏览器访问网站
response = urllib.request.urlopen(request)
# 获取网页源码
content = response.read().decode("utf-8")

# print(content)
# 解析源码 获取我们想要的数据
from lxml import etree

# 解析服务器响应的文件
tree = etree.HTML(content)

# 获取想要的数据
# 打开浏览器 使用xpath插件 ctrl shift X  然后定位到百度一下 找id 等
# 注意xpath获取的类型是列表类型 如果不想要[] 可以采用[0]
result = tree.xpath("//input[@id='su']/@value")[0]

print(result)
