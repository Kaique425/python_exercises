from socket import AF_INET, SOCK_STREAM, socket

HOST = "127.0.1.1"


PORT = 8050

socket_obj = socket(AF_INET, SOCK_STREAM)

socket_obj.connect((HOST, PORT))

messages = [b"test message"]

for msg in messages:

    socket_obj.send(msg)

    data = socket_obj.recv(1024)
    print(f"Cliente recebeu {data}")
