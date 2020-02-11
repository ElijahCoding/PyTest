import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.sendto(b"Test message", ('localhost', 8886))