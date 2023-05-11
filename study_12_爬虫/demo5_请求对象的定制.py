# 请求对象的定制 就是应对反扒的手段

# ua 反扒 就是 User-Agent 东西 在网页的network->headers中找

import urllib.request

# Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36


url = 'http://www.baidu.com'

# 下面两个就是请求对象的定制
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}
request = urllib.request.Request(url=url, headers=headers)


response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)
