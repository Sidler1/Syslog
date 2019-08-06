import socket
import parsersyslog
import mysql.connector
import datetime

host = ""  # Localhost
port = 514  # Standart Syslog Port
bufsize = 32 * 1024  # 32 kByte
fwaddr = "192.168.5.1"
addr = (host, port)

usr = "root"
pwd = "!!PASSWORD!!"
database = "syslog_server"
mysqlhost = "localhost"
sql = mysql.connector.connect(host=mysqlhost, user=usr, password=pwd, database=database)
exe = sql.cursor()


def listener():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(addr)
    while True:
        rec = sock.recvfrom(bufsize)
        msg = rec[0]
        ipfrom = rec[1][0]
        if ipfrom == fwaddr or ipfrom.split(".")[3] == fwaddr.split(".")[3]:
            fwmsg = parsersyslog.ParserFirewall(msg)
            data = fwmsg.pars()
            addmsg = ("INSERT INTO syslog_fw"
                      "(ip, prio, msg, from_ip, to_ip) "
                      'VALUES ("{}", {}, {}, "{}", "{}")'.format(data['id'], data['pri'], data['msg'], data['src'], data['dst']))
            exe.execute(addmsg)
            sql.commit()
        else:
            print(msg)
    sock.close()


def main():
    listener()


if __name__ == "__main__":
    main()
