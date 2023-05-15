import urllib.request
import urllib.parse
from lxml import etree
import time


def create_request(page):
    if page == 1:
        base_url = 'http://sc.chinaz.com/tupian/qinglvtupian.html'
    else:
        base_url = 'https://sc.chinaz.com/tupian/qinglvtupian_' + str(page) + '.html'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
    }

    # 主要get请求需要拼接 post请求不需要
    # data = urllib.parse.urlencode(data).encode("utf-8")
    request = urllib.request.Request(url=base_url, headers=headers)

    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
    return content


def down_load(content):
    # 解析服务器响应的文件
    tree = etree.HTML(content)
    name_list = tree.xpath("//div[@class='container']//img/@alt")
    src_list = tree.xpath("//div[@class='container']//img/@data-original")

    for i in range(len(name_list)):
        name = name_list[i]
        url = 'https:' + src_list[i]

        # urllib.request.urlretrieve(url=url, filename="F:/workspace/study_python/study_12_爬虫/loveImg/" + name + '.jpg')
        urllib.request.urlretrieve(url=url, filename="./loveImg/" + name + '.jpg')


if __name__ == '__main__':
    start_page = int(input("开始页："))
    end_page = int(input("结束页:"))
    start = time.clock()

    for page in range(start_page, end_page + 1):
        # 每一页都定制请求
        request = create_request(page)

        content = get_content(request)
        # print(content)
        down_load(content)
    end = time.clock()
    print("final is in ", end - start)
# 7.143011868601275