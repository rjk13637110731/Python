from socket import *

IP = '0.0.0.0'

PORT = 50000

BUFLEN = 512

listenSocket = socket(AF_INET, SOCK_STREAM)

listenSocket.bind((IP, PORT))

listenSocket.listen(5)
print(f"服务端启动成功，在{PORT}端口等待用户端链接...")

dataSocket,addr = listenSocket.accept()
print("接受一个客户端连接：",addr)

while True:
    recved = dataSocket.recv(BUFLEN)

    if not recved:
        break
    info = recved.decode()
    print(f"收到对方消息：{info}")

    dataSocket.send(f"服务端收到信息：{info}".encode())

dataSocket.close()
listenSocket.close()
