# import socket
from socket import socket

data =[
'Jan  3 13:45:36 192.168.5.1 id=firewall sn=000SERIAL time="2007-01-03 14:48:06" fw=1.1.1.1 pri=6 c=262144 m=98 msg="Connection Opened" n=23419 src=2.2.2.2:36701:WAN dst=1.1.1.1:50000:WAN proto=tcp/50000',
'Jan  3 13:45:36 192.168.5.1 id=firewall sn=000SERIAL time="2007-01-03 14:48:07" fw=1.1.1.1 pri=1 c=32 m=30 msg="Administrator login denied due to bad credentials" n=7 src=2.2.2.2:36701:WAN dst=1.1.1.1:50000:WAN',
'Jan  3 13:45:36 192.168.5.1 id=firewall sn=000SERIAL time="2007-01-03 14:48:07" fw=1.1.1.1 pri=6 c=262144 m=98 msg="Connection Opened" n=23420 src=2.2.2.2:36702:WAN dst=1.1.1.1:50000:WAN proto=tcp/50000',
'Jan  3 13:45:37 192.168.5.1 id=firewall sn=000SERIAL time="2007-01-03 14:48:07" fw=1.1.1.1 pri=6 c=1024 m=537 msg="Connection Closed" n=567996 src=192.168.4.10:27577:WAN dst=192.168.5.10:53:LAN proto=tcp/dns sent=257 rcvd=242',
'Jan  3 13:45:37 192.168.5.1 id=firewall sn=000SERIAL time="2007-01-03 14:48:08" fw=1.1.1.1 pri=6 c=1024 m=537 msg="Connection Closed" n=567997 src=192.168.5.56:4277:LAN dst=192.168.1.100:1026:WAN proto=tcp/1026 sent=3590 rcvd=13042 vpnpolicy="name"',
'Jan  3 13:45:39 192.168.5.1 id=firewall sn=000SERIAL time="2007-01-03 14:48:10" fw=1.1.1.1 pri=6 c=1024 m=537 msg="Connection Closed" n=567999 src=192.168.5.56:4280:LAN dst=192.168.2.81:41850:WAN proto=tcp/41850 sent=386026 rcvd=454118 vpnpolicy="name"',
'Jan  3 13:45:40 192.168.5.1 id=firewall sn=000SERIAL time="2007-01-03 14:48:10" fw=1.1.1.1 pri=6 c=262144 m=98 msg="Connection Opened" n=23421 src=2.2.2.2:36703:WAN dst=1.1.1.1:50000:WAN proto=tcp/50000',
'Jan  3 13:45:43 192.168.5.1 id=firewall sn=000SERIAL time="2007-01-03 14:48:14" fw=1.1.1.1 pri=6 c=1024 m=537 msg="Connection Closed" n=568000 src=219.89.19.223:1026:WAN dst=1.1.1.1:0:WAN proto=udp/0',
'Jan  3 13:45:44 192.168.5.1 id=firewall sn=000SERIAL time="2007-01-03 14:48:15" fw=1.1.1.1 pri=6 c=262144 m=98 msg="Connection Opened" n=23423 src=1.1.1.1:500:WAN dst=2.2.2.2:500:WAN proto=udp/500'
]

def main():
    server = "127.0.0.1"
    port = 514
    addr = (server, port)
    udpsend = socket(socket.AF_INET, socket.SOCK_DGRAM)
    for logs in data:
        udpsend.sendto(logs, addr)
    udpsend.close()


if __name__ == "__main__":
    main()
