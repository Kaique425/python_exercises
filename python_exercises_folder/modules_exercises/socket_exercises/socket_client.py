from http import client
from socket import AF_INET, SOCK_STREAM, socket

HOST = "127.0.1.1"


PORT = 8050

client = socket(AF_INET, SOCK_STREAM)

client.connect((HOST, PORT))

while True:
    msg = input("msg=")
    client.send(msg.encode("utf-8"))

    data = client.recv(1024)
    print(f"Server disse: {data.decode()}")
