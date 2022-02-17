from http import server
from socket import AF_INET, SO_REUSEADDR, SOCK_STREAM, SOL_SOCKET, socket
from threading import Thread
from time import sleep

HOST = ""


PORT = 8050

server = socket(AF_INET, SOCK_STREAM)
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

server.bind((HOST, PORT))
print("Server bind success!")

connections = []
messages = []


def individual_send_message(connection):
    print(f"Sending messages to {connection['addr']}")
    for i in range(connection["last"], len(messages)):
        send_message = "msg=" + messages[i]
        connection["conn"].send(send_message.encode("utf-8"))
        connection["last"] = i + 1
        sleep(0.2)


def global_send_message():
    global connections
    for connection in connections:
        individual_send_message(connection)


def handle_client(conn, addr):
    print(f"New user connection by {addr} address")
    global connections
    global messages

    while True:
        msg = conn.recv(1024).decode()
        if msg:
            if msg.startswith("name="):
                splited_message = msg.split("=")
                name = splited_message[1]
                connection_map = {"conn": conn, "addr": addr, "name": name, "last": 0}
                connections.append(connection_map)
                individual_send_message(connection_map)
            elif msg.startswith("msg="):
                splited_message = msg.split("=")
                message = splited_message[1]
                messages.append(name + ":" + message)
                global_send_message()


def start():
    print("Server is now listen!")
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = Thread(target=handle_client, args=(conn, addr))
        thread.start()


start()
