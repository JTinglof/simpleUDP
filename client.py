import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

host = "127.0.0.1"

serverPort = 5432

clientPort = 5433

sock.bind((host, clientPort))

sock.sendto(("Hello").encode('UTF-8'), (host, serverPort))

data, address = sock.recvfrom(1024)

print(data.decode('UTF-8'))