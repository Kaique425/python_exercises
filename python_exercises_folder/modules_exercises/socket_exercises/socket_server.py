from http import client, server
from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread
from time import sleep

HOST = ""


PORT = 8050

server = socket(AF_INET, SOCK_STREAM)

server.bind((HOST, PORT))

print("Socket bind success!")

server.listen(2)

print("Server is now listen!")


while True:
    client, ip_address = server.accept()
    print(f"Server connected by: {ip_address}")

    while True:

        data = client.recv(1024)

        if not data:
            break
        input_msg = f"key pressed {data.decode()}"
        client.send(input_msg.encode("utf-8"))

    sleep(1)
    server.close()
    client.close()
