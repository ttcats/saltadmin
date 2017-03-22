#!/usr/bin/env python
#-*- coding:utf-8 -*-
from main import *
import time

# 报告系统

# 故障上报系统
class Fault:
    @Check_Login
    def GET(self):
        sData = getLogin()
        SID = sData['SID']
        ShowName = sData['ShowName']
        try:
            getReports = db.query('''select * from reports''')
        except:
            return "Database Error"
        return render.report_fault(ShowName=ShowName,uid=SID,getReports=getReports)


class Add:
    @Check_Login
    def GET(self):
        SID = getLogin()['SID']
        ShowName = getLogin()['ShowName']
        #print "ShowName: " + ShowName
        #sd = getOptions()
        sd = {'status':["Finish","Not Finish"],'level':["I","II","III","IV","V"]}
        print sd,12
        if sd:
            return render.reportAdd(ShowName=ShowName,uid=SID,SD=sd)
        else:
            return "Options Error! You may check MySQL server ..."

    def POST(self):
        if getLogin() is False:
            web.ctx.status = '401 Unauthorized'
            return '401 - Unauthorized\n'
        p = web.input()
        print p
        time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print time_now
	try:
            db.query('''
                     insert into
                     reports (time, lasttime, faulty, hostip, project, user, level, status)
                     values ("%s","%s","%s","%s","%s","%s","%s","%s")
                     ''' %
                     (p.time, p.lasttime, p.faulty, p.hostip, p.project, p.user, p.level, p.status))
        except Exception,e:
        #    # 无法提交，可能是数据库挂了
            print "MySQL Error: ",Exception,":",e
            return "Error"
        # 添加成功
        return "Add.True"


class Del:
    def GET(self):
        if getLogin():
            sData = getLogin()
            SID = sData['SID']
            ShowName = sData['ShowName']
            Del = web.input()
            Del_id = Del['pid']
            try:
                db.query('''delete from reports WHERE id="%s"''' % Del_id)
                #print "ds"
            except Exception,e:
                # 无法提交，可能是数据库挂了
                print "MySQL Error: ",Exception,":",e
                return "Error"
            return web.seeother("/report/fault")
        else:
            web.setcookie('HTTP_REFERER', web.ctx.fullpath, 86400)
        



class Releaselog:
    @Check_Login
    def GET(self):
        sData = getLogin()
        SID = sData['SID']
        ShowName = sData['ShowName']
        try:
            getReports = db.query('''select * from release_logs order by id desc''')
        except:
            return "Database Error"
        return render.report_releaselogs(ShowName=ShowName,uid=SID,getReports=getReports)


class Querysqllog:
    @Check_Login
    def GET(self):
        sData = getLogin()
        SID = sData['SID']
        ShowName = sData['ShowName']
        try:
            getReports = db.query('''select * from querysql_logs order by id desc''')
        except:
            return "Database Error"
        return render.report_querysqllogs(ShowName=ShowName,uid=SID,getReports=getReports)

