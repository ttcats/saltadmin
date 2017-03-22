#!/usr/bin/env python
#-*- coding:utf-8 -*-
from main import *


import sys
reload(sys)
sys.setdefaultencoding("utf-8")


def getOptions():
    try:
        opData = db.query('''select * from options where type in ("business","frame","status","project") and status="yes" order by type,value''')
    except Exception,e:
        print "MySQL Error: ",Exception,":",e
        return None
    sd = {'business':[],'frame':[],'status':[],'project':[]}
    for i in opData:
        sd[i.type].append({"id":i.id,"value":i.value})
    #要解决输出顺序问题
    return sd




# 项目管理
class Index:
    def GET(self):
        if getLogin():
            SID = getLogin()['SID']
            ShowName = getLogin()['ShowName']
            #print "ShowName: " + ShowName
            #return render.project(ShowName=ShowName,uid=SID)
            w = web.input(id="1",q='')
            page = int(w.id)
            per_page = 20
            offset = (page -1) * per_page
            print w
            if w['q'] == '':
                try:
                    pd = db.query('''select p.id,p.name,op3.value as lang,p.developer,p.ip_add,op1.value as pro,op.value as type,op2.value as status,u1.nickname as creator,p.cdate,u2.nickname as editor,p.mdate,p.comment
                              from project_base as p
                              left join options as op on p.type=op.id
                              left join options as op1 on p.pro=op1.id
                              left join options as op2 on p.status=op2.id
                              left join options as op3 on p.lang=op3.id
                              left join users as u1 on p.creator=u1.id
                              left join users as u2 on p.editor=u2.id limit %d offset %d''' % (per_page, offset))
                    post_count = db.query("SELECT COUNT(*) AS count FROM project_base")[0].count
                    page_count = post_count / per_page
                    if post_count % per_page > 0:
                        page_count += 1
                except:
                    return "服务器(数据库)错误"
            else:
                like = "%" + w['q'] + "%"
                #print like
                try:
                    pd = db.query('''select p.id,p.name,op3.value as lang,p.developer,p.ip_add,op1.value as pro,op.value as type,op2.value as status,u1.nickname as creator,p.cdate,u2.nickname as editor,p.mdate,p.comment
                              from project_base as p
                              left join options as op on p.type=op.id
                              left join options as op1 on p.pro=op1.id
                              left join options as op2 on p.status=op2.id
                              left join options as op3 on p.lang=op3.id
                              left join users as u1 on p.creator=u1.id
                              left join users as u2 on p.editor=u2.id where name like "%s"''' % like)
                    page_count = 1
                except:
                    return "服务器(数据库)错误"
            grace = 5
            range = grace * 2
            start = page - grace if page - grace > 0 else 1
            end = start + range
            if end > page_count:
                end = page_count
                start = end - range if end - range > 0 else 1
            return render.project(ShowName=ShowName,uid=SID,pd=pd,end=end, start=start, page=page, page_count=page_count)
        else:
            web.setcookie('HTTP_REFERER', web.ctx.fullpath, 86400)
            return web.seeother("/login")

# 添加项目
class Add:
    def GET(self):
        if getLogin():
            SID = getLogin()['SID']
            ShowName = getLogin()['ShowName']
            #print "ShowName: " + ShowName
            # 新增项目时发布机不属于项目属性,因此取消
            #rh = db.query('''select id,priip1 from hosts where role=(select id from options where type='role' and value='Release')''')
            selects = getOptions()
            #print selects
            return render.project_add(ShowName=ShowName,uid=SID,SD=selects)
        else:
            web.setcookie('HTTP_REFERER', web.ctx.fullpath, 86400)
            return web.seeother("/login")

    def POST(self):
        if getLogin() is False:
            web.ctx.status = '401 Unauthorized'
            return '401 - Unauthorized\n'
        p = web.input()
        # 插入域名前，应该有个域名检测，域名应该不能重复
        print p.bw,"p"
        check = db.query('''select id,name,cname from project_base where name="%s" and pro="%s"''' % (p.name,p.pro))
        if check:
            return '["repeat","%s","%s"]' % (check[0].name,p.pro)
	try:
            db.query('''insert into project_base(
                    name,lang,developer,type,status,comment,cdate,mdate,pro,creator,editor,ip_add)
                    values("%s","%s","%s","%s","%s","%s","%s",now(),"%s","%s","%s","%s")
                    ''' % (p.name,p.lang,p.developer,p.type,p.status,p.comment,p.cdate,p.pro,getLogin()['SID'],getLogin()['SID'],p.bw))
            pid = db.query('''select id from project_base where name="%s" and pro="%s" ''' % (p.name,p.pro))
        except Exception,e:
            # 无法提交，可能是数据库挂了
            print "Error: ",Exception,":",e
            return '["error","database","%s"]' % e
        # 添加成功
        rt = '["true","pid","%s"]' % (pid[0].id)
        #print 'Return Value: ',rt
        return rt

class Config:
    def GET(self):
        if getLogin():
            SID = getLogin()['SID']
            ShowName = getLogin()['ShowName']
            i = web.input()
            #rh = db.query('''select id,priip1 from hosts where role=(select id from options where type='role' and value='Release')''')
            pd = db.query('''select p.id,p.name,p.lang,p.developer,p.ip_add,p.type as type,p.status,u1.nickname as creator,p.cdate,u2.nickname as editor,p.mdate,p.comment,p.pro
                              from project_base as p
                              left join users as u1 on p.creator=u1.id
                              left join users as u2 on p.editor=u2.id
                              where p.id="%s"''' % i.pid)
            #s = db.query('''select id,priip1 from hosts where role=(select id from options where value="Web")''')
            selects = getOptions()
            print selects
            sm = []
            #for i in s:
            #    sm.append((i.id,i.priip1))
            #s = pd
            #print s
            #A = pd[0]
            #App = {"id":A.id,"frame":A.lang,"status":}
            return render.project_config(ShowName=ShowName,uid=SID,pd=pd[0],sm=sm,selects=selects)
        else:
            web.setcookie('HTTP_REFERER', web.ctx.fullpath, 86400)
            return web.seeother("/login")

    def POST(self):
        if getLogin() is False:
            web.ctx.status = '401 Unauthorized'
            return '401 - Unauthorized\n'
        i = web.input()
        print "Test Post Data: "
        print i,i.id
        print "####################"
        try:
            db.query('''update project_base set lang="%s",status="%s",pro="%s",comment="%s",ip_add="%s",type="%s",developer="%s" where id="%s"''' % (i.lang, i.status, i.pro, i.comment, i.bw, i.type, i.developer, i.id))
            return "Update_True"
        except:
            return "Error"
        #print "OK"
        #return web.seeother("/project")
        #return "Update_True"

class Del:
    def GET(self):
        if getLogin():
            sData = getLogin()
            SID = sData['SID']
            ShowName = sData['ShowName']
            Del = web.input()
            Del_id = Del["pid"]
            try:
                db.query('''DELETE FROM project_base WHERE id="%s"''' % Del_id)
                #print "ok"
            except Exception,e:
                # 无法提交，可能是数据库挂了
                print "MySQL Error: ",Exception,":",e
                return "Error"
            return web.seeother("/project")
        else:
            web.setcookie('HTTP_REFERER', web.ctx.fullpath, 86400)
            return web.seeother("/login")
