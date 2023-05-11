# 以下是socket 服务端开发

# socket(简称套接字)是进程之间通信一个工具,好比现实生活中的插座,所有的家用电器要想工作都是基于插座进行，
# 进程之间想要进行网络通信需要socket。
# Socket负责进程之间的网络数据传输，好比数据的搬运工。大多软件都用到了socket 比如qq 微信 谷歌都有用到 socket通信

# 2个进程之间通过Socket进行相互通讯,就必须有服务端和客户端
# Socket服务端等待其它进程的连接、可接受发来的消息、可以回复消息
# Socket客户端:生动连接服务端、可以发送消息、可以接收回复.

# 注意我们是服务端
import socket

# 1.创建socket对象
# 此时socket对象还没有区分是服务端还是客户端
socket_server = socket.socket()

# 2.绑定socket对象到指定的ip和地址
socket_server.bind(("localhost", 8888))

# 3.服务端开始监听端口
socket_server.listen(1)
# backlog为int整数，表示允许的连接致量，超出的会等待，可以不填，不填会目动设置一个合理值

# 4.接收客户端连接，获取连接对象
# result = socket_server.accept()  #accept方法返回的是二元元组
socket_server.accept()

# con = result[0]  # 客户端和服务端连接的对象
# address = result[1]  # 客户端的地址信息
# 简写
conn, address = socket_server.accept()
# 前面是con是连接 address是内容
print(f"接收到的客户端连接，连接来自：{address}")
# # accept方法是阻塞方法， 如果没有连接，会卡再当前这一行不向下执行代码
# # accept返回的是一个二元元组，可以使用上述形式，用两个变量接收二元元组的2个元素

# 5.客户端连接之后，通过recv方法接收客户端发送的消息
while True:
    # recv方法的返回值是字节数组(Bytes)，可以通过decode使用UTF-8解码为字符串 此时data就是字符串类型
    # recv方法的传参是buffsize,缓冲区大小，一般设置为1024即可
    # recv不是采用socket_server对象了 而是采用 客户端和服务端连接的这个对象conn
    data = conn.recv(1024).decode(encoding="UTF-8")

    print(f"接收到的消息为：{data}")

    msg = input("服务端发送的消息是：")
    # 注意 这里的退出是服务端的
    if msg == 'exit':
        break

    # 6.通过conn (客户端当次连接对象),调用send方法可以回复消息
    conn.send(msg.encode("UTF-8"))


# 7. conn (客户端当次连接对象)和socket_server对象调用close方法,关闭连接
conn.close()
