# 适用场景 数据采集的时候 需要绕过登录 然后登录到某个页面

# 视屏做的是微博的 但是微博现在改了 所以我做个QQ空间的
import urllib.request
import urllib.error

url = "http://user.qzone.qq.com/948342540"

headers = {
    # referer有时候验证 有时候不验证 这个和cookie都要加上
    "referer": "https://i.qq.com/?s_url=http%3A%2F%2Fuser.qzone.qq.com%2F948342540",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
    # 市面上百分之六七十的问题都可以使用cookie解决 后面也会使用动态cookie解决另一个问题
    "cookie": "RK=SGPEJs15WM; ptcz=91cc3aab1892a8c156c3fe3efbea4a7b17813b5db709790969dc61578d416448; logTrackKey=74a21deb79974ea2b6d43621a3f1a0b8; pgv_pvid=9597902640; eas_sid=d176t8h1i208F418B3s8J0Q3F2; LW_sid=7116b891w2U8V4S8X4A8r1P344; LW_uid=U1R6R8N1D2s8w4F8k4Y861Z3f5; fqm_pvqid=b173d347-b814-4450-93a4-9ef708be12de; pac_uid=0_9ca4bedd8dd2c; _qpsvr_localtk=0.02307631449020997; pgv_info=ssid=s1618362600; uin=o0948342540; skey=@iZqQOilzZ; p_uin=o0948342540; pt4_token=NF1LiPTHiKvDE-oY-Qq6ikWuqQHzUzL3BOsCTt8rbSM_; p_skey=ftZhEcfvTyFttFN600uFvERiAZ*6XBFMOj*szkkUTCo_; Loading=Yes; qz_screen=1920x1080; QZ_FE_WEBP_SUPPORT=1; cpu_performance_v8=11"
}

request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
# 如果页面不是utf-8的那么要在这里也该编码下面的编码也要改
content = response.read().decode("utf-8")

with open("QQkongjian.html", "w", encoding="utf-8") as fp:
    fp.write(content)
