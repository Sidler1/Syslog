import socket


def main():
    server = "127.0.0.1"
    port = 514
    addr = (server, port)
    data = 'id=firewall sn=00XX time="2005-10-22 00:12:11" fw=1.2.3.4 pri=5 c=128 m=37 msg="UDP packet dropped" n=14333 src=1.3.4.5 dst=2.5.6.7:1025:LAN'
    udpsend = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udpsend.sendto(data, addr)
    udpsend.close()


if __name__ == "__main__":
    main()
