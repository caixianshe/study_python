import urllib.request

url = "https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}

# 1/请求定制
request = urllib.request.Request(url=url, headers=headers)
# 2/获取响应数据
response = urllib.request.urlopen(request)
content = response.read().decode("utf-8")

# (3)数据下载到本地
# open方法默认情况下使用的是gbk的编码如果 我们要想保存汉字那么需要在open方法中指定编码格式为utf-8
# fp = open("douban.json", "w", encoding="utf-8")
# fp.write(content)

# 上面两句haul可以换一种写法 一样的   下面这个自带 fp.close()
with open("douban.json", "w", encoding="utf-8") as fp:
    fp.write(content)


# print(content)
