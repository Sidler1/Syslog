import datetime
import socket

import mysql.connector

import parsersyslog
import server_check

host = ""  # Localhost
port = 514  # Standart Syslog Port
bufsize = 32 * 1024  # 32 kByte
fwaddr = "192.168.5.1"
addr = (host, port)

usr = "root"
pwd = "mysql"
mysqlhost = "127.0.0.1"
sql = mysql.connector.connect(host=mysqlhost, user=usr, password=pwd)
exe = sql.cursor()


def listener():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(addr)
    while True:
        rec = sock.recvfrom(bufsize)
        msg = rec[0]
        msg = str(msg)
        f = open("{}.log".format(datetime.date), "a+")
        f.write(msg)
        f.close()
        msg = msg.replace('"', '')
        ipfrom = rec[1][0]
        if ipfrom == fwaddr or ipfrom.split(".")[3] == fwaddr.split(".")[3] or server_check.isfirewall(ipfrom):
            fwmsg = parsersyslog.ParserFirewall(msg)
            data = fwmsg.pars()
            addmsg = ("INSERT INTO syslog_server.syslog_fw"
                      "(ip, prio, msg, from_ip, to_ip) "
                      'VALUES ("{}", {}, {}, "{}", "{}")'.format(data['id'], data['pri'], data['msg'], data['src'],
                                                                 data['dst']))
            exe.execute(addmsg)
            sql.commit()
        elif server_check.isserver(ipfrom):
            linuxmsg = parsersyslog.ParserLinux(str(msg))
            data = linuxmsg.pars()
            if data == None:
                pass
            else:
                addmsg = ("INSERT INTO syslog_server.syslog_srv"
                          "(client_ip, msg, prio, service) "
                          'VALUES ("{}", "{}", "{}", "{}")'.format(ipfrom, data['msg'], data['pri'], data['trigger']))
                exe.execute(addmsg)
                sql.commit()
        elif server_check.isswitch(ipfrom):
            sysmsg = parsersyslog.ParserSwitch(msg)
            data = sysmsg.pars()
            addmsg = ("INSERT INTO syslog_server.syslog_switch"
                      "(from_ip, msg, prio) "
                      'VALUES ("{}", "{}", "{}")'.format(ipfrom, data['msg'].replace('"', ""), data['pri']))
            exe.execute(addmsg)
            sql.commit()


def main():
    listener()


if __name__ == "__main__":
    main()
