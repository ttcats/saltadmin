#!/usr/bin/env python

import MySQLdb


def Mysql(host,user,passwd,db,port,sql):
    try:
        conn = MySQLdb.connect(host=host,user=user,passwd=passwd,db=db,port=port)
        cur = conn.cursor()
        cur.execute(sql)
        data = cur.fetchall()
    except Exception, e:
        print e

if __name__ == "__main__":
    Mysql("127.0.0.1","","","sd",3306,"show databases;")


