#!/usr/bin/env python
#-*- coding:utf-8 -*-
import re

def Action_ng(ip,port,status):
  f = open("/tmp/op2.conf","r")
  s = f.read()
  f.close()
  a = open("/tmp/op2.conf","w+")
  if status == "true":
    patt = ".*server\s+%s:%s" %(ip,port)
    patt_down = "\t\t#server %s:%s" %(ip,port)
    value = "down_true"
  else:
    patt = ".*server\s+%s:%s" %(ip,port)
    patt_down = "\t\tserver %s:%s" %(ip,port)
    value = "up_true"
  g = re.sub(patt,patt_down,s)
  #print g,"----------------------------"
  a.write(g)
  a.close()
  return value

