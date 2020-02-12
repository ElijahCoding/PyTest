import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

socket.bind(('127.0.0.1', 8886))

while True:
    try:
        result = socket.recv(1024)
    except KeyboardInterrupt:
        socket.close()
        break
    else:
        print('Message', result.decode('utf-8'))


