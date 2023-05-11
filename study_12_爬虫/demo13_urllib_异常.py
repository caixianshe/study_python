# try except
import urllib.request
import urllib.error

url = "http://goudanzhenshuai.com/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}

try:
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
    print(content)
except urllib.error.URLError:
    print("系统正在升级中.....")
except urllib.error.HTTPError:
    print("系统还在升级中.....")
