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
pwd = "mysql"
database = "syslog_server"
mysqlhost = "127.0.0.1"
sql = mysql.connector.connect(host=mysqlhost, user=usr, password=pwd, database=database)
exe = sql.cursor()

def listener():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(addr)
    while True:
        rec = sock.recvfrom(bufsize)
        msg = rec[0]
        msg = str(msg)
        msg = msg.replace('"','')
        ipfrom = rec[1][0]
        if ipfrom == fwaddr or ipfrom.split(".")[3] == fwaddr.split(".")[3]:
            fwmsg = parsersyslog.ParserFirewall(msg)
            data = fwmsg.pars()
            addmsg = ("INSERT INTO syslog_fw"
                      "(ip, prio, msg, from_ip, to_ip) "
                      'VALUES ("{}", {}, {}, "{}", "{}")'.format(data['id'], data['pri'], data['msg'], data['src'], data['dst']))
            exe.execute(addmsg)
            sql.commit()
        elif ipfrom == "172.20.4.78":
            linuxmsg = parsersyslog.ParserLinux(str(msg))
            data = linuxmsg.pars()
            if data == None:
                pass
            else:
                addmsg = ("INSERT INTO syslog_srv"
                "(client_ip, msg, prio, service) "
                'VALUES ("{}", "{}", "{}", "{}")'.format(ipfrom, data['msg'], data['pri'], data['trigger']))
                print(addmsg)
                exe.execute(addmsg)
                sql.commit()
        else:
            sysmsg = parsersyslog.ParserSwitch(msg)
            data = sysmsg.pars()
            addmsg = ("INSERT INTO syslog_switch"
                      "(from_ip, msg, prio) "
                      'VALUES ("{}", "{}", "{}")'.format(ipfrom, data['msg'].replace('"',""), data['pri']))
            print(addmsg)
            exe.execute(addmsg)
            sql.commit()
    sock.close()


def main():
    listener()


if __name__ == "__main__":
    main()
