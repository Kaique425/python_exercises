import ipaddress
import re
import socket

host_name = socket.gethostbyaddr("192.168.0.62")
teste = socket.gethostbyname("HUBINTERN01")
print(host_name)


def write_host_info(name, ip):
    with open("Host_info.txt", "a") as file:
        text = f"Hostname: {name} IP: {ip} \n"
        print()
        file.write(text)
        file.close


host_info = socket.gethostbyaddr("192.168.0.62")


def clean_host(host_specs):
    text = [w for w in re.split(r"[unimed197.local]+", host_specs[0]) if w != " "]
    clean_text = text[0] + text[1]
    return clean_text


for ip in range(2, 254):
    is_ip = ipaddress.IPv4Address(f"192.168.0.{ip}") in ipaddress.IPv4Network(
        "192.168.0.0/24"
    )
    if is_ip:
        print(ip)
        host_info = socket.gethostbyaddr(f"192.168.0.{ip}")
        host_name = clean_host(host_info)
        host_ip = socket.gethostbyname(host_name)
        print(host_ip)
        write_host_info(host_name, host_ip)
