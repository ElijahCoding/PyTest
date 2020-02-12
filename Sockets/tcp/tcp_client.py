import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(('', 8882))
socket.send(b'test message')
socket.close()