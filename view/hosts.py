#!/usr/bin/env python
#-*- coding:utf-8 -*-
from main import *

import salt

# 获取适配hosts的select选项菜单值
def getOptions():
    try:
        opData = db.query('''select * from options where type in ("role","os","cpu","hdd","mem","model","idc","idctag","status") and status="yes" order by type,value''')
    except Exception,e:
        print "MySQL Error: ",Exception,":",e
        return None
    sd = {'role':[],'os':[],'cpu':[],'hdd':[],'mem':[],'model':[],'idc':[],'idctag':[],'status':[]}
    for i in opData:
        sd[i.type].append({"id":i.id,"value":i.value})
    #要解决输出顺序问题
    #print sd
    return sd





# 主机管理
class Index:
    def GET(self):
        if getLogin():
            SID = getLogin()['SID']
            ShowName = getLogin()['ShowName']
            print web.input(q='')
            w = web.input(q='') 
            if w['q'] == '':
                try:
                # 用多表查询实现
                    getHosts = db.query('''
                                    select h.id,priip1,pubip1,h.type,h.status,h.comment,
                                    op1.value as mem,
                                    op2.value as hdd,
                                    op3.value as os,
                                    op4.value as idc,
                                    op5.value as role,
                                    op6.value as model,
                                    op7.value as idctag,
                                    op8.value as status,
                                    u1.nickname as creator,
                                    u2.nickname as editor,
                                    h.mdate
                                    from hosts as h
                                    left join options as op1 on h.mem=op1.id
                                    left join options as op2 on h.hdd=op2.id
                                    left join options as op3 on h.os=op3.id
                                    left join options as op4 on h.idc=op4.id
                                    left join options as op5 on h.role=op5.id
                                    left join options as op6 on h.model=op6.id
                                    left join options as op7 on h.idctag=op7.id
                                    left join options as op8 on h.status=op8.id
                                    left join users as u1 on h.creator=u1.id
                                    left join users as u2 on h.editor=u2.id
                                    ''')
                except:
                    #return "服务器(数据库)错误"
                    return "Database Error"
            else:
                like = "%" + w['q'] + "%"
                try:
                # 用多表查询实现
                    getHosts = db.query('''
                                    select h.id,priip1,pubip1,h.type,h.status,h.comment,
                                    op1.value as mem,
                                    op2.value as hdd,
                                    op3.value as os,
                                    op4.value as idc,
                                    op5.value as role,
                                    op6.value as model,
                                    op7.value as idctag,
                                    op8.value as status,
                                    u1.nickname as creator,
                                    u2.nickname as editor,
                                    h.mdate
                                    from hosts as h
                                    left join options as op1 on h.mem=op1.id
                                    left join options as op2 on h.hdd=op2.id
                                    left join options as op3 on h.os=op3.id
                                    left join options as op4 on h.idc=op4.id
                                    left join options as op5 on h.role=op5.id
                                    left join options as op6 on h.model=op6.id
                                    left join options as op7 on h.idctag=op7.id
                                    left join options as op8 on h.status=op8.id
                                    left join users as u1 on h.creator=u1.id
                                    left join users as u2 on h.editor=u2.id
                                    where priip1 like "%s"
                                    ''' % like)
                except:
                    #return "服务器(数据库)错误"
                    return "Database Error"
            return render.hosts(ShowName=ShowName,uid=SID,getHosts=getHosts,sortShow=getOptions())
        else:
            web.setcookie('HTTP_REFERER', web.ctx.fullpath, 86400)
            return web.seeother("/login")




# 添加主机
class Add:
    @Check_Login
    def GET(self):
        SID = getLogin()['SID']
        ShowName = getLogin()['ShowName']
        #print "ShowName: " + ShowName
        sd = getOptions()
        print sd,12
        if sd:
            return render.hostAdd(ShowName=ShowName,uid=SID,SD=sd)
        else:
            return "Options Error! You may check MySQL server ..."

    def POST(self):
        if getLogin() is False:
            web.ctx.status = '401 Unauthorized'
            return '401 - Unauthorized\n'
        p = web.input()
        # 主机名和内网IP地址1的冲突检测
        try:
            getSQL = db.query('''select priip1 from hosts where  priip1="%s"''' % p.priip1)
        except Exception,e:
            print "MySQL Error: ",Exception,":",e
            return "Error"
        if getSQL:
            return "PriIP1Error"
        #if getSQL:
        #    for i in getSQL:
        #        if p.hostname == i.hostname:
                    # 主机名冲突
        #            return "HostnameError"
        #        if p.priip1 == i.priip1:
                    # 内网IP1冲突
        #            return "PriIP1Error"
        # 开始插入数据
	try:
            db.query('''
                     insert into
                     hosts (role,priip1,priip2,pubip1,pubip2,model,cpu,hdd,mem,os,rnum,storagedate,adminip,startdate,idc,idctag,status,comment,creator,editor)
                     values ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")
                     ''' %
                     (p.role,p.priip1,p.priip2,p.pubip1,p.pubip2,p.model,p.cpu,p.hdd,p.mem,p.os,p.rnum,p.storagedate,p.adminip,p.startdate,p.idc,p.idctag,p.status,p.comment,getLogin()['SID'],getLogin()['SID']))
            #db.query('''update hosts set role="%s",priip1="%s",priip2="%s",pubip1="%s",pubip2="%s",model="%s",cpu="%s",hdd="%s",mem="%s",os="%s",rnum="%s",storagedate="%s",adminip="%s",startdate="%s",idc="%s",idctag="%s",status="%s",comment="%s",creator="%s",editor="%s" where id="%s"''' %(p.role,p.priip1,p.priip2,p.pubip1,p.pubip2,p.model,p.cpu,p.hdd,p.mem,p.os,p.rnum,p.storagedate,p.adminip,p.startdate,p.idc,p.idctag,p.status,p.comment,getLogin()['SID'],getLogin()['SID'],p.id))
        except Exception,e:
            # 无法提交，可能是数据库挂了
            print "MySQL Error: ",Exception,":",e
            return "Error"
        # 添加成功
        return "Add.True"

# 编辑主机
class Edit:
    def GET(self):
        if getLogin():
            SID = getLogin()['SID']
            ShowName = getLogin()['ShowName']
            #print "ShowName: " + ShowName
            i = web.input()
            pid = i.pid
            sd = getOptions()
            hd = db.query('''select * from hosts where id="%s"''' % pid)
            h = hd[0]
            HostData = {"id":h.id,"priip1":h.priip1,"priip2":h.priip2,"pubip1":h.pubip1,"pubip2":h.pubip2,"adminip":h.adminip,"model":h.model,"cpu":h.cpu,"hdd":h.hdd,"mem":h.mem,"os":h.os,"rnum":h.rnum,"storagedate":h.storagedate,"startdate":h.startdate,"role":h.role,"idc":h.idc,"idctag":h.idctag,"status":h.status,"comment":h.comment}
            print "HostData: ",HostData
            return render.hostEdit(ShowName=ShowName,uid=SID,SD=sd,HostData=HostData)
        else:
            web.setcookie('HTTP_REFERER', web.ctx.fullpath, 86400)
            return web.seeother("/login")

    def POST(self):
        if getLogin() is False:
            web.ctx.status = '401 Unauthorized'
            return '401 - Unauthorized\n'
        p = web.input()
        print p
        # 主机名和内网IP地址1的冲突检测
        try:
            getSQL = db.query('''select priip1 from hosts where  priip1="%s"''' % (p.priip1))
        except Exception,e:
            print "MySQL Error: ",Exception,":",e
            return "Error"
        if getSQL:
            return "PriIP1Error"
            #for i in getSQL:
                #if str(p.id) != str(i.id):
                    # 首先排除对比自身的数据
                    #if p.priip1 == i.priip1:
                        # 内网IP1冲突
                        #return "PriIP1Error"
        # 开始更新数据
	try:
            db.query('''
                     update hosts
                     set role="%s",priip1="%s",priip2="%s",pubip1="%s",pubip2="%s",model="%s",cpu="%s",hdd="%s",mem="%s",os="%s",rnum="%s",storagedate="%s",adminip="%s",startdate="%s",idc="%s",idctag="%s",status="%s",comment="%s",editor="%s",mdate=now()
                     where id="%s"
                     ''' %
                     (p.role,p.priip1,p.priip2,p.pubip1,p.pubip2,p.model,p.cpu,p.hdd,p.mem,p.os,p.rnum,p.storagedate,p.adminip,p.startdate,p.idc,p.idctag,p.status,p.comment,getLogin()['SID'],p.id))
        except Exception,e:
            # 无法提交，可能是数据库挂了
            print "MySQL Error: ",Exception,":",e
            return "Error"
        # 添加成功
        return "Edit.True"


class Del:
    def GET(self):
        if getLogin():
            sData = getLogin()
            SID = sData['SID']
            ShowName = sData['ShowName']
            Del = web.input()
            Del_id = Del['pid']
            try:
                db.query('''delete from hosts WHERE id="%s"''' % Del_id)
                #print "ds"
            except Exception,e:
                # 无法提交，可能是数据库挂了
                print "MySQL Error: ",Exception,":",e
                return "Error"
            return web.seeother("/hosts")
        else:
            web.setcookie('HTTP_REFERER', web.ctx.fullpath, 86400)
