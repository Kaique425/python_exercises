import nmap


class Network:
    def __init__(self, ip):
        self.ip = ip

    def networkscanner(self):

        network = "192.168.1.1/24"

        nm = nmap.PortScanner()
        nm.scan(hosts=network, arguments="-sn")
        host_list = [(x, nm[x]["status"]["state"]) for x in nm.all_hosts()]
        for host, status in host_list:
            print(f"host: {host} state {status}")


if __name__ == "__main__":
    D = Network("192.168.1.1/24")
    D.networkscanner()
