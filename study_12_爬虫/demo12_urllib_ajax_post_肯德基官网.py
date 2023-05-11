#

# 在 network -> Request Headers ->  X-Requested-With: XMLHttpRequest   ->   证明是ajax请求

import urllib.request
import urllib.parse


def create_request(page):
    base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
    }

    data = {
        "cname": "宁波",
        "pid": "",
        "pageIndex": page,
        "pageSize": "10"
    }

    # post请求必须编码多一个这个  .encode("utf-8")
    # 主要get请求需要拼接 post请求不需要
    data = urllib.parse.urlencode(data).encode("utf-8")

    request = urllib.request.Request(url=base_url, headers=headers, data=data)

    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
    return content


def down_load(content, page):
    with open("kfc_" + str(page) + ".json", "w", encoding="utf-8") as fp:
        fp.write(content)


if __name__ == '__main__':
    start_page = int(input("开始页："))
    end_page = int(input("结束页:"))

    for page in range(start_page, end_page + 1):
        # 每一页都定制请求
        request = create_request(page)

        content = get_content(request)

        down_load(content, page)
