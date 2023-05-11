# 导入相关库
import requests
from lxml import etree

# 定义请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.0.0",
    "Cookie": "RK=SGPEJs15WM; ptcz=505efb8980216747cc0775103c2117db83fb55c2cbe62b9b2dcf1d707be1ca77; pgv_pvid=8384677070; fqm_pvqid=95a2c6cb-c02a-4e28-b205-70af2093c76e; fqm_sessionid=d835b6fb-0ef3-420a-81cf-aa6fd4616098; pgv_info=ssid=s1276779116; ts_uid=9249408000; ts_last=y.qq.com/n/ryqq/player"
}

# 定义要爬取的歌手主页链接
singer_url = "https://y.qq.com/n/yqq/singer/0025NhlN2yWrP4.html"

# 发送请求获取响应
response = requests.get(singer_url, headers=headers)

# 解析响应内容为html对象
html = etree.HTML(response.text)

# 提取所有歌曲的songmid参数
songmids = html.xpath("//span[@class='songlist__songname_txt']/@data-songmid")

# 遍历每个songmid参数
for songmid in songmids:
    # 拼接出歌曲播放页的链接
    song_url = f"https://y.qq.com/n/yqq/song/{songmid}.html"
    # 发送请求获取响应
    response = requests.get(song_url, headers=headers)
    # 解析响应内容为html对象
    html = etree.HTML(response.text)
    # 提取音频地址和其他信息
    audio_url = html.xpath("//a[@id='h5audio_media']/@src")[0]
    song_name = html.xpath("//h1[@class='data__name_txt']/text()")[0]
    album_name = html.xpath("//a[@class='data__album_txt']/text()")[0]
    duration = html.xpath("//span[@class='data__time_txt']/text()")[0]

    # 打印或保存数据
    print(f"歌名：{song_name}")
    print(f"专辑：{album_name}")
    print(f"时长：{duration}")
    print(f"音频地址：{audio_url}")
