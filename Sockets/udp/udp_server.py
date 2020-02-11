import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

socket.bind(('127.0.0.1', 8886))

result = socket.recv(1024)
print('Message: ', result.decode('utf-8'))
socket.close()