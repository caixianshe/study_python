import urllib.request
import urllib.parse

# handler作用   urlopen()不能定制请求头   Request()可以定制请求头
# 而handler作用是可以定制更高级的请求头(随着我们的业务逻辑的复杂 请求定制已经不能满足我们的需求（动态cookie和代理不能使用请求对象的定制）)
# 代理就是 假如一群人去爬一个网站把你们的ip给封掉了  此时可以使用代理去访问这个网站


# 需求使用handler来访问百度 获取网页源码
url = 'http://www.baidu.com'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}

request = urllib.request.Request(url=url, headers=headers)
# handler 主要有 handler   build_opener  opener 这三个

# (1)获取handler
handler = urllib.request.HTTPHandler()

# (2)获取opener对象
opener = urllib.request.build_opener(handler)
# (3)调用open方法
response = opener.open(request)

content = response.read().decode("utf-8")

print(content)
