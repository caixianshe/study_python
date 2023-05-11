import urllib.request
import random

# 注意哈 这里是有反扒的 所以我加了s 因为没解决
url = 'https://www.baidu.com/s?wd=ip'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}

proxies_pool = [
    {"http": "210.5.10.87:53281"},
    {"http": "210.5.10.87:53281"}
]

proxies = random.choice(proxies_pool)
# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

handler = urllib.request.ProxyHandler(proxies=proxies)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

content = response.read().decode("utf-8")

with open("dailichi.html", "w", encoding="utf-8") as fp:
    fp.write(content)
