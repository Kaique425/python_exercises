from socket import AF_INET, SOCK_STREAM, socket
from time import sleep

HOST = ""


PORT = 8050

socket_obj = socket(AF_INET, SOCK_STREAM)

socket_obj.bind((HOST, PORT))

print("Socket bind success!")

socket_obj.listen(2)

print("Server is now listen!")

while True:

    connection, ip_address = socket_obj.accept()
    print(connection)
    print(f"Server connected by: {ip_address}")

    while True:

        data = connection.recv(1024)

        if not data:
            break

        connection.send(b"msg: " + data)

    sleep(1)
    connection.close()
