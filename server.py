import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = "127.0.0.1"

serverPort = 5432

sock.bind((host, serverPort))

clientPort = 5433

noMessage = True

while noMessage:
    data, address = sock.recvfrom(1024)
    message = data.decode('UTF-8') + " - Don't eat the yellow snow."
    sock.sendto(message.encode('UTF-8'), (host, clientPort))
    noMessage = False