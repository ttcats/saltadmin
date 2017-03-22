#!/usr/bin/env python

from celery import task,platforms
import time
from django.core.mail import send_mail

platforms.C_FORCE_ROOT = True

@task
def test(data,**kwargs):
#def sendmail(task_id, result, status, traceback, request="we", **kwargs):
  #return args,kwargs
  #mail = args
  time.sleep(10)
  return "sending mail to %s ..." % data



@task
def sendmail(title,content,tomail,**kwargs):
  send_mail(title,content,'ke.dong@travelzen.com',[tomail])
  return "mail_titile mail_content to %s ... " % content
