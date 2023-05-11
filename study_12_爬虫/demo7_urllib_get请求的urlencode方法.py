import urllib.request
import urllib.parse

base_url = 'https://www.baidu.com/s?'

data = {
    "wd": "周杰伦",
    "sex": "男",
    "location": "中国台湾省"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}

a = urllib.parse.urlencode(data)
# print(a)

url = base_url + a
# print(url)

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

connect = response.read().decode("utf-8")
print(connect)
