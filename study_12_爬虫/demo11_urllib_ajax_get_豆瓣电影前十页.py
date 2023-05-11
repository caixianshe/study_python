import urllib.request
import urllib.parse


def create_request(page):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
    }

    data = {
        "start": (page - 1) * 20,
        "limit": 20
    }

    # 转码进行参数拼接
    data = urllib.parse.urlencode(data)
    url = base_url + data

    request = urllib.request.Request(url=url, headers=headers)

    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
    return content


def down_load(content, page):
    with open("doubanq_" + str(page) + ".json", "w", encoding="utf-8") as fp:
        fp.write(content)


if __name__ == '__main__':
    start_page = int(input("开始页："))
    end_page = int(input("结束页:"))

    for page in range(start_page, end_page + 1):
        # 每一页都定制请求
        request = create_request(page)

        content = get_content(request)

        down_load(content, page)
