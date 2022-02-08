import ipaddress

is_ip = ipaddress.IPv4Address("192.168.0.62") in ipaddress.IPv4Network("192.168.0.0/24")

print(is_ip)
