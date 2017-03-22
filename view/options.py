#!/usr/bin/env python
#-*- coding:utf-8 -*-
from main import *
import os


# 选项管理
class Option:
    def GET(self):
        if getLogin():
            sData = getLogin()
            SID = sData['SID']
            ShowName = sData['ShowName']
           
            i = web.input(id="1",q="")
            print i,"options"
            sel = i.q
            page = int(i.id)
            per_page = 20
            offset = (page -1) * per_page
            if sel == "":
                posts = db.query('''select * from options order by type,value limit %d offset %d''' % (per_page, offset))
                post_count = db.query("SELECT COUNT(*) AS count FROM options")[0].count
                page_count = post_count / per_page
                if post_count % per_page > 0:
                    page_count += 1
            else:
                like = "%" + sel + "%"
                posts = db.query('''select * from options where type like "%s"''' % like)
                page_count = 1
            page_posts = []
            SelectType = []
            for p in posts:
                page_posts.append({'id':p.id, 'type':p.type, 'value':p.value, 'comment':p.comment, 'status':p.status})
            grace = 5
            range = grace * 2
            start = page - grace if page - grace > 0 else 1
            end = start + range
            if end > page_count:
                end = page_count
                start = end - range if end - range > 0 else 1

            g = db.query('''select * from options order by type,value''')
            SelectType = []
            for i in g:
                if str(i.type) == 'option':
                    SelectType.append({'value':i.value,'comment':i.comment})
            return render.options(ShowName=ShowName,uid=SID,OpsData=page_posts,SelectType=SelectType,end=end, start=start, page=page, page_count=page_count)
        else:
            web.setcookie('HTTP_REFERER', web.ctx.fullpath, 86400)
            return web.seeother("/login")

    def POST(self):
        if getLogin() is False:
            web.ctx.status = '401 Unauthorized'
            return '401 - Unauthorized\n'
        i = web.input()
        #sr = web.data()
        #print sr
        OpsID = i.id
        OpsType = i.type
        OpsValue = i.value
        OpsComment = i.comment
        OpsStatus = i.status
        #print "Ops: " + OpsType + OpsValue
        if OpsID == "none":
            db.query('''insert into options(type,value,comment,status)values("%s","%s","%s","%s")''' % (OpsType,OpsValue,OpsComment,OpsStatus))
        else:
            db.query('''update options set type="%s",value="%s",comment="%s",status="%s" where id="%s"''' % (OpsType,OpsValue,OpsComment,OpsStatus,OpsID))
        return web.seeother("/options")
        #return render('alert("操作成功！");window.location.href="/admin/options";')



class Del:
    def GET(self):
        if getLogin():
            sData = getLogin()
            SID = sData['SID']
            ShowName = sData['ShowName']
            Del = web.input()
            Del_id = Del['pid']
            try:
                db.query('''DELETE FROM options WHERE id="%s"''' % Del_id)
            except Exception,e:
                # 无法提交，可能是数据库挂了
                print "MySQL Error: ",Exception,":",e
                return "Error"
            return web.seeother("/options")
        else:
            web.setcookie('HTTP_REFERER', web.ctx.fullpath, 86400)
            return web.seeother("/login")

class Enable:
    def GET(self):
        if getLogin():
            sData = getLogin()
            SID = sData['SID']
            ShowName = sData['ShowName']
            Del = web.input()
            Del_id = Del['pid']
            try:
                db.query('''update options set status="yes" WHERE id="%s"''' % Del_id)
                print "ds"
            except Exception,e:
                # 无法提交，可能是数据库挂了
                print "MySQL Error: ",Exception,":",e
                return "Error"
            return web.seeother("/options")
        else:
            web.setcookie('HTTP_REFERER', web.ctx.fullpath, 86400)
            return web.seeother("/login")

class Disable:
    def GET(self):
        if getLogin():
            sData = getLogin()
            SID = sData['SID']
            ShowName = sData['ShowName']
            Del = web.input()
            Del_id = Del['pid']
            try:
                db.query('''update options set status="no" WHERE id="%s"''' % Del_id)
                print "ds"
            except Exception,e:
                # 无法提交，可能是数据库挂了
                print "MySQL Error: ",Exception,":",e
                return "Error"
            return web.seeother("/options")
        else:
            web.setcookie('HTTP_REFERER', web.ctx.fullpath, 86400)
