import mysql.connector

usr = "root"
pwd = "mysql"
mysqlhost = "127.0.0.1"
sql = mysql.connector.connect(host=mysqlhost, user=usr, password=pwd)
exe = sql.cursor()
sql.autocommit = True


def isserver(ipaddr):
    getsrv = 'SELECT SQL_NO_CACHE * FROM syslog_server.server WHERE ip = "{}"'.format(ipaddr)
    exe.execute(getsrv)
    server = exe.fetchall()
    if len(server) > 0:
        return server[0][5]
    else:
        return 0


def isswitch(ipaddr):
    getsrv = 'SELECT SQL_NO_CACHE * FROM syslog_server.server WHERE ip = "{}"'.format(ipaddr)
    exe.execute(getsrv)
    server = exe.fetchall()
    if len(server) > 0:
        return server[0][4]
    else:
        return 0


def isfirewall(ipaddr):
    getsrv = 'SELECT SQL_NO_CACHE * FROM syslog_server.server WHERE ip = "{}"'.format(ipaddr)
    exe.execute(getsrv)
    server = exe.fetchall()
    if len(server) > 0:
        return server[0][3]
    else:
        addserversql = 'INSERT INTO syslog_server.server (name, ip) VALUES ("{}", "{}")'.format(ipaddr, ipaddr)
        exe.execute(addserversql)
