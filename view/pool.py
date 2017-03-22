#!/usr/bin/env python
#-*- coding:utf-8 -*-
from main import *
import os
from renginx import pool_dic
from action_ng import Action_ng

import sys
reload(sys)
sys.setdefaultencoding('utf8')


# 选项管理
class Pool:
    def GET(self):
        if getLogin():
            sData = getLogin()
            SID = sData['SID']
            ShowName = sData['ShowName']
            ng_pool = pool_dic()
            pool_names = ng_pool.keys()
            numb_pool = {}
            for key in pool_names:
                num_ip = {}
                n = 0
                for st in ng_pool[key]:
                    if st["status"] == "true":
                      n += 1
                num_ip_total = len(ng_pool[key])
                num_ip["up"] = n
                num_ip["total"] = num_ip_total
                numb_pool[key]=num_ip
            print numb_pool
            return render.pool(ShowName=ShowName,uid=SID,numb_pool=numb_pool)
        else:
            web.setcookie('HTTP_REFERER', web.ctx.fullpath, 86400)
            return web.seeother("/login")

    def POST(self):
        if getLogin() is False:
            web.ctx.status = '401 Unauthorized'
            return '401 - Unauthorized\n'
        ng_pool = pool_dic()
        update = web.input()
        #print update,ng_pool
        n = 0
        Value = ng_pool[update["nodeview"]]
        #print Value
        for i in Value:
            if i["status"] == "true":
                n += 1
        st = str(n) + "/" + str(len(Value))
        print st
        return st



class Pool_node:
    def POST(self):
        if getLogin():
            sData = getLogin()
            SID = sData['SID']
            ShowName = sData['ShowName']
            Del = web.input()
            #print Del
            nodeview = Del['nodeview']
            ng_pool = pool_dic()
            #print ng_pool[nodeview]
            pool_tr = ''''''
            ip = "127.0.0.1"
            for pool in ng_pool[nodeview]:
                if pool['status'] == "true":
                    Img_status = "/static/images/switch2.png"
                    pool_status = "/static/images/status1.gif"
                else:
                    Img_status = "/static/images/switch1.png"
                    pool_status = "/static/images/status2.gif"
                #print pool['ip'].replace('.','_')
                Img_status_id = "Img_status" + nodeview + str(pool['ip'].replace('.','_')) + str(pool['port'])
                pool_status_id = "pool_status" + nodeview + str(pool['ip'].replace('.','_')) + str(pool['port'])
                pool_tr += '''<tr class="datalist"><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td><img id="%s" src="%s"></td><td>%s</td><td>%s</td><td>%s</td><td><a href="javascript:void(0)" onclick="action_pool('%s','%s','%s','%s','%s')"><img id="%s" src="%s"></a></td><tr>''' % (ip,nodeview,pool['ip'],pool['port'],pool_status_id,pool_status,pool['weight'],pool['max_fails'],pool['fail_timeout'],ip,nodeview,pool['ip'],pool['port'],pool['status'],Img_status_id,Img_status)
            #print pool_tr
            s_pool = '''<table class="datalist" id="datalist"><thead><tr><th>Nginx IP</th><th>Pool</th><th>node</th><th>port</th><th>status</th><th>weight</th><th>max_fails</th><th>fail_timeout</th><th>Action</th></tr></thead><tbody>'''
            d_pool = '''</tbody></table>'''
            table_pool = s_pool + pool_tr + d_pool
            return table_pool
            #Del_id = Del['pid']
            #return web.seeother("/nginx/pool")
        else:
            web.setcookie('HTTP_REFERER', web.ctx.fullpath, 86400)
            return web.seeother("/login")

class Action:
    def POST(self):
        if getLogin():
            sData = getLogin()
            SID = sData['SID']
            ShowName = sData['ShowName']
            Del = web.input()
            ng_pool = pool_dic()
            print ng_pool,Del,"123"
            ip = Del['ip']
            pool_ip = Del['pool_ip']
            pool_port = Del['pool_port']
            pool_status = Del['pool_status']
            pool_nodeview = Del['nodeview']
            num_nodeview = len(ng_pool[pool_nodeview])
            #print ng_pool[pool_nodeview],pool_status 
            n = 0
            for nm in ng_pool[pool_nodeview]:
                if nm['status'] == 'true':
                    n += 1
            #print n
            if pool_status == 'true' and n <= 1:
                return "one_pool"
            else:
                st = Action_ng(pool_ip,pool_port,pool_status)
                return st
            #Del_id = Del['pid']
            #return web.seeother("/nginx/pool")
        else:
            web.setcookie('HTTP_REFERER', web.ctx.fullpath, 86400)
            return web.seeother("/login")

