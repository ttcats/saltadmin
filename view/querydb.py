#!/usr/bin/env python
#-*- coding:utf-8 -*-
from main import *
import time

from Mysql import *
from Postgre import *
from db_connet import *

import sys
reload(sys)
sys.setdefaultencoding('utf-8')




class Choose:
    @Check_Login
    def GET(self):
        sData = getLogin()
        SID = sData['SID']
        ShowName = sData['ShowName']
        i = web.input(sql = "")
        print i,"12"
        dbs = i["dbs"]
        input_tag = "input" + dbs
        div_tag = "div" + dbs
        one = '''<div style="margin-left:60px; padding-top:10px;">
            <input type="button" onclick="sql_1('showdbs','%s')" value="+" id="%s"><span> %s</span>
            <div id="%s" style="display:none"><div id="%s" class="dbs"></div></div></div>''' %(dbs, input_tag, dbs, div_tag, dbs)
        return one
        
class Sql_onput:
    @Check_Login
    def GET(self):
        sData = getLogin()
        User = sData['Username']
        i = web.input()
        sql = i['sql']
        sr = i['table'].split("#")[0]
        db_envname = i['table'].split("#")[1]
        time_query = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        try:
            if sr == "mysql":
                #fileds = Mysql("localhost","","",db,3306,sql)
                #print sql,sr,Db_name 
                Db_names = db.query('''select * from db_query where db_envname = "%s" ''' % db_envname)
                Names = Db_names[0]
                Db_name = Names['db_name']
                Db_ip = Names['db_ip']
                Db_port = int(Names['db_port'])
                #print Db_port,Db_ip,Db_name,"456"
                fileds = env(Db_ip,Db_port,Db_name,sql)
            elif sr == "pgsql":
                fileds = postgre("localhost","5432","postgres","123456",Db_name,sql)
            db.query('''insert into querysql_logs ( dbname,username,querysql,sendtime ) value ("%s", "%s", "%s", "%s")''' %(db_envname ,User,sql,time_query))
            #print fileds,"fileds",len(fileds)
            f2 = ''''''
            if fileds[0] == "ErroR":
                ende = fileds[1]
            else:
                for filed in fileds:
                    f1 = ''''''
                    for f in filed:
                        f1 += '''<th>%s</th>''' % f
                    f2 += '''<tr>%s</tr>'''  %f1
                table_head = '''<table class="querysql">'''
                table_end = '''</table>'''
                #ende = '''<table class="querysql"><tr><th>123</th><th>31</th><th>53</th></tr></table>'''
                ende = table_head + f2 + table_end  
        except Exception,e:
            print "lerror",e
        #return fileds
        return ende



class Sql_test:
    @Check_Login
    def GET(self):
        sData = getLogin()
        SID = sData['SID']
        ShowName = sData['ShowName']
        User = sData['Username']
        try:
            i = web.input(sql = "" )
            Sr = i['dbs']
            Sql = i['sql']
            ul_f = '''<ul>'''
            ul_l = '''</ul>'''
            ons = ''''''
            DB_names = []
            if Sql == "showdbs":
                if Sr == "mysql":
                    Db_id = db.query('''select db_id from dbquery_user where user_name = "%s"''' % User)
                    #print Db_id[0]
                    for i in Db_id:
                        #DB_ids.append(i['db_id'])
                        Db_names = db.query('''select * from db_query where id = "%s"''' %i['db_id'])
                        #print Db_names[0]
                        DB_names.append(Db_names[0]['db_envname'])
                    print DB_names
                    sql = "show databases;"
                    #DBs = Mysql("localhost","","","",3306,sql)
                    DBs = env("127.0.0.1",3306,"",sql)
                    print DBs,"DBs"
                elif Sr == "pgsql":
                    sql = "select datname from pg_database;"
                    DBs = postgre("localhost","5432","postgres","123456","test2",sql)
                #for dbname in DBs:
                for dbname in DB_names:
                    print dbname
                    table = Sr + "#" + dbname
                    inputid = "input" + table
                    divid = "div" + table
                    ons += '''<li><div><input type="button" onclick="sql_1('showtables','%s')" value="+" id="%s">
                        <span class="schema" name="%s">%s</span><div id="%s" style="display: none">
                        <div id="%s"></div></div></div></li>''' %(table, inputid, table, dbname, divid, table)
            elif Sql == "showtables":
                SR = Sr.split("#")[0]
                Db = Sr.split("#")[1]
                #print SR,Db
                if SR == "mysql":
                    sql = "show tables"
                    Db_names = db.query('''select * from db_query where db_envname = "%s"''' % Db)
                    #print Db_names[0]
                    Names = Db_names[0]
                    Db_name = Names['db_name']
                    Db_ip = Names['db_ip']
                    Db_port = int(Names['db_port'])
                    print Db_port,Db_ip,Db_name,"456"
                    Tables = env(Db_ip,Db_port,Db_name,sql)
                    #Tables = Mysql("localhost","","",Db,3306,sql)
                    print Tables
                elif SR == "pgsql":
                    sql = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';"
                    Tables = postgre("localhost","5432","postgres","123456",Db,sql)
                for Table in Tables:
                    Filed_tag =  Sr + "#" + Table[0]
                    inputid = "input" + Filed_tag
                    divid = "div" + Filed_tag
                    ons += '''<li><div><input type="button" onclick="sql_1('choice','%s')" value="+" id="%s" >
                        <span> %s</span><div id="%s" style="display: none">
                        <div id="%s"></div></div></div></li>''' %(Filed_tag, inputid, Table[0], divid, Filed_tag)
            elif Sql == "choice":
                SR = Sr.split("#")[0]
                Db = Sr.split("#")[1]
                Ta = Sr.split("#")[2]
                desc_tag = Sr + "#" + "disc"
                desc_inputid = "input" + desc_tag
                desc_divid = "div" + desc_tag
                index_tag = Sr + "#" + "index"
                index_inputid = "input" + index_tag
                index_divid = "div" + index_tag
                ons = '''<li><div><input type="button" onclick="sql_1('desc','%s')" value="+" id="%s">
                    <span>字段</span><div id="%s" style="display: none">
                    <div id="%s"></div></div></div></li>
                    <li><div><input type="button" onclick="sql_1('index','%s')" value="+" id="%s">
                    <span>索引</span><div id="%s" style="display: none">
                    <div id="%s"></div></div></div></li>''' %(desc_tag, desc_inputid, desc_divid, desc_tag, index_tag,index_inputid,index_divid,index_tag)
            elif Sql == "desc":
                SR = Sr.split("#")[0]
                Db = Sr.split("#")[1]
                Table = Sr.split("#")[2]
                print SR,Db,Table,"desc"
                if SR == "mysql":
                    sql = "desc %s"  % Table
                    print sql
                    db_name = db.query('''select * from db_query where db_envname = "%s"''' % Db)
                    Names = db_name[0]
                    Db_name = Names['db_name']
                    Db_ip = Names['db_ip']
                    Db_port = int(Names['db_port'])
                    fileds = env(Db_ip,Db_port,Db_name,sql)
                    #fileds = Mysql("localhost","","",Db,3306,sql)
                elif SR == "pgsql":
                    sql = "SELECT column_name FROM information_schema.columns WHERE table_name = '%s';" % Table
                    fileds = postgre("localhost","5432","postgres","123456",Db,sql)
                for filed  in fileds:
                    ons += '''<li>%s</li>''' % filed[0]
            elif Sql == "index":
                ons = '''<li>%s</li>''' % Sr
            one = ul_f + ons + ul_l
            #print one
            return one
            #return "sdf"
        except Exception,e:
            print "lerror",e
        return render.querydb(ShowName=ShowName,uid=SID)

    @Check_Login
    def POST(self):
        sData = getLogin()
        SID = sData['SID']
        ShowName = sData['ShowName']
        i =  web.input()
        #print web.input(),"post"
        info = i.customers.split(',')
        Sql = i.sql
        export = ""
        print info,Sql,"post"
        if Sql == "":
            export =  "No sql"
        else:
            if len(info) <= 1:
                message = "please choice Database"
                print message
            else:
                DB = info[0]
                dbName = info[1]
                print DB,dbName,"post"
                export = Mysql.Mysql("localhost","","",dbName,3306,Sql)
                print export
        return render.querydb(ShowName=ShowName,uid=SID,export=export)


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

