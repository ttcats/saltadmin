#!/usr/bin/env python

import psycopg2



def postgre(host,port,user,passwd,db,sql):
  try:
    conn = psycopg2.connect(dbname=db,user=user,password=passwd,host=host,port=port)
    con = conn.cursor()
    con.execute(sql)
    #print con.fetchall()
    return con.fetchall()
    conn.close()
  except Exception, e:
    #print e
    return e


if __name__ == "__main__":
  sql = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';"
  postgre("localhost","5432","postgres","123456","test2",sql)


