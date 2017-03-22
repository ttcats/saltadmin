#!/usr/bin/env python
#-*- coding:utf-8 -*-
import re

def pool_dic():
  f = open("/tmp/op2.conf","r")
  con = f.read()
  f.close()

  s = re.findall("[\s|#]*upstream\s+\S+\s{\s+(?:[\s|#]*server.*;)+",con)
  upstream_lists=[]
  for i in s:
    if i.strip()[0] != "#":
      upstream_lists.append(i.strip())

  upsteam_dict = {}

  for upstream_list in upstream_lists:
    serv_list = upstream_list.split("\n")
    upstream_name = serv_list[0].split()[1]
    server_li = []
    for serv_ip in serv_list[1:]:
      Weight = re.findall("weight=\d+",serv_ip.strip())
      Max_fails = re.findall("max_fails=\d+",serv_ip.strip())
      Fail_timeout = re.findall("fail_timeout=\d+.",serv_ip.strip())
      if Weight == [] or Max_fails == [] or Fail_timeout == []:
        weight = []
        max_fails = []
        fail_timeout = []
      else:
        weight = Weight[0].split("=")[1]
        max_fails = Max_fails[0].split("=")[1]
        fail_timeout = Fail_timeout[0].split("=")[1]
      ip = serv_ip.split("server")[1].split()[0].split(":")[0]
      port = serv_ip.split("server")[1].split()[0].split(":")[1]
      if serv_ip.strip()[0] == "#":
        server_li.append({"ip":ip,"port":port,"status":"false","weight":weight,"max_fails":max_fails,"fail_timeout":fail_timeout})
      else:
        server_li.append({"ip":ip,"port":port,"status":"true","weight":weight,"max_fails":max_fails,"fail_timeout":fail_timeout})
    upsteam_dict[upstream_name] = server_li
  return upsteam_dict



