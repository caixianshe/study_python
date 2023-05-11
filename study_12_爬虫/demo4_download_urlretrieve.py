# 下载图片 音乐等
import urllib.request

# url_page = 'https://www.huaxiashuyu.com'

# # 下载网页
# urllib.request.urlretrieve(url_page, "huaxiashuyu.html")

# 下载图片
# url_image = 'https://img0.baidu.com/it/u=2874790938,228875074&fm=253&fmt=auto&app=120&f=JPEG?w=800&h=1149'
# urllib.request.urlretrieve(url_image, "meinv.jpg")

url_video = "https://vd2.bdstatic.com/mda-pdpdq1uuede4jwvc/sc/cae_h264/1682333782171296272/mda-pdpdq1uuede4jwvc.mp4?v_from_s=hkapp-haokan-nanjing&auth_key=1682587708-0-0-66d161dc60eaaf1f279aade34579bbf6&bcevod_channel=searchbox_feed&pd=1&cd=0&pt=3&logid=3508455732&vid=8170936236631453019&abtest=109159_2&klogid=3508455732"
urllib.request.urlretrieve(url_video, "shiping.mp4")
