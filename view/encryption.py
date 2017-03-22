#!/usr/bin/env python
#-*- coding:utf-8 -*-

from main import *
import hashlib

import sys
reload(sys)
sys.setdefaultencoding('utf8')

class Index:
    def GET(self):
        if getLogin():
            SID = getLogin()['SID']
            ShowName = getLogin()['ShowName']
            #print "ShowName: " + ShowName       
            return render.encryption(ShowName=ShowName,uid=SID)
        else:
            return web.seeother("/login")


    def POST(self):
        if getLogin() is False:
            web.ctx.status = '401 Unauthorized'
            return '401 - Unauthorized\n'
        update = web.input()
        Cont = update['content']
        Num = update['num']
        Seed = update['seed']
        if Cont == '' or Seed == '':
            return "请输入内容."
        else:
            encry_con = str(Cont) + str(Seed) + str(Num) + "Hello World"
            Md5 = hashlib.md5()
            Md5.update(encry_con)
            Md5_con = Md5.hexdigest()
            if list(Md5_con)[int(Num)].isdigit():
                Md5_con_1 = int(Num)**2/16
            else:
                Md5_con_1 = int(Num)**2/12
            Md5_con_2 = int(Md5_con_1) + int(Num)
            Md5_con_3 = list(Md5_con)[int(Md5_con_1):int(Md5_con_2)] 
            for r in Md5_con_3[2:7]:
                Md5_con_3.append(r.upper())
            Md5_con_4 = Md5_con_3[5:]
            Md5_con_end = ''.join(Md5_con_4)
            #print Md5_con_1,Md5_con_2,Md5_con_3,Md5_con_4,
            return Md5_con_end
