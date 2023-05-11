# 客户端
import socket

socket_client = socket.socket()

socket_client.connect(("localhost", 8888))

while True:
    msg = input("客户端发送的消息是：")

    if msg == 'exit':
        break

    socket_client.send(msg.encode("UTF-8"))

    data = socket_client.recv(1024)

    print(f"服务端回复的消息是：{data.decode('UTF-8')}")

socket_client.close()

# 总结 客户端和服务端之间的差别
# 客户端是connect 连接 而服务端是 bind 绑定 加listen 监听 所以主动的是客户端  被动的是服务端....
# 客户端是先发送send  再接收recv  而服务端是 先接受  在发送
# 客户端连接对象是socket_client 而服务端是conn 因为服务端可能连接的不止一个对象


