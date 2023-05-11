import urllib.request

# 注意哈 这里是有反扒的 所以我加了s 因为没解决
url = 'https://www.baidu.com/s?wd=ip'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}

proxies = {
    "http": "114.233.70.231:9000"
}

request = urllib.request.Request(url=url, headers=headers)

# 代理主要有 handler   build_opener  opener 这三个
handler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(handler)
response = opener.open(request)

content = response.read().decode("utf-8")

with open("daili.html", "w", encoding="utf-8") as fp:
    fp.write(content)


