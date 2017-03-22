#coding=utf-8
from django.shortcuts import render, render_to_response
from django import forms
from app.models import *
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
#from django.contrib.admin import widgets
#from django.forms.extras.widgets import SelectDateWidget
#from timezone import timezone
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
#from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
#from django.core.mail import send_mail
from django.core import mail
from .tasks import sendmail


import sys
reload(sys)
sys.setdefaultencoding('utf-8')




def Login(request):
    print request.path
    if request.method == 'POST':
        print request.POST
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user:
            print request.COOKIES
            print request.session
            auth.login(request, user)
#            print user,"26"
            request.session['username'] = request.POST['username']
            request.session.get_expiry_age()
            request.session.get_expire_at_browser_close()
#            request.session.set_expiry(60)
            return HttpResponseRedirect('/app-one/')
        else:
            return render_to_response('app_info.html',{"login_err":"登陆失败:未知的用户名或密码错误"})
    return render_to_response('app_info.html')

def Logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/app-one/')



@login_required
def One(request):
    print request.POST,"123"
    print request.COOKIES
    user = request.session.get('username', 'anybody')
    print user
    if user == 'anybody':
        return HttpResponseRedirect('/')
    pros = Problems.objects.all()
    con = Event.objects.all()
    s1 = Event.objects.filter(author=user)
    v_user = Entrepreneur.objects.filter(entrepreneur=user)
    if request.method == 'POST':
        s = request.POST['statu']
        for i in v_user:
            if s == "busy" :
                i.working = "free"
                i.save()
            elif s == "free":
                i.working = "busy"
                i.save()
    if len(v_user) == 0:
        e_user = ""
    else:
        e_user = v_user[0]
    tag = Status.objects.get(id='5')
    ent = Entrepreneur.objects.all()
    event_wait = Event.objects.filter(status=Status.objects.get(id=1))
    vm = list(event_wait)
    ldle = {}
    for i in ent:
        if i.working != "busy":
            ldle[i]=i.time
    if len(ldle) != 0 and len(vm) != 0:
        sort = sorted(ldle.items(), key=lambda x:x[1])
        dele = sort[0][0]
        print dele,type(dele),type(dele.entrepreneur)
        event_one = vm.pop(0)
        event_one.status = Status.objects.get(id=2)
        event_one.enumerate = dele
        event_one.save()
        dele.working = "busy"
        dele.save()
        print dele.e_mail,event_one.author,event_one.createuser,"----------------------------create-------------------------------"
        mail_content = "工单创建人:" + event_one.author + "\n" + "工单事件人:" + event_one.createuser + "\n" + "部门:" + str(event_one.branch) + "\n" + "故障详情:" + event_one.content 
        mail_title = event_one.problem
        tomail = dele.e_mail
        sendmail.delay(mail_title,mail_content,tomail)
        
#        send_mail('Subject here',dele.entrepreneur,'ke.dong@travelzen.com',['835042664@qq.com'])
    return render_to_response('untitled.html', {'con':con, 'tag':tag, 'user':user, 'pros':pros,'ent':ent,'e_user':e_user,})


@login_required(login_url="/")
def Close(request, pro_id):
    user = request.session.get('username', 'anybody')
    pro = Problems.objects.all()
    tag = Status.objects.get(id='5')
    if Entrepreneur.objects.filter(entrepreneur=user):
        enum = Entrepreneur.objects.filter(entrepreneur=user)[0]
        try:
            pr = Problems.objects.get(id=pro_id)
            con = Event.objects.filter(status=tag,problem=pr,enumerate=enum) 
        except Exception:
            con = Event.objects.filter(status=tag,enumerate=enum)
    elif user == "root":
        try:
            pr = Problems.objects.get(id=pro_id)
            con = Event.objects.filter(status=tag,problem=pr) 
        except Exception:
            con = Event.objects.filter(status=tag) 
    else:
        try:
            pr = Problems.objects.get(id=pro_id)
            con = Event.objects.filter(status=tag,problem=pr,author=user)
        except Exception:
            con = Event.objects.filter(author=user,status=tag)
    paginator = Paginator(con, 10)
    page_num = request.GET.get('page')
    try:
        cons = paginator.page(page_num)
    except PageNotAnInteger:
        cons = paginator.page(1)
    except EmptyPage:
        cons = paginator.page(paginator.num_pages)
    return render_to_response('app_close2.html', {'pros':pro, 'cons':cons, 'tag':tag, 'user':user,})

class createquestion(forms.Form):
    name = forms.CharField(label='事件人')
#    floor = forms.ModelChoiceField(label='楼层',queryset=Floors.objects.all(),required=True,error_messages={'required':u'请选择'})
    branch = forms.ModelChoiceField(label='部门',queryset=Branches.objects.all(),required=True,error_messages={'required':u'请选择'})
    problem = forms.ModelChoiceField(label='故障类型',queryset=Problems.objects.all(),required=True,error_messages={'required':u'请选择'}) 
    content = forms.CharField(label='问题描述',widget=forms.Textarea(attrs={'rows':5,'style':"with:100%"}))
    img = forms.ImageField(label='截图附件',required=False)
    grade = forms.ModelChoiceField(label='紧急级别',queryset=Grades.objects.all(),required=True,error_messages={'required':u'请选择'})
    
@login_required(login_url="/")
def Create(request):
    print request.path
    print request.POST
    user = request.session.get('username', 'anybody')
    if user == "anybody":
        return render_to_response("create_info.html")
    else:
        if request.method == 'POST':
            form = createquestion(request.POST,request.FILES)
            if form.is_valid():
                name = form.cleaned_data['name']
#                floor = form.cleaned_data['floor']
                branch = form.cleaned_data['branch']
                problem = form.cleaned_data['problem']
                content = form.cleaned_data['content']
                grade = form.cleaned_data['grade']
                img = form.cleaned_data['img']
                if img is not None:
                    fl = open('/media/photos/' + form.cleaned_data['img'].name, 'wb+')
                    u = img.read()
                    fl.write(u)
                    fl.close()
                Event.objects.create(author=user,
                                     createuser=name,
#                                     floor=floor,
                                     branch=branch,
                                     problem=problem,
                                     content=content,
                                     createtime=timezone.now(),
                                     img=img,
                                     grade=grade,)
#                send_mail('Subject here','Here is the message.','ke.dong@travelzen.com',['835042664@qq.com'])
                #sendmail.delay('Subject here')
#                mail.send_mail('Subject here','Here is the message.','ke.dong@travelzen.com',['835042664@qq.com'])
                return HttpResponseRedirect('/app-one/')
        else:
            form = createquestion()
        return render_to_response("app_import.html", {"form":form, 'user':user},context_instance=RequestContext(request))

def Index(request, app_id):
    print request.session
    user = request.session.get('username', 'anybody')
    print request.POST,"163"
    pro = Event.objects.get(id=app_id)
    events = Event.objects.all()
    e_score = Score.objects.all()
    state_one = Status.objects.get(id='1')
    if Entrepreneur.objects.filter(entrepreneur=user):
        s = "1"
    else:
        s = "0"
    if pro.status == Status.objects.get(id='2') or pro.status == Status.objects.get(id='1'):
        if request.method == 'POST':
            if Entrepreneur.objects.filter(entrepreneur=user) or user == "root":
                form = admin_create(request.POST)
                if form.is_valid():
                    enumerat = form.cleaned_data['enumerate']
                    enumerat_Event = Entrepreneur.objects.filter(entrepreneur=pro.enumerate)
                    enumerat_Entre = Entrepreneur.objects.filter(entrepreneur=enumerat)
                    pro_user = pro.enumerate
                    pro.enumerate = enumerat
                    pro.save()
                    print pro.branch
                    print "--------------------------------------------------",enumerat.e_mail,type(enumerat),pro_user
                    mail_content = "工单创建人:" + pro.author + "\n" + "工单事件人:" + pro.createuser + "\n" + "部门:" + str(pro.branch) + "\n" + "故障详情:" + pro.content + "\n" + "改单人员:" + str(pro_user)
                    mail_title = pro.problem
                    tomail = enumerat.e_mail
                    sendmail.delay(mail_title,mail_content,tomail)
                    for e in enumerat_Event:
                        event_enum = []
                        for event in events:
                            if event.status != Status.objects.get(id=3) and event.status != Status.objects.get(id=5):
                                event_enum.append(event.enumerate)
                        if e not in event_enum:
                            e.working = "free"
                            e.time = timezone.now()
                            e.save()
                    for i in enumerat_Entre:
                        i.working = "busy"
                        i.save()
                    return HttpResponseRedirect('/app-one/')
                else:
                    pro.status = Status.objects.get(id='4')
                    pro.save()
                    return HttpResponseRedirect('/app-one/')
            else:
                pass
        else:
            form = admin_create()
        return render_to_response("app_index.html", {"pro":pro, "form":form, 'user':user, 'state_one':state_one ,'s':s})
    elif pro.status == Status.objects.get(id='4'):
        if request.method == 'POST':
            pro.status = Status.objects.get(id='3')
            pro.finishtime = timezone.now()
            pro.save()
            use = User.objects.get(username=pro.author)
            print pro.author,use.email,pro.enumerate,str(pro.problem)
            mail_content = "故障已经处理结束!请确认..." + "\n" + "故障处理人:" + str(pro.enumerate)
            mail_title = pro.problem
            tomail = use.email
            sendmail.delay(mail_title,mail_content,tomail)
#            send_mail('Subject here','Here is the message.','ke.dong@travelzen.com',['835042664@qq.com'])
            event = pro.enumerate
            even = Entrepreneur.objects.filter(entrepreneur=event)
            for i in even:
                event_enum = []
                for event in events:
                    if event.status != Status.objects.get(id=3) and event.status != Status.objects.get(id=5):
                        event_enum.append(event.enumerate)
                print event_enum
                if i not in event_enum:
                    i.working = "free"
                    i.time = timezone.now()
                    i.save()
            return HttpResponseRedirect('/app-one/')
        return render_to_response("app_index1.html", {"pro":pro, 'user':user, 's':s})
    elif pro.status == Status.objects.get(id='3'):
        coms = Com.objects.filter(envnt_id=app_id)
        if request.method == 'POST':
            try:
                if user != "anybody" :
                    score = request.POST["score"]
                    if user == pro.author or user == "root":
                        pro.status = Status.objects.get(id='5')
                    else:
                        pass
                    pro.e_score = score
                    pro.save()
            except Exception :
                pass
            content = request.POST["content"]
            if content != "":
                if user != "anybody":
                    Com.objects.create(envnt_id = app_id,
                                      name = user,
                                      time = timezone.now(),
                                      content = content,)
                else:
                    Com.objects.create(envnt_id = app_id,
                                      name = "匿名",
                                      time = timezone.now(),
                                      content = content,)
#            return HttpResponseRedirect('/app-one/')
            return HttpResponseRedirect("/index/%s/" % app_id)
        return render_to_response("app_index2.html", {"pro":pro, 'user':user, 'score':e_score, 'coms':coms })
    else:
        coms = Com.objects.filter(envnt_id=app_id)
        if request.method == 'POST':
            print request.POST
            try:
                if user != "anybody" :
                    score = request.POST["score"]
                    pro.e_score = score
                    pro.save()
            except Exception :
                pass
            content = request.POST["content"]
            if content != "":
                if user != "anybody":
                    Com.objects.create(envnt_id = app_id,
                                      name = user,
                                      time = timezone.now(),
                                      content = content,)
                else:
                    Com.objects.create(envnt_id = app_id,
                                      name = "匿名",
                                      time = timezone.now(),
                                      content = content,)
            return HttpResponseRedirect("/index/%s/" % app_id)
        return render_to_response("app_index3.html", {"pro":pro, 'user':user, 'score':e_score, 'coms':coms})

class admin_create(forms.Form):
    enumerate = forms.ModelChoiceField(label='更改故障处理人',empty_label="运维组",queryset=Entrepreneur.objects.all(),required=True,error_messages={'required':u'请确认'}) 



@login_required(login_url="/")
def Users(request):
    user = request.session.get('username', 'anybody')
    usr = User.objects.get(username=user)
    print usr.email
    return render_to_response("app_user.html", {"user":user})

def create_mail():
    begin = Status.objects.get(id=2)
    send_begin_event = Event.objects.filter(status=begin)
    for i in send_begin_event:
        Author_email = i.author + '@travelzen.com'
        Enumerate_email = i.enumerate.e_mail
        createuser = i.createuser
        title = 'author' + i.author + 'createuser' + i.createuser
        message = i.content
        send_mail(title, message, 'ke.dong@travelzen.com', [Enumerate_email])

def confirm_mail():
    end = Status.objects.get(id=3)
    send_end_event = Event.objects.filter(status=end)
    for s in send_end_event:
        Author_email = s.author + '@travelzen.com'
        problem = s.problem.ploblem
        message = '故障处理完成,请登陆工单确认'
        send_mail(problem, message, 'ke.dong@travelzen.com', [Author_email])

