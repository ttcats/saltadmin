#!/usr/bin/env python
#-*- coding:utf-8 -*-

import MySQLdb


def Mysql(host,user,passwd,db,port,sql):
    try:
        #print user,passwd
        conn = MySQLdb.connect(host=host,user=user,passwd=passwd,db=db,port=port,charset='utf8')
        #conn = MySQLdb.connect(host=host,user=user,passwd=passwd,db=db,port=port)
        cur = conn.cursor()
        cur.execute(sql)
        data = cur.fetchall()
        for i in data:
            print i[0]
        print data
        #return data
    except Exception, e:
        print e,"ds"
        return e
        #return "Mysql ERROR"    

if __name__ == "__main__":
    Mysql("127.0.0.1","","","saltadmin",3306,"select comment from options limit 1")
    #Mysql("127.0.0.1","","","saltadmin",3306,"select * from options limit 10")


