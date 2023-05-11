import urllib.request

url = 'https://www.huaxiashuyu.com'
response = urllib.request.urlopen(url)
content = response.read().decode('utf-8')

# print(response.getcode())
# print(response.geturl())

# print(content)

# 一个类型 六个方法  HttpResponse
# read readline readlines
# getcode-- 返回的是状态码
# geturl-- 获取的是请求地址
# gettheads  --获取的是状态信息
