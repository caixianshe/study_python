# 百度翻译
import urllib.request
import urllib.parse

url = "https://fanyi.baidu.com/sug"

data = {
    "kw": "happy"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}

# post请求的参数必须要进行编码
data = urllib.parse.urlencode(data).encode("utf-8")

request = urllib.request.Request(url, data, headers)
response = urllib.request.urlopen(request)

# decode是解码  encode编码
connect = response.read().decode("utf-8")

import json

loads = json.loads(connect)

print(loads)
