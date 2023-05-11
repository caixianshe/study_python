from lxml import etree

# xpath解析
# (1)本地文件                                     ----     etree.parse
# (2) 服务器响应的数据response.read().decode('utf-8')----    etree.HTML( )

# xpath解析本地文件
tree = etree.parse("demo18_xpath的基本使用.html")

#学习目标一： 查找ul下的li
# li_list = tree.xpath("//body/ul/li")
# 可以使用//
li_list = tree.xpath("//li")

print(li_list)
print(len(li_list))

# xpath基本语法:
# 1.路径查询
# //:查找所有子孙节点，不考虑层级关系
# / :找直接子节点

# 2.谓词查询
# //div[@id]
# //div[@id="maincontent"]

# 3.属性查询
# //@class

# 4.模糊查询
# //div[contains(@id, "he" )]
# //div[starts-with(@id, "he")]

# 5.内容查询
# //div/h1/text()

# 6.逻辑运算
# //div[@id="head" and @class="s_down" ]
# //title | //price
