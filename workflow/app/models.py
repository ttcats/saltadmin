#coding=utf-8
from django.db import models
#from timezone import timezone
from django.utils import timezone

class Floors(models.Model):
    floor = models.CharField(max_length=100,verbose_name = "楼层")
    
    def __unicode__(self):
        return self.floor
    
    class Meta:
        verbose_name = "楼层"
        verbose_name_plural = "楼层"


class Branches(models.Model):
    branch = models.CharField(max_length=100,verbose_name = "部门")
    
    def __unicode__(self):
        return self.branch
    
    class Meta:
        verbose_name = "部门"
        verbose_name_plural = "部门"
    
    
class Status(models.Model):
    status = models.CharField(max_length=100,verbose_name = "状态")
    
    def __unicode__(self):
        return self.status
    
    class Meta:
        verbose_name = "状态"
        verbose_name_plural = "状态"

class Entrepreneur(models.Model):
    entrepreneur = models.CharField(max_length=100,verbose_name ="维护人员")
    working = models.CharField(max_length=100,blank=True,null=True)
    ipone = models.CharField(max_length=100,blank=True,null=True)
    e_mail = models.CharField(max_length=100,blank=True,null=True)
    time = models.DateTimeField(blank=True,null=True)
    
    def __unicode__(self):
        return self.entrepreneur
    
    class Meta:
        verbose_name = "维护人员"
        verbose_name_plural = "维护人员"

class Problems(models.Model):
    ploblem = models.CharField(max_length=100,verbose_name = "故障类型")
    
    def __unicode__(self):
        return self.ploblem
    
    class Meta:
        verbose_name = "故障类型"
        verbose_name_plural = "故障类型"

class Grades(models.Model):
    grade = models.CharField(max_length=100,verbose_name = "故障等级")
    
    def __unicode__(self):
        return self.grade
    
    class Meta:
        verbose_name = "故障等级"
        verbose_name_plural = "故障等级"

class Score(models.Model):
    score = models.CharField(max_length=100,verbose_name = "评分等级")
    
    def __unicode__(self):
        return self.score
    
    class Meta:
        verbose_name = "评分等级"
        verbose_name_plural = "评分等级"
    

class Event(models.Model):
    author = models.CharField(max_length=100,blank=True,null=True)
    createuser = models.CharField(max_length=100)
    title = models.CharField(max_length=200,blank=True,null=True)
    floor = models.ForeignKey(Floors,default='1')
    branch = models.ForeignKey(Branches)
    problem = models.ForeignKey(Problems)
    content = models.TextField()
    img = models.ImageField(upload_to="photos",blank=True,null=True)
    grade = models.ForeignKey(Grades)
    status = models.ForeignKey(Status,default='1')
    createtime = models.DateTimeField(default=timezone.now())
    finishtime = models.DateTimeField(blank=True,null=True)
    enumerate = models.ForeignKey(Entrepreneur,default='1')
    #e_score = models.ForeignKey(Score,default='1')
    e_score = models.CharField(max_length=20,blank=True,null=True)
    
    def __unicode__(self):
        return self.createuser
    
    class Meta:
        verbose_name = "工单"
        verbose_name_plural = "工单"

    
class Com(models.Model):
    envnt_id = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    time = models.DateTimeField(default=timezone.now())
    content = models.TextField()
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = "评论"
        verbose_name_plural = "评论"

