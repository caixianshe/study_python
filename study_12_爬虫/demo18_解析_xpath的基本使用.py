from lxml import etree

# xpath解析
# (1)本地文件                                     ----     etree.parse
# (2) 服务器响应的数据response.read().decode('utf-8')----    etree.HTML( )

# xpath解析本地文件
tree = etree.parse("demo18_xpath的基本使用.html")

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
# //div[contains(@id, "he" )]    ----包含
# //div[starts-with(@id, "he")]       ----以...什么开头

# 5.内容查询
# //div/h1/text()

# 6.逻辑运算
# //div[@id="head" and @class="s_down" ]
# //title | //price

# ====学习目标一： 查找ul下的li   //body 这个层级可以改为//ul是没问题的  主要参考  1.路径查询
# li_list = tree.xpath("//body/ul/li")
# 可以使用//
# li_list = tree.xpath("//li")
#
# print(li_list)
# print(len(li_list))

# ====学习目标二：查找所有id的属性的li标签  注意 text()是获取标签中的内容
# li_list = tree.xpath("//body/ul/li[@id]/text()")
#
# print(li_list)
# print(len(li_list))

# ====学习目标三：查找id为l1的li标签 注意l1是字符串 在引号里面写字符串必须使用引号 外双内单  注意引号的问题
# li_list = tree.xpath("//body/ul/li[@id='l1']/text()")
#
# print(li_list)
# print(len(li_list))

# ====学习目标四：查找到id为l1的li标签的class的属性值
# li_list = tree.xpath("//body/ul/li[@id='l1']/@class")
#
# print(li_list)
# print(len(li_list))

# ====学习目标五：查找到id带l的li标签(采用模糊查询)
# li_list = tree.xpath("//body/ul/li[contains(@id,'c')]/text()")
#
# print(li_list)
# print(len(li_list))

# ====学习目标六：查找到id以l开头的li标签
# li_list = tree.xpath("//body/ul/li[starts-with(@id,'c')]/text()")
#
# print(li_list)
# print(len(li_list))

# ====学习目标七：查询id为l1和class为c1的
# li_list = tree.xpath("//body/ul/li[@id='l1'and@class='c1']/text()")
#
# print(li_list)
# print(len(li_list))

# ====学习目标七：查询id为l1 或id为c3的
# li_list = tree.xpath("//body/ul/li[@id='l1' | @id='c3']/text()")  注意是不支持在里面写的
li_list = tree.xpath("//ul/li[@id='l1']/text() | //ul/li[@id='c3']/text()")

print(li_list)
print(len(li_list))
