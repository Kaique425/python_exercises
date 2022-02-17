<<<<<<< HEAD
from http import server
from socket import AF_INET, SO_REUSEADDR, SOCK_STREAM, SOL_SOCKET, socket
=======
from http import client, server
from socket import AF_INET, SOCK_STREAM, socket
>>>>>>> 53199833751f5809a2ebeb64f3541f7ff84259c3
from threading import Thread
from time import sleep

HOST = ""


PORT = 8050

server = socket(AF_INET, SOCK_STREAM)
<<<<<<< HEAD
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

server.bind((HOST, PORT))
print("Server bind success!")
=======

server.bind((HOST, PORT))
>>>>>>> 53199833751f5809a2ebeb64f3541f7ff84259c3

connections = []
messages = []

<<<<<<< HEAD
=======
server.listen(2)
>>>>>>> 53199833751f5809a2ebeb64f3541f7ff84259c3

def individual_send_message(connection):
    print(f"Sending messages to {connection['addr']}")
    for i in range(connection["last"], len(messages)):
        send_message = "msg=" + messages[i]
        connection["conn"].send(send_message.encode("utf-8"))
        connection["last"] = i + 1
        sleep(0.2)


<<<<<<< HEAD
def global_send_message():
    global connections
    for connection in connections:
        individual_send_message(connection)


def handle_client(conn, addr):
    print(f"New user connection by {addr} address")
    global connections
    global messages
=======
while True:
    client, ip_address = server.accept()
    print(f"Server connected by: {ip_address}")
>>>>>>> 53199833751f5809a2ebeb64f3541f7ff84259c3

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

<<<<<<< HEAD

def start():
    print("Server is now listen!")
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = Thread(target=handle_client, args=(conn, addr))
        thread.start()


start()
=======
        data = client.recv(1024)

        if not data:
            break
        input_msg = f"key pressed {data.decode()}"
        client.send(input_msg.encode("utf-8"))

    sleep(1)
    server.close()
    client.close()
>>>>>>> 53199833751f5809a2ebeb64f3541f7ff84259c3
