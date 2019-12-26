from django.db import models

# Create your models here.
# class firewall_policy(models.Model):

# -*- coding: utf-8 -*-
from django import forms

class log_b(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    id_f = models.CharField(default='',max_length=128)
    operation = models.CharField(default='',max_length=16)
    user = models.CharField(default='',max_length=128)
    befor = models.CharField(default='',max_length=512)
    after = models.CharField(default='',max_length=512)

class log(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    id_f = models.CharField(default='',max_length=128)
    operation = models.CharField(default='',max_length=16)
    user = models.CharField(default='',max_length=128)
    befor = models.CharField(default='',max_length=512)
    after = models.CharField(default='',max_length=512)

class var(models.Model):
    var = models.CharField(default='',max_length=2000)

#
class User(models.Model):
    name = models.CharField(max_length=128,unique=True)
    password = models.CharField(max_length=256)
    level = models.CharField(default='',max_length=10)
    c_time = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(default='',max_length=128)
    course = models.EmailField(default='',max_length=10000)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = 'user'
        verbose_name_plural = 'user'
#
class Department(models.Model):
    name = models.CharField(default='',max_length=128)
    code = models.CharField(default='',max_length=16)
    description = models.CharField(default='',max_length=128)
    url_in_sustc = models.CharField(default='',max_length=128)
    college = models.CharField(default='',max_length=128)
    id_f = models.CharField(default='',max_length=128)
    level = models.CharField(default='1',max_length=128)
    super = models.CharField(default='0',max_length=128)

class Question(models.Model):
    questioner = models.CharField(default='',max_length=128)
    title = models.CharField(default='',max_length=10000)
    question = models.CharField(default='',max_length=10000)
    question_time = models.CharField(default='', max_length=128)
#
class Question_2(models.Model):
    questioner = models.CharField(default='',max_length=128)
    title = models.CharField(default='',max_length=10000)
    question = models.CharField(default='',max_length=10000)
    question_time = models.CharField(default='', max_length=128)
#
class Anwser(models.Model):
    question_id = models.CharField(default='',max_length=128)
    anwser = models.CharField(default='',max_length=10000)
    anwser_time = models.CharField(default='',max_length=128)
    respondent_level = models.CharField(default='',max_length=128)
    respondent_id = models.CharField(default='',max_length=128)
    star = models.CharField(default='',max_length=128)
    star_guy = models.CharField(default='',max_length=50000)


class General_knowledge(models.Model):
    department_code = models.CharField(default='',max_length=512)
    credit_min = models.CharField(default='', max_length=512)
    credit_min_gk = models.CharField(default='', max_length=512)
    credit_min_pe = models.CharField(default='', max_length=512)
    credit_min_el = models.CharField(default='', max_length=512)

#
class Course(models.Model):
    name = models.CharField(default='',max_length=200)
    name_code = models.CharField(default='',max_length=200)
    credit = models.CharField(default='',max_length=200)
    credit_for_exp = models.CharField(default='0',max_length=200)
    hours_per_week = models.CharField(default='',max_length=200)
    Opening_semester = models.CharField(default='',max_length=200)
    recommended_Opening_semester = models.CharField(default='',max_length=200)
    language = models.CharField(default='',max_length=200)
    prerequisite_courses = models.CharField(default='',max_length=200)
    department = models.CharField(default='',max_length=200)
    replace_course = models.CharField(default='',max_length=200)

    # content_all = models.CharField(default='', max_length=400)
    # content_all1 = models.CharField(default='', max_length=400)
    # add_time = models.CharField(default='', max_length=400)
    # last_change = models.CharField(default='', max_length=400)
    def __str__(self):
        return self.name

    def content(self):
        return "Name:"+self.name+" Code:"+self.name_code+" Department:"+self.department



class firewall(models.Model):
    name = models.CharField(default='',max_length=200)
    process = models.CharField(default='',max_length=200)
    local_ip = models.CharField(default='',max_length=200)
    local_port = models.CharField(default='',max_length=200)
    remote_ip = models.CharField(default='',max_length=200)
    remote_port = models.CharField(default='',max_length=200)
    protocol = models.CharField(default='',max_length=200)
    direction = models.CharField(default='',max_length=200)
    action = models.CharField(default='',max_length=200)
    type = models.CharField(default='',max_length=200)
    enalbled = models.CharField(default='',max_length=200)
    profile = models.CharField(default='',max_length=400)
    redirect_ip = models.CharField(default='',max_length=40)
    redirect_port = models.CharField(default='', max_length=40)
    # content_all = models.CharField(default='', max_length=400)
    content_all1 = models.CharField(default='', max_length=400)
    add_time = models.CharField(default='', max_length=400)
    last_change = models.CharField(default='', max_length=400)
    def __str__(self):
        return self.name

    def content(self):
        return "name:"+self.name+" process:"+self.process+" local_ip:"+self.local_ip+" local_port:"+self.local_port+" remote_ip:"+self.remote_ip+" remote_port:"+self.remote_port+" protocol:"+self.protocol+" direction:"+self.direction+" action:"+self.action+" type:"+self.type+" enalbled:"+self.enalbled+" profile:"+self.profile

class Rule(models.Model):
    number = models.IntegerField(default=0, verbose_name='order')
    name = models.CharField(default='',max_length=20,verbose_name='title')
    content = models.CharField(default='',max_length=1000,verbose_name='content')

    def __str__(self):
        return self.name
    #自定义返回的数据
    def test1(self):
        if 0:
            return 0
        return self.content

    class Meta:
        db_table = 'tb_Rule'  # 指明数据库表名
        verbose_name = 'rule'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __unicode__(self):
        return self.number

    # test1.short_dexcription = 'content'
#
class CaseFile(models.Model):
     name = models.CharField(default='no name',max_length=200)
     file_name = models.FileField(upload_to='case/%Y/%m/%d/', verbose_name=u"file_name")

     # 不注释会报错
     # def __str__(self):
     #     return self.file_name

     # 定义表名称
     class Meta:
         verbose_name = "t1"
         verbose_name_plural = "t2"


class Article(models.Model):
    title = models.CharField(u'title',max_length=256)
    content = models.TextField(u'content')
    pub_date = models.DateTimeField(u'time',auto_now_add=True)
    update_time = models.DateTimeField(u'uodate_time',auto_now=True)

    def __str__(self):
        return self.title

    # #自定义返回的数据
    # def test1(self):
    #     if
    #         return
    #     return self.title