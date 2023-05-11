# 目标一：了解什么是包
# 从物理.上看，包就是一个文件夹，在该文件夹下包含了一个__init__ .py 文件，该文件夹可用于包含多个模块文件
# 从逻辑.上看，包的本质依然是模块
# 如果包里面没有__init__.py 就是一个普通的文件夹 如果有的话就是一个python包

# 创建一个python包 点击项目右键  new pythonPackage 里面的__init__.py可以不写东西  但是不可以没有  并且 python包的图标和普通包的图表不一样 有一个点
# 方式一：
# import my_package.my_module1
# import my_package.my_module2
#
# my_package.my_module1.print_a()
# my_package.my_module2.print_b()

# 方式二：
# from  my_package import my_module1
# from  my_package import my_module2
# my_module1.print_a()
# my_module2.print_b()


# 目标二：如何自定义包
# 在__init__.py 中使用__all__控制 import*
# from my_package import *
#
# my_module1.print_a()
# my_module2.print_b()

# 目标三：安装第三方包
# 在cmd中输入pip install 包（这个访问的是国外的网速可能会慢可以使用清华的这边网址） eg # 使用国内的 -i https://pypi.tuna.tsinghua.edu.cn/simple 包
# （https://pypi.tuna.tsinghua.edu.cn/simple 清华大学弄的一个镜像网址）
# 或者在pycharm中下载 打开pycharm右下角 有个python3.6这个 找到 Interpreter Settings...
# 找到 Python Interpreter 右边的是存在的包 添加新的话 选择加号 在输入框中输入你要的包 可以点 Options 输入国内的那个站 加快下载速度
