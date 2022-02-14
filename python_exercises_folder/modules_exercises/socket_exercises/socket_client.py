from re import T
from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread

HOST = "127.0.1.1"


PORT = 8050

client = socket(AF_INET, SOCK_STREAM)

client.connect((HOST, PORT))


def handle_messages():
    while True:
        msg = client.recv(1024).decode()
        splited_message = msg.split("=")
        print(splited_message[0] + ":" + splited_message[1])


def send(message):
    client.send(message.encode("utf-8"))


def send_name():
    name = input("Type your name: ")
    send("name=" + name)


def send_message():
    message = input()
    send("msg=" + message)


def start_sending():
    send_name()
    send_message()


def start():
    th1 = Thread(target=handle_messages)
    th2 = Thread(target=start_sending)
    th1.start()
    th2.start()


start()
