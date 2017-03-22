#!/usr/bin/env python
#-*- coding: utf-8 -*-

import MySQLdb
import psycopg2
import ConfigParser


import sys
reload(sys)
sys.setdefaultencoding('utf-8')



class dbconnet:
    def __init__(self,host,user,passwd,db,port,sql):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.port = port
        self.sql = sql

    def mysql(self):
        #print self.host,self.user,self.passwd,self.db,self.port,self.sql,
        try:
            conn = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db,port=self.port,charset='utf8')
            #conn = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db,port=self.port,use_unicode=0, charset='gb2312')
            #print "s",conn
            cur = conn.cursor()
            #cur.execute("set names utf8")
            cur.execute(self.sql)
            data = cur.fetchall()
            #for i in data:
            #    print i
            #print data,"data"
            return data
            conn.close()
        except Exception, e:
            return "ErroR",e

    def pgsql(self):
        try:
            conn = psycopg2.connect(dbname=self.db,user=self.user,password=self.passwd,host=self.host,port=self.port)
            con = conn.cursor()
            con.execute(self.sql)
            return con.fetchall()
            conn.close()
        except Exception, e:
            return e


#s = dbconnet("127.0.0.1","","","",3306,"show databases;")
#s.mysql()

def env(ip,port,db,sql):
    conf = ConfigParser.ConfigParser()
    conf.read("/tmp/saltdmin-master/SaltAdmin/view/db_config.cfg")
    Connet = ip + "_" + str(port)
    #print type(port)
    #print type(Connet),"connet"
    #print conf.sections
    user =  conf.get(Connet,"username")
    passwd = conf.get(Connet,"passwd")
    #print user, passwd
    s = dbconnet(ip,"","",db,port,sql)
    v = s.mysql()
    print "cd",v
    return v 
    

if __name__ == "__main__":
    env("127.0.0.1",3306,"db","sql")
