# 最早期冯诺依曼电脑采用的是ascii编码 有大小写英文字母 数字以及一些字符
# 这个编码表被称为ASCII编码，比如大写字母A的编码是65，小写字母z的编码是122。
# 但是要处理中文显然一个字节是不够的， 至少需要两个字节，而且还不能和ASCII编码冲突，
# 所以，中国制定了GB2312编码，用来把中文编进去。
# 你可以想得到的是，全世界有上百种语言，日本把日文编到Shift_ JIS里， 韩国把韩文编到Euc-kr里，
# 各国有各国的标准，就会不可避免地出现冲突，结果就是，在多语言混合的文本中，显示出来会有乱码。
# 因此，Unicode应运而生。Unicode把所有语言都统一到套编码里，这样就不会再有乱码问题了。
# Unicode标准也在不断发展，但最常用的是用两个字节表示一个字符(如果要用到非常偏僻的字符，就需要4个
# 字节)。
# 现代操作系统和大多数编程语言都直接支持Unicode。

import urllib.request
import urllib.parse

# 周杰伦在网页中是字符串 而在代码里面采用的是Unicode编码
# 采用parse中的quote方法 把字符串转换为unicode编码
url = "https://www.baidu.com/s?wd="
name = urllib.parse.quote("周杰伦")
url = url + name

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)
connect = response.read().decode("utf-8")
print(connect)
