import hashlib
import os
import re
import time

import xlrd
from django.db.models.functions import window
from django.http import FileResponse
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
import pymysql
# import web1
from django.contrib import messages
import tkinter as tk
import web1.forms
from tkinter import filedialog

def decode_xlx(myFile):
    bok = xlrd.open_workbook(filename=None, file_contents=myFile.read())
    sht = bok.sheets()[0]
    row1 = sht.row_values(0)
    cell_d4 = sht.cell(1, 1).value
    print(len(sht.col_values(1)))
    row_num = sht.nrows

    r = len(sht.col_values(1))
    l = len(sht.col_values(1))

    print(r)
    print(l)

    name_of_department = ""
    error = 0
    errors = []
    pre_course_1 = []
    pre_course_1_addi = []
    pre_course_2 = []
    pre_course_2_addi = []
    req_course_base = []
    req_course_base_addi = []
    req_course_core = []
    req_course_core_addi = []
    req_course_exp = []
    req_course_exp_addi = []
    ele_course = []
    ele_course_addi = []
    exp_course = []
    exp_course_addi = []
    tb = {}
    fun_of_sci_eng = []
    fun_of_sci_eng_addi = []
    Eng = []
    Eng_addi = []
    Ipe = []
    Ipe_addi = []
    Pe = []
    Pe_addi = []
    W_c = []
    W_c_addi = []




    if sht.cell(0, 0).value == "Code for department":
        name_of_department = sht.cell(1, 0).value
        pass
    else:
        error = 1
    if sht.cell(0, 1).value == "Prerequisite courses for 1":
        for i in range(1, row_num):
            out = 0
            if (sht.cell(i, 1).value == ""):
                break;
            if (sht.cell(i, 1).value == "Additional"):
                out = 1
                for j in range(i + 1, row_num):
                    if (sht.cell(j, 1).value == ""):
                        break;
                    pre_course_1_addi.append(sht.cell(j, 1).value)
            if out == 1:
                break
            pre_course_1.append(sht.cell(i, 1).value)

    else:
        error = 1
    if sht.cell(0, 2).value == "Prerequisite courses for 2":
        for i in range(1, row_num):
            out = 0
            if (sht.cell(i, 2).value == ""):
                break;
            if (sht.cell(i, 2).value == "Additional"):
                out = 1
                for j in range(i + 1, row_num):
                    if (sht.cell(j, 2).value == ""):
                        break;
                    pre_course_2_addi.append(sht.cell(j, 2).value)
            if out == 1:
                break
            pre_course_2.append(sht.cell(i, 2).value)

    else:
        error = 1
    if sht.cell(0, 3).value == "Required course base":
        for i in range(1, row_num):
            out = 0
            if (sht.cell(i, 3).value == ""):
                break;
            if (sht.cell(i, 3).value == "Additional"):
                out = 1
                for j in range(i + 1, row_num):
                    if (sht.cell(j, 3).value == ""):
                        break;
                    req_course_base_addi.append(sht.cell(j, 3).value)
            if out == 1:
                break
            req_course_base.append(sht.cell(i, 3).value)
    else:
        error = 1

    if sht.cell(0, 4).value == "Required course core":
        for i in range(1, row_num):
            out = 0
            if (sht.cell(i, 4).value == ""):
                break;
            if (sht.cell(i, 4).value == "Additional"):
                out = 1
                for j in range(i + 1, row_num):
                    if (sht.cell(j, 4).value == ""):
                        break;
                    req_course_core_addi.append(sht.cell(j, 4).value)
            if out == 1:
                break
            req_course_core.append(sht.cell(i, 4).value)
    else:
        error = 1

    if sht.cell(0, 5).value == "Required course experience":
        for i in range(1, row_num):
            out = 0
            if (sht.cell(i, 5).value == ""):
                break;
            if (sht.cell(i, 5).value == "Additional"):
                out = 1
                for j in range(i + 1, row_num):
                    if (sht.cell(j, 5).value == ""):
                        break;
                    req_course_exp_addi.append(sht.cell(j, 5).value)
            if out == 1:
                break
            req_course_exp.append(sht.cell(i, 5).value)
    else:
        error = 1

    if sht.cell(0, 6).value == "Election":
        for i in range(1, row_num):
            out = 0
            if (sht.cell(i, 6).value == ""):
                break;
            if (sht.cell(i, 6).value == "Additional"):
                out = 1
                for j in range(i + 1, row_num):
                    if (sht.cell(j, 6).value == ""):
                        break;
                    ele_course_addi.append(sht.cell(j, 6).value)
            if out == 1:
                break
            ele_course.append(sht.cell(i, 6).value)
    else:
        error = 1

    if sht.cell(0, 7).value == "Experience":
        for i in range(1, row_num):
            out = 0
            if (sht.cell(i, 7).value == ""):
                break;
            if (sht.cell(i, 7).value == "Additional"):
                out = 1
                for j in range(i + 1, row_num):
                    if (sht.cell(j, 7).value == ""):
                        break;
                    exp_course_addi.append(sht.cell(j, 7).value)
            if out == 1:
                break
            exp_course.append(sht.cell(i, 7).value)
    else:
        error = 1

    if sht.cell(0, 11).value == "Fundamentals of science and Engineering":
        for i in range(1, row_num):
            out = 0
            if (sht.cell(i, 11).value == ""):
                break;
            if (sht.cell(i, 11).value == "Additional"):
                out = 1
                for j in range(i + 1, row_num):
                    if (sht.cell(j, 11).value == ""):
                        break;
                    fun_of_sci_eng_addi.append(sht.cell(j, 11).value)
            if out == 1:
                break
            fun_of_sci_eng.append(sht.cell(i, 11).value)
            print(sht.cell(i, 11).value)
    else:
        error = 1

    if sht.cell(0, 12).value == "English":
        for i in range(1, row_num):
            out = 0
            if (sht.cell(i, 12).value == ""):
                break;
            if (sht.cell(i, 12).value == "Additional"):
                out = 1
                for j in range(i + 1, row_num):
                    if (sht.cell(j, 12).value == ""):
                        break;
                    Eng_addi.append(sht.cell(j, 12).value)
            if out == 1:
                break
            Eng.append(sht.cell(i, 12).value)
    else:
        error = 1

    if sht.cell(0, 13).value == "IPE":
        for i in range(1, row_num):
            out = 0
            if (sht.cell(i, 13).value == ""):
                break;
            if (sht.cell(i, 13).value == "Additional"):
                out = 1
                for j in range(i + 1, row_num):
                    if (sht.cell(j, 13).value == ""):
                        break;
                    Ipe_addi.append(sht.cell(j, 13).value)
            if out == 1:
                break
            Ipe.append(sht.cell(i, 13).value)
    else:
        error = 1

    if sht.cell(0, 14).value == "PE":
        for i in range(1, row_num):
            out = 0
            if (sht.cell(i, 14).value == ""):
                break;
            if (sht.cell(i, 14).value == "Additional"):
                out = 1
                for j in range(i + 1, row_num):
                    if (sht.cell(j, 14).value == ""):
                        break;
                    Pe_addi.append(sht.cell(j, 14).value)
            if out == 1:
                break
            Pe.append(sht.cell(i, 14).value)
    else:
        error = 1

    if sht.cell(0, 15).value == "Writing and Comunication":
        for i in range(1, row_num):
            out = 0
            if (sht.cell(i, 15).value == ""):
                break;
            if (sht.cell(i, 15).value == "Additional"):
                out = 1
                for j in range(i + 1, row_num):
                    if (sht.cell(j, 15).value == ""):
                        break;
                    W_c_addi.append(sht.cell(j, 15).value)
            if out == 1:
                break
            W_c.append(sht.cell(i, 15).value)
    else:
        error = 1

    tmp = 0
    for i in range(1,12):
        tmp = tmp+int(sht.cell(i, 10).value)

    tb["t1"] = int(sht.cell(1, 10).value)
    tb["t2"] = int(sht.cell(2, 10).value)
    tb["t3"] = int(sht.cell(3, 10).value)
    tb["t4"] = int(sht.cell(4, 10).value)
    tb["t5"] = int(sht.cell(5, 10).value)
    tb["t6"] = int(sht.cell(6, 10).value)
    tb["t7"] = int(sht.cell(7, 10).value)
    tb["t8"] = int(sht.cell(8, 10).value)
    tb["t9"] = int(sht.cell(9, 10).value)
    tb["t10"] = int(sht.cell(10, 10).value)
    tb["t11"] = int(sht.cell(11, 10).value)
    tb["t12"] = tmp
    return error,name_of_department ,pre_course_1 ,pre_course_1_addi ,pre_course_2 ,pre_course_2_addi ,req_course_base ,req_course_base_addi , req_course_core , req_course_core_addi ,req_course_exp , req_course_exp_addi ,ele_course ,ele_course_addi ,exp_course ,exp_course_addi ,tb ,fun_of_sci_eng ,fun_of_sci_eng_addi , Eng , Eng_addi , Ipe , Ipe_addi , Pe , Pe_addi , W_c , W_c_addi

def download(request):
    file=open('PHY.xlsx','rb')
    response =FileResponse(file)
    response['Content-Type']='application/octet-stream'
    response['Content-Disposition']='attachment;filename="xlsx_file.xlsx"'
    return response

# use salt to create a hash code to hash password
def hash_code(s, salt='test1'):# 加点盐

    h = hashlib.sha256()

    s += salt

    h.update(s.encode())  # update方法只接收bytes类型

    return h.hexdigest()

# delete user
def D_b(request):
    # confirm it's login
    if  not (request.session.get('is_login', None) and request.session.get('level') =='3'):
        return redirect('/login')
    else:
        # get the id of user
        v = request.get_full_path().split("id=", 1)[1]
        tmp = web1.models.User.objects.get(pk=v)
        # delete
        web1.models.User.objects.filter(id=v).delete()
        # add log
        web1.models.log_b.objects.create(operation='Delete', user=request.session['user_name'], befor=tmp.name+" level:"+tmp.level,
                                  after='',
                                  id_f=v)

        user_list = web1.models.User.objects.all()

        return render(request, 'back.html', {'li': user_list})

# change information of user
def Change_b(request):
    # confirm it's login and level as admin
    if  not (request.session.get('is_login', None) and request.session.get('level') =='3'):
        return redirect('/login')
    if request.method == "POST":
        # back
        if 'back_regi_back' in request.POST:
            return redirect("/back/")
        # get old information
        tmp1 = web1.models.User.objects.get(pk=request.session['id_back'])

        #get input
        p1 = request.POST['password1_b']
        p2 = request.POST['password2_b']
        power = request.POST['power_b']
        email = request.POST['email_b']
        # power = request.POST['level2']
        messages = ''
        values1 = {'v1':tmp1.name,'message': messages, 'v2': '', 'v3': '', 'v4': '','v5':''}

        # judge the input
        if p1 != p2:
            messages = "两次输入密码不同"
            values1 = {'v1':tmp1.name,'message': messages, 'v2': '', 'v3': '', 'v4': power,'v5':email}
            return render(request, 'back_regi.html', values1)
        else :
            if power != '1' and power !='2' and power != '3':
                messages = "权限错误"
                values1 = {'v1':tmp1.name,'message': messages, 'v2': p1, 'v3': p2, 'v4': '','v5':email}
                return render(request, 'back_regi.html', values1)

            same_email_user = web1.models.User.objects.filter(email=email)
            if same_email_user :  # 邮箱地址唯一
                if not (len(same_email_user) == 1 and  same_email_user[0].id == tmp1.id):
                    messages = '该邮箱地址已被注册，请使用别的邮箱！'
                    values1 = {'v1': tmp1.name, 'message': messages, 'v2': p1, 'v3': p2, 'v4': power, 'v5': ''}
                    return render(request, 'back_regi.html', values1)
            if not re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$', email):
                messages = '邮箱地址错误'
                values1 = {'v1': tmp1.name, 'message': messages, 'v2': p1, 'v3': p2, 'v4': power, 'v5': ''}
                return render(request, 'back_regi.html', values1)
            else:
                # add password no change
                if p1 == tmp1.password:
                    web1.models.User.objects.filter(id=request.session['id_back']).update(level=power, email=email)
                else:
                    # add password change , get new hash password
                    web1.models.User.objects.filter(id=request.session['id_back']).update(password = hash_code(p1) ,level = power,email = email)
                tmp2 = web1.models.User.objects.get(pk=request.session['id_back'])
                # add log
                web1.models.log_b.objects.create(operation='Change', user=request.session['user_name'],
                                            befor=tmp1.name+ " level:" + tmp1.level+" email:"+tmp1.email,
                                            after=tmp2.name+ " level:" + tmp2.level+" email:"+tmp2.email,
                                            id_f=tmp1.id)
                return redirect("/back/")
    # init
    request.session['id_back'] = request.get_full_path().split("id=", 1)[1]

    tmp = web1.models.User.objects.get(pk=request.session['id_back'])
    values = {'v1':tmp.name,'message':'','v2':tmp.password , 'v3':tmp.password ,'v4':tmp.level,'v5':tmp.email}


    return render(request, 'back_regi.html', values)

# get log of user admin from database
def log_b(request):
    # back
    list = []
    if 'back' in request.POST:
        if request.session.get('log_back'):
            request.session.pop('log_back')
        return redirect("/back/")
    # get the request is one or all
    if  not (request.session.get('is_login', None) and request.session.get('level') =='3'):
        return redirect('/login')
    t = request.get_full_path().split("id=", 1)
    if len(t) > 1:
        v = request.get_full_path().split("id=", 1)[1]
        log_list = web1.models.log_b.objects.filter(id_f=v)
        request.session['log_back'] = v
    else:
        if(not request.session.get('log_back')):
            # all policy log
            log_list = web1.models.log_b.objects.all()
        else:
            # one policy log
            log_list = web1.models.log_b.objects.filter(id_f=request.session['log_back'])
    # search
    if 'search_log' in request.POST:
        s = request.POST['search_name'].lower()
        if  re.search(s, 'add') or  re.search(s, 'delete') or  re.search(s, 'change'):
            # search by operation
            log_list = log_list.filter(operation__icontains=s)
        else:
            # search by operator name
            log_list = log_list.filter(user__icontains=s)
        # for li in log_list:
        #     list.append(li.time.strftime(
        #         "%Y-%m-%d %H:%M") + ' id: ' + li.id_f + ' operator: ' + li.user + ' operation: ' + li.operation + ' befor: ' + li.befor + ' after: ' + li.after)
        return render(request, 'log_back.html', {'li': log_list})

    # list = []

    # for li in log_list:
    #     list.append(li.time.strftime("%Y-%m-%d %H:%M")+' id: '+li.id_f+' operator: '+li.user+' operation: '+li.operation+' befor: '+li.befor+' after: '+li.after)

    return render(request, 'log_back.html', {'li': log_list})

# login
def login(request):
    #避免重复登陆
    if request.session.get('is_login', None):
        return redirect('/login')

    if request.method == "POST":

        login_form = web1.forms.UserForm(request.POST)

        message = "请检查填写的内容！"

        if login_form.is_valid():

            username = login_form.cleaned_data['username']

            password = login_form.cleaned_data['password']

            try:

                user = web1.models.User.objects.get(name=username)

                if user.password == hash_code(password):

                    # save user info into session

                    request.session['is_login'] = True

                    request.session['user_id'] = user.id

                    request.session['user_name'] = user.name

                    request.session['level'] = user.level

                    request.session.set_expiry(0)

                    return redirect('/index/')

                else:

                    message = "密码不正确！"

            except:

                message = "用户不存在！"

        return render(request, 'login.html', locals())

    login_form = web1.forms.UserForm()

    return render(request, 'login.html', locals())

# link to different page from back.html
def back(request):
    # make sure session log_info is empty(used in search function in log of policy to get it's for on or for all)
    if request.session.get('log_info'):
        request.session.pop('log_info')
    if request.session.get('log_back'):
        request.session.pop('log_back')

    # confirm level
    if  not (request.session.get('is_login', None) and request.session.get('level') =='3'):
        return redirect('/login')
    user_list = web1.models.User.objects.all()
    if 'log_b' in request.POST:
        return redirect("/log_b/")
    if 'register' in request.POST:
        return redirect("/register/")
    if 'search' in request.POST:
        rule_list = web1.models.User.objects.all().filter(name__icontains=request.POST['search_name'])
        return render(request, 'back.html', {'li': rule_list})
    return render(request,'back.html',{'li':user_list})

# add user (by admin)
def register(request):

        # confirm level
        if not (request.session.get('is_login', None) and request.session.get('level') == '3'):
            return redirect('/login')
        # back
        if 'CreatUser_back' in request.POST:
            return redirect("/back/")
        if request.method == "POST":

            print('no back')
            register_form = web1.forms.RegisterForm(request.POST)

            message = "请检查填写的内容！"

            if register_form.is_valid():  # 获取数据

                username = register_form.cleaned_data['username']

                password1 = register_form.cleaned_data['password1']

                password2 = register_form.cleaned_data['password2']

                email = register_form.cleaned_data['email']
                # level = register_form.cleaned_data['level']
                level = register_form.cleaned_data['level2']
                # not empty
                if password1 == '' or password2 == '' or username =='' or level == '':
                    message = "不能为空！"

                    return render(request, 'CreateUser.html', locals())
                # password not sure
                if password1 != password2:  # 判断两次密码是否相同

                    message = "两次输入的密码不同！"

                    return render(request, 'CreateUser.html', locals())

                else:
                    # use name repeat
                    same_name_user = web1.models.User.objects.filter(name=username)

                    if same_name_user:  # 用户名唯一

                        message = '用户已经存在，请重新选择用户名！'

                        return render(request, 'CreateUser.html', locals())

                    # email repeat

                    same_email_user = web1.models.User.objects.filter(email=email)

                    if same_email_user:  # 邮箱地址唯一

                        message = '该邮箱地址已被注册，请使用别的邮箱！'

                        return render(request, 'CreateUser.html', locals())

                    if not (level == '1' or level == '2' or level == '3'):
                        message = '权限设置错误'

                        return render(request, 'CreateUser.html', locals())

                    if not re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$', email):
                        message = '邮箱地址错误'

                        return render(request, 'CreateUser.html', locals())
                    # 当一切都OK的情况下，创建新用户 everything right

                    new_user = web1.models.User.objects.create()

                    new_user.name = username

                    new_user.password = hash_code(password1)

                    new_user.level = level

                    new_user.email = email

                    new_user.save()
                    # add log
                    web1.models.log_b.objects.create(operation='Add', user=request.session['user_name'],
                                                befor='',
                                                after=username + " level:" + level+" email:"+email,
                                                id_f=new_user.id)

                    return redirect('/back/')  # 自动跳转到登录页面

        register_form = web1.forms.RegisterForm()
        return render(request, 'CreateUser.html', locals())

#logout
def logout(request):
    # confirm it's login
    if not request.session.get('is_login', None):

        # 如果本来就未登录，也就没有登出一说

        return redirect("/login/")
    # logout
    request.session.flush()
    return redirect("/login/")

# check the policy input
def check(a,b,type):
    ok = 1
    #name
    if not a['v1']:
        b['error1'] = '不能为空'
        a['v1'] = ''
        ok = 0;
    else:
        pass
    #process
    if not a['v2']:
        b['error2'] = '不能为空'
        a['v2'] = ''
        ok = 0;
    else:
        pass
    #local_ip
    if not a['v3']:
        b['error3'] = '不能为空'
        a['v3'] = ''
        ok = 0;
    else:
        # ip match v4 or v6 or /*
        x = a['v3'].split("/")
        if len(x) ==1:
            # v4 or v6
            if re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", x[0])\
                    or re.match(r"^(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}$", x[0], re.I):
                pass
            else:
                b['error3'] = 'IP invaild'
                a['v3'] = ''
                ok = 0;
        else:
            # 2 part ip + /*(0-32(v4) / 0-128(v6))
            if (re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", x[0])\
                  and  x[1].isdigit() and 0<=int(x[1])<=32 )or (re.match(r"^(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}$", x[0], re.I)and  x[1].isdigit() and 0<=int(x[1])<=128):
                pass
            else:
                b['error3'] = 'IP invaild'
                a['v3'] = ''
                ok = 0;
    #local_port
    if not a['v4']:
        b['error4'] = '不能为空'
        a['v4'] = ''
        ok = 0;
    else:
        x = a['v4'].split("/")
        # devide by /
        if len(x) == 1:
            # one part - any or * (0-65535) or *(0-65536)-*(0-65535)
            if x[0] == "any":
                pass
            else:
                if x[0].isdigit():
                    if(0<=int(x[0])<=65535):
                        pass
                    else:
                        b['error4'] = 'port invaild'
                        a['v4'] = ''
                        ok = 0;
                else:
                    y = x[0].split("-")
                    if len(y) == 2 and y[0].isdigit() and y[1].isdigit() and 0 <= int(y[0]) <= 65535 and 0 <= int(y[1]) <= 65535:
                        pass
                    else:
                        b['error4'] = 'port invaild'
                        a['v4'] = ''
                        ok = 0;
        else:
            # more than one part  */*/*/.....
            for xx in x:
                if xx.isdigit() and 0<int(xx)<65535:
                    pass
                else:
                    # y = xx.split("-")
                    # if len(y) == 2 and y[0].isdigit() and y[1].isdigit() and 0<=int(y[0])<=65535 and 0<=int(y[1])<=65535:
                    #     pass
                    # else:
                        b['error4'] = 'port invaild'
                        a['v4'] = ''
                        ok = 0;
    #remote_ip
    # same as local ip
    if not a['v5']:
        b['error5'] = '不能为空'
        a['v5'] = ''
        ok = 0;
    else:
        x = a['v5'].split("/")
        if len(x) ==1:

            if re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", x[0])\
                    or re.match(r"^(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}$", x[0], re.I):
                pass
            else:
                b['error3'] = 'IP invaild'
                a['v3'] = ''
                ok = 0;
        else:
            if (re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", x[0])\
                  and  x[1].isdigit() and 0<=int(x[1])<=32 )or (re.match(r"^(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}$", x[0], re.I)and  x[1].isdigit() and 0<=int(x[1])<=128):
                pass
            else:
                b['error3'] = 'IP invaild'
                a['v3'] = ''
                ok = 0;
    #remote_port
    # same as local port
    if not a['v6']:
        b['error6'] = '不能为空'
        a['v6'] = ''
        ok = 0;
    else:
        x = a['v6'].split("/")
        if len(x) == 1:
            if x[0] == "any":
                pass
            else:
                if x[0].isdigit():
                    if (0 <= int(x[0]) <= 65535):
                        pass
                    else:
                        b['error6'] = 'port invaild'
                        a['v6'] = ''
                        ok = 0;
                else:
                    y = x[0].split("-")
                    if len(y) == 2 and y[0].isdigit() and y[1].isdigit() and 0 <= int(y[0]) <= 65535 and 0 <= int(
                            y[1]) <= 65535:
                        pass
                    else:
                        b['error6'] = 'port invaild'
                        a['v6'] = ''
                        ok = 0;
        else:
            for xx in x:
                if xx.isdigit() and 0 < int(xx) < 65535:
                    pass
                else:
                    # y = xx.split("-")
                    # if len(y) == 2 and y[0].isdigit() and y[1].isdigit() and 0 <= int(y[0]) <= 65535 and 0 <= int(
                    #         y[1]) <= 65535:
                    #     pass
                    # else:
                        b['error6'] = 'port invaild'
                        a['v6'] = ''
                        ok = 0;
    #protocol
    if not a['v7']:
        b['error7'] = '不能为空'
        a['v7'] = ''
        ok = 0;
    else:
        pass
    #direction
    # inbound or outbound
    if not a['v8']:
        b['error8'] = '不能为空'
        a['v8'] = ''
        ok = 0;
    else:
        if a['v8'] == "inbound" or a['v8'] == "outbound":
            pass
        else:
            b['error8'] = 'invaild direction'
            a['v8'] = ''
            ok = 0;
    #action
    # permit or direct or redirect
    if not a['v9']:
        b['error9'] = '不能为空'
        a['v9'] = ''
        ok = 0;
    else:
        if a['v9'] == "permit" or a['v9'] == "direct" or a['v9'] == "redirect":
            pass
        else:
            b['error9'] = 'invaild action'
            a['v9'] = ''
            ok = 0;
    #type
    # system or control
    if not a['v10']:
        b['error10'] = '不能为空'
        a['v10'] = ''
        ok = 0;
    else:
        if a['v10'] == "system" or a['v10'] == "control":
            pass
        else:
            b['error10'] = 'invaild type'
            a['v10'] = ''
            ok = 0;
    #enalbled
    # false or true
    if not a['v11']:
        b['error11'] = '不能为空'
        a['v11'] = ''
        ok = 0;
    else:
        if a['v11'] == "false" or a['v11'] == "true":
            pass
        else:
            b['error11'] = 'invaild type'
            a['v11'] = ''
            ok = 0;
    #profile
    # public private domain any combination
    if not a['v12']:
        b['error12'] = '不能为空'
        a['v12'] = ''
        ok = 0;
    else:
        if a['v12'] =="public|private|domain" or a['v12'] =="public|private" or a['v12'] =="public|domain" or a['v12'] =="private|domain" or a['v12'] =="public" or a['v12'] =="private" or a['v12'] =="domain" :
            pass
        else:
            b['error12'] = 'invaild profile'
            a['v12'] = ''
            ok = 0;
            #redirect_ip
    # when action = redirect the follow two are vaild
    if a['v9'] == "redirect":

        if not a['v14']:
            b['error14'] = '不能为空'
            a['v14'] = ''
            ok = 0;
        else:
            if a['v14'].isdigit() and 0<=int(a['v14'])<=65535:
                pass
            else:
                b['error14'] = 'refirect_port invaild'
                a['v14'] = ''
                ok = 0;
        if not a['v13']:
            b['error13'] = '不能为空'
            a['v13'] = ''
            ok = 0;
        else:
            if re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",
                        a['v13']) \
                    or re.match(r"^(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}$", a['v13'], re.I):
                pass
            else:
                b['error13'] = 'redirect_ip invaild'
                a['v13'] = ''
                ok = 0;
    else:
        if a['v13']:
            b['error13'] = 'redirect_ip invaild'
            a['v13'] = ''
            ok = 0;
        if a['v14']:
            b['error14'] = 'redirect_ip invaild'
            a['v14'] = ''
            ok = 0;
    return a,b,ok

def check1(a,b,type):
    ok = 1
    #name
    if not a['v1']:
        b['error1'] = '不能为空'
        a['v1'] = ''
        ok = 0;
    else:
        pass
    #process
    if not a['v2']:
        b['error2'] = '不能为空'
        a['v2'] = ''
        ok = 0;
    else:
        list = web1.models.Course.objects.all().filter(name_code = a['v2'])
        if len(list) >0:
            b['error2'] = 'Duplicate'
            a['v2'] = ''
            ok = 0;
        pass
    #local_ip
    if not a['v3']:
        b['error'] = '不能为空'
        a['v3'] = ''
        ok = 0;
    else:
        pass
    if not a['v4']:
        b['error4'] = '不能为空'
        a['v4'] = ''
        ok = 0;
    else:
        pass
    if not a['v5']:
        b['error5'] = '不能为空'
        a['v5'] = ''
        ok = 0;
    else:
        pass
    if not a['v6']:
        b['error6'] = '不能为空'
        a['v6'] = ''
        ok = 0;
    else:
        pass
    if not a['v7']:
        b['error7'] = '不能为空'
        a['v7'] = ''
        ok = 0;
    else:
        pass
    if not a['v8']:
        b['error8'] = '不能为空'
        a['v8'] = ''
        ok = 0;
    else:
        pass
    if not a['v9']:
        b['error9'] = '不能为空'
        a['v9'] = ''
        ok = 0;
    else:
        pass
    if not a['v10']:
        b['error10'] = '不能为空'
        a['v10'] = ''
        ok = 0;
    else:
        pass
    if not a['v11']:
        b['error11'] = '不能为空'
        a['v11'] = ''
        ok = 0;
    else:
        pass
    return a,b,ok

def check2(a,b,type):
    ok = 1
    #name
    if not a['v1']:
        b['error1'] = '不能为空'
        a['v1'] = ''
        ok = 0;
    else:
        pass
    #process
    if not a['v3']:
        b['error'] = '不能为空'
        a['v3'] = ''
        ok = 0;
    else:
        pass
    if not a['v4']:
        b['error4'] = '不能为空'
        a['v4'] = ''
        ok = 0;
    else:
        pass
    if not a['v5']:
        b['error5'] = '不能为空'
        a['v5'] = ''
        ok = 0;
    else:
        pass
    if not a['v6']:
        b['error6'] = '不能为空'
        a['v6'] = ''
        ok = 0;
    else:
        pass
    if not a['v7']:
        b['error7'] = '不能为空'
        a['v7'] = ''
        ok = 0;
    else:
        pass
    if not a['v8']:
        b['error8'] = '不能为空'
        a['v8'] = ''
        ok = 0;
    else:
        pass
    if not a['v9']:
        b['error9'] = '不能为空'
        a['v9'] = ''
        ok = 0;
    else:
        pass
    if not a['v10']:
        b['error10'] = '不能为空'
        a['v10'] = ''
        ok = 0;
    else:
        pass
    if not a['v11']:
        b['error11'] = '不能为空'
        a['v11'] = ''
        ok = 0;
    else:
        pass
    return a,b,ok

def test_for_c(request):
    print("in there")
    if request.session.get('is_login', None):
        if request.method == "POST":
            # button submit
            if 'k_submit' in request.POST:
                # get input
                name1 = request.POST['name']
                name_code1 = request.POST['name_code']
                credit1 = request.POST['credit']
                credit_for_exp1 = request.POST['credit_for_exp']
                hours_per_week1 = request.POST['hours_per_week']
                Opening_semester1 = request.POST['opening_semester']
                recommended_opening_semester1 = request.POST['recommended_opening_semester']
                language1 = request.POST['language']
                prerequisite_courses1 = request.POST['prerequisite_courses']
                department1 = request.POST['department']
                replace_course1 = request.POST['replace_course']

                # got checkbox and change to *|*|* format

                # input dirc, send to check function to check
                values = {'v1': name1, 'v2': name_code1, 'v3': credit1, 'v4': credit_for_exp1, 'v5': hours_per_week1,
                          'v6': Opening_semester1, 'v7': recommended_opening_semester1, 'v8': language1, 'v9': prerequisite_courses1, 'v10': department1 , 'v11' : replace_course1}

                # error diec to return
                empty_error = {'error1': '', 'error2': '', 'error3': '', 'error4': '', 'error5': '', 'error6': '',
                               'error7': '', 'error8': '', 'error9': '', 'error10': '' , 'error11':''}
                ok = 1;
                # check
                values, empty_error, ok = check1(values, empty_error, 1)
                # ttest1 = {}
                # for iter1 in web1.models.Course.objects.all():
                #     ttest1[iter1.name] = iter1.name

                if ok == 1:
                    # add
                    print("add")
                    # add policy
                    tmp = web1.models.Course.objects.create(name=name1, name_code=name_code1, credit=credit1,
                                                              credit_for_exp=credit_for_exp1,
                                                              hours_per_week=hours_per_week1, Opening_semester=Opening_semester1,
                                                              recommended_Opening_semester=recommended_opening_semester1,
                                                              language=language1,
                                                              prerequisite_courses=prerequisite_courses1, department=department1,replace_course = replace_course1
                                                              )
                    # add log
                    # web1.models.log.objects.create(operation='Add', user=request.session['user_name'], befor='',
                    #                                after=content_all, id_f=tmp.id)
                    rule_list = web1.models.Course.objects.all()
                    return render(request, 'infor_department_test.html', {'li': rule_list})
                else:
                    from collections import Counter
                    # return right input and change wrong input to '' and return
                    z = {**values, **empty_error}
                    return render(request, 'test_for_course.html', z)
            else:
                # init
                rule_list = web1.models.Course.objects.all()
                return render(request, 'infor_department_test.html', {'li': rule_list})
    else:
        return redirect('/login')


#add policy
def add_page(request,c = 0):
    print('in add_page')
    # confirm login
    if  request.session.get('is_login', None):
        if request.method == "POST":
            # button submit
            if 'f_submit' in request.POST:
                # get input
                name1 = request.POST['name']
                process1 = request.POST['process']
                local_ip1 = request.POST['local_ip']
                local_port1 = request.POST['local_port']
                remote_ip1 = request.POST['remote_ip']
                remote_port1 = request.POST['remote_port']
                protocol1 = request.POST['protocol']
                direction1 = request.POST['direction']
                action1 = request.POST['action']
                type1 = request.POST['type']
                enalbled1 = request.POST['enalbled']

                # got checkbox and change to *|*|* format
                if not request.POST.get('public') == None:
                    profile1 = 'public'
                else:
                    profile1 = ''

                if not request.POST.get('private') == None:
                    if profile1 == '':
                        profile1 = 'private'
                    else:
                        profile1 += '|private'

                if not request.POST.get('domain') == None:
                    if profile1 == '':
                        profile1 = 'domain'
                    else:
                        profile1 += '|domain'
                redirect_ip1 = request.POST['redirect_ip']
                redirect_port1 = request.POST['redirect_port']

                # input dirc, send to check function to check
                values = {'v1': name1, 'v2': process1, 'v3': local_ip1, 'v4': local_port1, 'v5': remote_ip1,
                          'v6': remote_port1, 'v7': protocol1, 'v8': direction1, 'v9': action1, 'v10': type1,
                          'v11': enalbled1, 'v12': profile1,'v13':redirect_ip1,'v14':redirect_port1 }

                # error diec to return
                empty_error = {'error1': '', 'error2': '', 'error3': '', 'error4': '', 'error5': '', 'error6': '',
                               'error7': '', 'error8': '', 'error9': '', 'error10': '', 'error11': '', 'error12': '','error13':'','error14':'' }
                ok = 1;
                # check
                values, empty_error, ok = check(values, empty_error, 1)
                # ttest1 = {}
                # for iter1 in web1.models.Course.objects.all():
                #     ttest1[iter1.name] = iter1.name

                if ok == 1:
                    # add
                    print("add")
                    if action1 == "redirect":
                        content_all = "name:"+name1+" process:"+process1+" local_ip:"+local_ip1+" local_port:"+local_port1+" remote_ip:"+remote_ip1+" remote_port:"+remote_port1+" protocol:"+protocol1+" direction:"+direction1+" action:"+action1+" type:"+type1+" enalbled:" + enalbled1+" profile:"+profile1+" redirect_ip:"+redirect_ip1+" redirect_port:"+redirect_port1
                    else:
                        content_all = "name:"+name1+" process:"+process1+" local_ip:"+local_ip1+" local_port:"+local_port1+" remote_ip:"+remote_ip1+" remote_port:"+remote_port1+" protocol:"+protocol1+" direction:"+direction1+" action:"+action1+" type:"+type1+" enalbled:" + enalbled1+" profile:"+profile1
                    # add policy
                    tmp = web1.models.firewall.objects.create(name=name1, process=process1, local_ip=local_ip1,
                                                   local_port=local_port1,
                                                   remote_ip=remote_ip1, remote_port=remote_port1, protocol=protocol1,
                                                   direction=direction1,
                                                   action=action1, type=type1, enalbled=enalbled1, profile=profile1,
                                                   redirect_ip = redirect_ip1,redirect_port = redirect_port1,
                                                   content_all1=content_all,add_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+" User:"+request.session['user_name'],
                                                         last_change = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+" User:"+request.session['user_name'])
                    # add log
                    web1.models.log.objects.create(operation='Add',user = request.session['user_name'] , befor='',after=content_all,id_f=tmp.id)
                    rule_list = web1.models.firewall.objects.all()
                    return render(request, 'infor_department_test.html', {'li': rule_list})
                else:
                    from collections import Counter
                    # return right input and change wrong input to '' and return
                    z = {**values, **empty_error}
                    return render(request, 'info_add_page.html', z)
            else:
                # init
                rule_list = web1.models.firewall.objects.all()
                return render(request, 'infor_department_test.html', {'li': rule_list})
    else:
        return redirect('/login')

# some function in info_all html
def search(request):
    if request.session.get('is_login', None):
        # search
        if 'search' in request.POST:
            # fuzzy Matching
            rule_list = web1.models.Course.objects.all().filter(name__icontains=request.POST['search_name'])
            return render(request, 'infor_department_test.html', {'li': rule_list})
        # show all log of policy
        elif 'log' in request.POST:
            log_list = web1.models.log.objects.all()
            return render(request,'info_log.html',{'li':log_list})
        # download policy
        elif 'download' in request.POST:
            # open selection window to got address
            root = tk.Tk()
            root.withdraw()
            # complete address
            file_path = filedialog.asksaveasfilename(title=u'保存文件', filetypes=[("TXT", ".txt")])
            print(file_path + ".txt")
            rule_list = web1.models.Course.objects.all().order_by('id').order_by('type')
            # open(create) file
            f = open(file_path + ".txt", 'a')
            for li in rule_list:
                f.write('id:'+str(li.id)+' '+li.content_all1)
                f.write('\n')
            root.destroy()
            rule_list =web1.models.Course.objects.all()
            return render(request, 'infor_department_test.html', {'li': rule_list})
        else:
            # init
            return render(request, 'test_for_course.html')
    else:
        return redirect('/login')

def search1(request):
    if request.session.get('is_login', None):
        # search
        if 'search' in request.POST:
            # fuzzy Matching
            rule_list = web1.models.Course.objects.all().filter(name_code__icontains=request.POST['search_name'])
            return render(request, 'infor_department_test.html', {'li': rule_list})
        # show all log of policy
        elif 'log' in request.POST:
            log_list = web1.models.log.objects.all()
            return render(request,'info_log.html',{'li':log_list})
        # download policy
        elif 'download' in request.POST:
            file = open('/Users/kumazuirin/PycharmProjects/test11/test11/PHY.xlsx', 'rb')
            response = FileResponse(file)
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment;filename="xlsx_file.xlsx"'

            # tmp_file_list = web1.models.CaseFile.objects.all().filter(id = 9)
            # for li in tmp_file_list:
            #     tmp_file = li.file_name
            #     response = FileResponse(tmp_file)
            #     response['Content-Type'] = 'application/octet-stream'
            #     response['Content-Disposition'] = 'attachment;filename="xlsx_file.xlsx"'
            return response
        elif 'download_c' in request.POST:
            file = open('/Users/kumazuirin/PycharmProjects/test11/test11/Course_template.xlsx', 'rb')
            response = FileResponse(file)
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment;filename="xlsx_file.xlsx"'

            # tmp_file_list = web1.models.CaseFile.objects.all().filter(id = 9)
            # for li in tmp_file_list:
            #     tmp_file = li.file_name
            #     response = FileResponse(tmp_file)
            #     response['Content-Type'] = 'application/octet-stream'
            #     response['Content-Disposition'] = 'attachment;filename="xlsx_file.xlsx"'
            return response
        elif 'upload' in request.POST:
            myFile =request.FILES.get("myfile", None)
            tmp = myFile
            # ff = FileForm(request.POST, request.FILES)
            print(type(myFile))
            # print(myFile.read())
            if myFile != None:
                error = 0
                try:
                    error_out = ""
                    error , name_of_department ,pre_course_1 ,pre_course_1_addi ,pre_course_2 ,pre_course_2_addi ,req_course_base ,req_course_base_addi , req_course_core , req_course_core_addi ,req_course_exp , req_course_exp_addi ,ele_course ,ele_course_addi ,exp_course ,exp_course_addi ,tb ,fun_of_sci_eng ,fun_of_sci_eng_addi , Eng , Eng_addi , Ipe , Ipe_addi , Pe , Pe_addi , W_c , W_c_addi = decode_xlx(request.FILES.get("myfile", None))
                    print(name_of_department)
                    print(pre_course_1)
                    for it in pre_course_1:
                        c_list = web1.models.Course.objects.all().filter(name_code = it)
                        if len(c_list) == 0:
                            error_out += it+" (in pre_course_1)    "
                    print(pre_course_1_addi)
                    print(pre_course_2)
                    for it in pre_course_2:
                        c_list = web1.models.Course.objects.all().filter(name_code = it)
                        if len(c_list) == 0:
                            error_out += it+" (in pre_course_2)    "
                    print(pre_course_2_addi)
                    print(req_course_base)
                    for it in req_course_base:
                        c_list = web1.models.Course.objects.all().filter(name_code = it)
                        if len(c_list) == 0:
                            error_out += it+" (in req_course_base)    "
                    print(req_course_base_addi)
                    print(req_course_core)
                    for it in req_course_core:
                        c_list = web1.models.Course.objects.all().filter(name_code = it)
                        if len(c_list) == 0:
                            error_out += it+" (in req_course_core)    "
                    print(req_course_core_addi)
                    print(req_course_exp)
                    for it in req_course_exp:
                        c_list = web1.models.Course.objects.all().filter(name_code = it)
                        if len(c_list) == 0:
                            error_out += it+" (in req_course_exp)    "
                    print(req_course_exp_addi)
                    print(ele_course)
                    for it in ele_course:
                        c_list = web1.models.Course.objects.all().filter(name_code = it)
                        if len(c_list) == 0:
                            error_out += it+" (in ele_course)    "
                    print(ele_course_addi)
                    print(exp_course)
                    for it in exp_course:
                        c_list = web1.models.Course.objects.all().filter(name_code = it)
                        if len(c_list) == 0:
                            error_out += it+" (in exp_course)    "
                    print(exp_course_addi)
                    print(tb)
                    print(fun_of_sci_eng)
                    for it in fun_of_sci_eng:
                        c_list = web1.models.Course.objects.all().filter(name_code = it)
                        if len(c_list) == 0:
                            error_out += it+" (in fun_of_sci_eng)    "
                    print(fun_of_sci_eng_addi)
                    print(Eng)
                    for it in Eng:
                        c_list = web1.models.Course.objects.all().filter(name_code = it)
                        if len(c_list) == 0:
                            error_out += it+" (in Eng)    "
                    print(Eng_addi)
                    print(Ipe)
                    for it in Ipe:
                        c_list = web1.models.Course.objects.all().filter(name_code = it)
                        if len(c_list) == 0:
                            error_out += it+" (in Ipe)    "
                    print(Ipe_addi)
                    print(Pe)
                    for it in Pe:
                        c_list = web1.models.Course.objects.all().filter(name_code = it)
                        if len(c_list) == 0:
                            error_out += it+" (in Pe)    "
                    print(Pe_addi)
                    print(W_c)
                    for it in W_c:
                        c_list = web1.models.Course.objects.all().filter(name_code = it)
                        if len(c_list) == 0:
                            error_out += it+" (in W_c)    "
                    print(W_c_addi)



                    if error_out =="":
                        tmp_file = web1.models.CaseFile.objects.create(name=name_of_department, file_name=myFile)
                        web1.models.Department.objects.all().filter(code = name_of_department).update(id_f = tmp_file.id)
                        messages.success(request, "Upload successful")
                    else:
                        print(error_out)
                        error_out = "Upload error "+error_out +" is not in DataBase"
                        messages.success(request, error_out)
                except Exception as e:
                    messages.success(request, "File is not correct")
                    rule_list = web1.models.Department.objects.all().filter(level="1")
                    return render(request, 'info_all_department.html', {'li': rule_list})
            else:
                messages.success(request, "No file")

            rule_list = web1.models.Department.objects.all().filter(level="1")
            return render(request, 'info_all_department.html', {'li': rule_list})
            # pass
        elif 'upload_c' in request.POST:
            myFile = request.FILES.get("myfile", None)
            tmp = myFile
            # ff = FileForm(request.POST, request.FILES)
            print(type(myFile))
            # print(myFile.read())
            if myFile != None:
                myFile = request.FILES.get("myfile", None)

                try:
                    bok = xlrd.open_workbook(filename=None, file_contents=myFile.read())
                    sht = bok.sheets()[0]

                    row_num = len(sht.row_values(1))
                    col_num = len(sht.col_values(1))
                    print(row_num)
                    print(col_num)
                    if (row_num != 11):
                        messages.success(request, "the file is not correct")
                        rule_list = web1.models.Course.objects.all()
                        return render(request, 'infor_department_test.html', {'li': rule_list})
                    for i in range(1, col_num):
                        dup = web1.models.Course.objects.filter(name_code=sht.cell(i, 1).value)

                        if dup:
                            web1.models.Course.objects.filter(name_code=sht.cell(i, 1).value).update(
                                name=sht.cell(i, 0).value, name_code=sht.cell(i, 1).value, credit=sht.cell(i, 2).value,
                                credit_for_exp=sht.cell(i, 3).value, hours_per_week=sht.cell(i, 4).value,
                                Opening_semester=sht.cell(i, 5).value,
                                recommended_Opening_semester=sht.cell(i, 6).value, language=sht.cell(i, 7).value,
                                prerequisite_courses=sht.cell(i, 8).value, department=sht.cell(i, 9).value,
                                replace_course=sht.cell(i, 10).value)
                            print("dup for {}".format(sht.cell(i, 1).value))
                            # for dupp in dup:
                            #     print("dup for {}".format(sht.cell(i,1).value))
                            #     web1.models.Course.objects.filter(name_code=sht.cell(i, 1).value)
                            #     dupp.update(name = sht.cell(i,0).value , name_code = sht.cell(i,1).value , credit = sht.cell(i,2).value , credit_for_exp = sht.cell(i,3).value , hours_per_week = sht.cell(i,4).value , Opening_semester = sht.cell(i,5).value , recommended_Opening_semester = sht.cell(i,6).value , language = sht.cell(i,7).value , prerequisite_courses = sht.cell(i,8).value , department = sht.cell(i,9).value , replace_course = sht.cell(i,10).value)
                        else:
                            web1.models.Course.objects.create(name=sht.cell(i, 0).value, name_code=sht.cell(i, 1).value,
                                                              credit=sht.cell(i, 2).value,
                                                              credit_for_exp=sht.cell(i, 3).value,
                                                              hours_per_week=sht.cell(i, 4).value,
                                                              Opening_semester=sht.cell(i, 5).value,
                                                              recommended_Opening_semester=sht.cell(i, 6).value,
                                                              language=sht.cell(i, 7).value,
                                                              prerequisite_courses=sht.cell(i, 8).value,
                                                              department=sht.cell(i, 9).value,
                                                              replace_course=sht.cell(i, 10).value)
                    messages.success(request, "Upload successful")
                except Exception as e :
                    messages.success(request, "the file is not correct")
                    rule_list = web1.models.Course.objects.all()
                    return render(request, 'infor_department_test.html', {'li': rule_list})

            rule_list = web1.models.Course.objects.all()
            return render(request, 'infor_department_test.html', {'li': rule_list})

        else:
            # init
            return render(request, 'test_for_course.html')
    else:
        return redirect('/login')

def order_QA(x):
    t1 = len(web1.models.Anwser.objects.all().filter(question_id = x.id))

    return t1

def QA_action(request):
    if request.session.get('is_login', None):
        # search
        if 'search' in request.POST:
            # fuzzy Matching
            QA_list = web1.models.Question_2.objects.all().filter(title__icontains=request.POST['search_name']).order_by('-question_time')
            for item in QA_list:
                item.hot = len(web1.models.Anwser.objects.all().filter(question_id = item.id))
                for item2 in web1.models.Anwser.objects.all().filter(question_id = item.id):
                    item.hot = int(item.hot)+int(item2.star)
            return render(request, 'info_Q_A_all.html', {'li': QA_list})
        # show all log of policy
        elif 'add' in request.POST:
            return render(request,'info_QA_add.html')
        # download policy
        elif 'hot' in request.POST:
            QA_list = web1.models.Question_2.objects.all()
            for item in QA_list:
                item.hot = len(web1.models.Anwser.objects.all().filter(question_id = item.id))
                for item2 in web1.models.Anwser.objects.all().filter(question_id = item.id):
                    item.hot = int(item.hot)+int(item2.star)
            QA_list = sorted(QA_list, key=order_QA, reverse=True)
            for item in QA_list:
                print(order_QA(item))
            return render(request, 'info_Q_A_all.html', {'li': QA_list})
        elif 'mine' in request.POST:
            QA_list = web1.models.Question_2.objects.all().filter(questioner=request.session['user_name'])
            for item in QA_list:
                item.hot = len(web1.models.Anwser.objects.all().filter(question_id = item.id))
                for item2 in web1.models.Anwser.objects.all().filter(question_id = item.id):
                    item.hot = int(item.hot)+int(item2.star)
            return render(request, 'info_Q_A_all.html', {'li': QA_list})
        elif 'no_anwser' in request.POST:
            QA_list = []
            for item in web1.models.Question_2.objects.all():
                if len(web1.models.Anwser.objects.all().filter(question_id = item.id)) == 0:
                    QA_list.append(item)
            for item in QA_list:
                item.hot = len(web1.models.Anwser.objects.all().filter(question_id = item.id))
                for item2 in web1.models.Anwser.objects.all().filter(question_id = item.id):
                    item.hot = int(item.hot)+int(item2.star)
            return render(request, 'info_Q_A_all.html', {'li': QA_list})
        else:
            # init
            return render(request, 'test_for_course.html')
    else:
        return redirect('/login')

def QA_answer(request):
    if request.session.get('is_login', None):
        v = request.get_full_path().split("id=", 1)[1]
        tmp = web1.models.Question_2.objects.get(pk=v)
        value = {}
        value['v0'] = v
        value['v1'] = tmp.title
        value['v2'] = tmp.question
        return render(request, 'info_Q_A_anwser.html', value)
    else:
        return redirect('/login')

def QA_show_one(request):
    print("arrive ")
    if request.session.get('is_login', None):
        v = request.get_full_path().split("id=", 1)[1]
        tmp = web1.models.Question_2.objects.get(pk=v)
        value = {}
        value['v1'] = tmp.title
        value['v2'] = tmp.question
        return render(request, 'info_Q_A_one.html', value)
    else:
        return redirect('/login')

def QA_anwsers_one(request):
    if request.session.get('is_login', None):
        v = request.get_full_path().split("id=", 1)[1]
        tmp = web1.models.Anwser.objects.get(pk=v)
        ttmp = web1.models.Question_2.objects.get(pk = tmp.question_id)
        value = {}
        value['v00'] = v
        value['v0'] = ttmp.id
        value['v1'] = ttmp.title
        value['v2'] = ttmp.question
        value['v3'] = tmp.respondent_id
        value['v4'] = tmp.anwser
        return render(request, 'info_Q_A_anwser_one.html', value)
    else:
        return redirect('/login')
def QA_add(request):
    print("in there")
    if request.session.get('is_login', None):
        if request.method == "POST":
            # button submit
            if 'QA_anwser_submit' in request.POST:
                print(request.POST['id'])
                question_id = request.POST['id']
                title = request.POST['title']
                question = request.POST['question']
                anwser = request.POST['anwser']
                if len(anwser) == 0:
                    value = {}
                    value['v0'] = question_id
                    value['v1'] = title
                    value['v2'] = question
                    errors = {}
                    errors['error1'] = "title can't be empty"
                    z = {**value, **errors}
                    return render(request, 'info_QA_add.html', z)
                web1.models.Anwser.objects.create(question_id = question_id , anwser = anwser , anwser_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) , respondent_level = request.session['level'] , respondent_id = request.session['user_name'] , star = '0' , star_guy = '')
                QA_list = web1.models.Question_2.objects.all().order_by('-question_time')
                for item in QA_list:
                    item.hot = len(web1.models.Anwser.objects.all().filter(question_id = item.id))
                    for item2 in web1.models.Anwser.objects.all().filter(question_id=item.id):
                        item.hot = int(item.hot)+int(item2.star)
                return render(request, 'info_Q_A_all.html', {'li': QA_list})
            if 'QA_goodjob' in request.POST:
                anwser_id = request.POST['id_a']
                tmp = web1.models.Anwser.objects.get(pk = anwser_id)
                guys = tmp.star_guy
                star = tmp.star
                guy_list = guys.split('/')
                ok = 1
                for item in guy_list:
                    if item == request.session['user_name']:
                        messages.success(request, "You have supported")
                        ok = 0
                        break
                if ok == 1:
                    guys = guys+request.session['user_name']+'/'
                    star_1 = int(star) +1
                    web1.models.Anwser.objects.filter(id = anwser_id).update(star = star_1 , star_guy = guys)
                    messages.success(request, "Successful")

                ttmp = web1.models.Question_2.objects.get(pk=tmp.question_id)
                value = {}
                value['v00'] = anwser_id
                value['v0'] = ttmp.id
                value['v1'] = ttmp.title
                value['v2'] = ttmp.question
                value['v3'] = tmp.respondent_id
                value['v4'] = tmp.anwser
                return render(request, 'info_Q_A_anwser_one.html', value)

            if 'QA_back2' in request.POST:
                question_id = request.POST['id']
                tmp = web1.models.Question_2.objects.get(pk=question_id)
                anwser_list = web1.models.Anwser.objects.all().filter(question_id=question_id).order_by('-respondent_level','-star')
                print(anwser_list)
                for item in anwser_list:
                    print(item.respondent_id)
                return render(request, 'info_Q_A_anwsers.html',
                              {'li': anwser_list, 'v0': question_id, 'v1': tmp.title, 'v2': tmp.question})
            if 'QA_submit' in request.POST:
                # get input
                title = request.POST['title']
                question = request.POST['question']
                values = {'v1': title, 'v2': question }
                empty_error = {'error1': '', 'error2': ''}
                ok = 1
                if len(title) == 0:
                    ok = 0
                    empty_error['error1'] = "title can't be empty"
                if len(question) == 0:
                    ok = 0
                    empty_error['error2'] = "question can't be empty"
                print(request.session['user_name'])
                if ok == 1:
                    # add
                    print("add")
                    web1.models.Question_2.objects.create(questioner = request.session['user_name'] , title = title , question = question , question_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                    # add
                    QA_list = web1.models.Question_2.objects.all().order_by('-question_time')
                    for item in QA_list:
                        item.hot = len(web1.models.Anwser.objects.all().filter(question_id = item.id))
                        for item2 in web1.models.Anwser.objects.all().filter(question_id=item.id):
                            item.hot = int(item.hot)+int(item2.star)
                    return render(request, 'info_Q_A_all.html', {'li': QA_list})
                else:
                    from collections import Counter
                    # return right input and change wrong input to '' and return
                    z = {**values, **empty_error}
                    return render(request, 'info_QA_add.html', z)
            else:
                # init
                QA_list = web1.models.Question_2.objects.all().order_by('-question_time')
                for item in QA_list:
                    item.hot = len(web1.models.Anwser.objects.all().filter(question_id = item.id))
                    for item2 in web1.models.Anwser.objects.all().filter(question_id=item.id):
                        item.hot = int(item.hot)+int(item2.star)
                return render(request, 'info_Q_A_all.html', {'li': QA_list})
    else:
        return redirect('/login')

def QA_show_anwsers(request):
    if request.session.get('is_login', None):
        v = request.get_full_path().split("id=", 1)[1]
        tmp = web1.models.Question_2.objects.get(pk=v)
        value = {}
        value['v0'] = v
        value['v1'] = tmp.title
        value['v2'] = tmp.question
        anwser_list = web1.models.Anwser.objects.all().filter(question_id = v).order_by('-respondent_level','-star')
        print(anwser_list)
        for item in anwser_list:
            print(item.respondent_id)
        return render(request, 'info_Q_A_anwsers.html', {'li':anwser_list , 'v0':v , 'v1':tmp.title , 'v2':tmp.question})
    else:
        return redirect('/login')

# search function in policy's log(for one or all)
def log(request):
    # back
    if 'back' in request.POST:
        if request.session.get('log_info'):
            request.session.pop('log_info')
        return redirect("/index/")
    t = request.get_full_path().split("id=", 1)
    # print(len(t))
    # one policy's log
    # to confirm one or all policy,use session'log_info' to store the policy id(if is all , store nothing)
    if len(t) > 1:
        v = request.get_full_path().split("id=", 1)[1]
        log_list = web1.models.log.objects.filter(id_f=v)
        request.session['log_info'] = v
    else:
        if(not request.session.get('log_info')):
            # all policy log
            log_list = web1.models.log.objects.all()
        else:
            # one policy log
            log_list = web1.models.log.objects.filter(id_f=request.session['log_info'])
    # search
    if 'search_log' in request.POST:
        s = request.POST['search_name'].lower()
        if  re.search(s, 'add') or  re.search(s, 'delete') or  re.search(s, 'change'):
            # search by operation
            log_list = log_list.filter(operation__icontains=s)
        else:
            # search by operator name
            log_list = log_list.filter(user__icontains=s)
        return render(request, 'info_log.html', {'li': log_list})
    return render(request, 'info_log.html', {'li': log_list})

# delete policy
def D(request):
    # confirm login
    if request.session.get('is_login', None):
        # get id
        v = request.get_full_path().split("id=", 1)[1]
        # delete
        tmp = web1.models.Course.objects.get(pk = v)
        web1.models.Course.objects.filter(id=v).delete()
        # add log
        web1.models.log.objects.create(operation='Delete', user=request.session['user_name'], befor=tmp.content_all1, after='',
                                  id_f=v)
        rule_list = web1.models.Course.objects.all()
        return render(request, 'infor_department_test.html', {'li': rule_list})
    else:
        return redirect('/login')

def Q_D(request):
    # confirm login
    if request.session.get('is_login', None):
        # get id
        v = request.get_full_path().split("id=", 1)[1]
        # delete
        web1.models.Question_2.objects.filter(id=v).delete()
        web1.models.Anwser.objects.filter(question_id=v).delete()
        # add log
        QA_list = web1.models.Question_2.objects.all().order_by('-question_time')
        for item in QA_list:
            item.hot = len(web1.models.Anwser.objects.all().filter(question_id = item.id))
            for item2 in web1.models.Anwser.objects.all().filter(question_id=item.id):
                item.hot = int(item.hot)+int(item2.star)
        return render(request, 'info_Q_A_all.html', {'li': QA_list})
    else:
        return redirect('/login')

def Q_A_D(request):
    # confirm login
    if request.session.get('is_login', None):
        # get id
        v = request.get_full_path().split("id=", 1)[1]
        # delete
        vv = web1.models.Anwser.objects.get(pk=v).question_id
        web1.models.Anwser.objects.filter(id=v).delete()
        # add log
        v = vv

        tmp = web1.models.Question_2.objects.get(pk=v)
        value = {}
        value['v0'] = v
        value['v1'] = tmp.title
        value['v2'] = tmp.question
        anwser_list = web1.models.Anwser.objects.all().filter(question_id=v).order_by('-respondent_level', '-star')
        print(anwser_list)
        for item in anwser_list:
            print(item.respondent_id)
        return render(request, 'info_Q_A_anwsers.html',
                      {'li': anwser_list, 'v0': v, 'v1': tmp.title, 'v2': tmp.question})
    else:
        return redirect('/login')

def change_1(request):
    # confirm login
    if  request.session.get('is_login', None):
        if request.method == "POST":
            # print("00")
            # submit button
            if 'c_submit' in request.POST:
                name1 = request.POST['name']
                name_code1 = request.POST['name_code']
                credit1 = request.POST['credit']
                credit_for_exp1 = request.POST['credit_for_exp']
                hours_per_week1 = request.POST['hours_per_week']
                Opening_semester1 = request.POST['opening_semester']
                recommended_opening_semester1 = request.POST['recommended_opening_semester']
                language1 = request.POST['language']
                prerequisite_courses1 = request.POST['prerequisite_courses']
                department1 = request.POST['department']
                replace_course1 = request.POST['replace_course']

                # same as add
                values_t = {'v1': name1, 'v2': name_code1, 'v3': credit1, 'v4': credit_for_exp1, 'v5': hours_per_week1,
                            'v6': Opening_semester1,
                            'v7': recommended_opening_semester1, 'v8': language1, 'v9': prerequisite_courses1, 'v10': department1 , 'v11' : replace_course1}

                empty_error = {'error1': '', 'error2': '', 'error3': '', 'error4': '', 'error5': '', 'error6': '',
                               'error7': '',
                               'error8': '', 'error9': '', 'error10': '' , 'error11' : ''}

                values_t, empty_error, ok = check2(values_t, empty_error, 2)
                # same as add
                # ok = 1  #
                if ok == 1:
                    # print(1)

                    web1.models.Course.objects.all().filter(name_code = name_code1).update(name=name1,credit=credit1,
                                                            credit_for_exp=credit_for_exp1,
                                                            hours_per_week=hours_per_week1,
                                                            Opening_semester=Opening_semester1,
                                                            recommended_Opening_semester=recommended_opening_semester1,
                                                            language=language1,
                                                            prerequisite_courses=prerequisite_courses1,
                                                            department=department1,replace_course = replace_course1
                                                            )

                else:
                    z = {**values_t, **empty_error}
                    return render(request, 'test_info_change_page.html', z)

            else:
                pass
            rule_list = web1.models.Course.objects.all()
            return render(request, 'infor_department_test.html', {'li': rule_list})
        # init get the policy
        rule_list = web1.models.Course.objects.all().filter(id=request.get_full_path().split("id=", 1)[1])
        for li in rule_list:
            # name1 = request.POST['name']
            # name_code1 = request.POST['name_code']
            # credit1 = request.POST['credit']
            # credit_for_exp1 = request.POST['credit_for_exp']
            # hours_per_week1 = request.POST['hours_per_week']
            # Opening_semester1 = request.POST['opening_semester']
            # recommended_opening_semester1 = request.POST['recommended_opening_semester']
            # language1 = request.POST['language']
            # prerequisite_courses1 = request.POST['prerequisite_courses']
            # department1 = request.POST['department']
            name1 = li.name
            name_code1 = li.name_code
            credit1 = li.credit
            credit_for_exp1 = li.credit_for_exp
            hours_per_week1 = li.hours_per_week
            Opening_semester1 = li.Opening_semester
            recommended_Opening_semester1 = li.recommended_Opening_semester
            language1 = li.language
            prerequisite_courses1 = li.prerequisite_courses
            department1 = li.department
            replace_course1 = li.replace_course

        values = {'v1': name1, 'v2': name_code1, 'v3': credit1, 'v4': credit_for_exp1, 'v5': hours_per_week1, 'v6': Opening_semester1,
                  'v7': recommended_Opening_semester1, 'v8': language1, 'v9': prerequisite_courses1, 'v10': department1 , 'v11' : replace_course1}
        print(values['v1'])
        return render(request, 'test_info_change_page.html', values)
    else:
        return redirect('/login')

# change policy
def change_(request):
    # confirm login
    if  request.session.get('is_login', None):
        if request.method == "POST":
            # print("00")
            # submit button
            if 'c_submit' in request.POST:
                # print("01")
                # get input
                print(request.POST['direction'])
                print(request.POST['action'])
                print(request.POST['type'])
                print(request.POST['enalbled'])
                print(request.POST.get('public'))
                print(request.POST.get('private'))
                print(request.POST.get('domain'))
                name1 = request.POST['name']
                process1 = request.POST['process']
                local_ip1 = request.POST['local_ip']
                local_port1 = request.POST['local_port']
                remote_ip1 = request.POST['remote_ip']
                remote_port1 = request.POST['remote_port']
                protocol1 = request.POST['protocol']
                direction1 = request.POST['direction']
                action1 = request.POST['action']
                type1 = request.POST['type']
                enalbled1 = request.POST['enalbled']
                # same as add
                if not request.POST.get('public') == None:
                    profile1 = 'public'
                else :
                    profile1 = ''

                if not request.POST.get('private') == None:
                    if profile1 == '':
                        profile1 = 'private'
                    else:
                        profile1 +='|private'

                if not request.POST.get('domain') == None:
                    if profile1 == '':
                        profile1 = 'domain'
                    else:
                        profile1 +='|domain'


                # print(profile1)
                redirect_ip1 = request.POST['redirect_ip']
                redirect_port1 = request.POST['redirect_port']
                # same as add
                values_t = {'v1': name1, 'v2': process1, 'v3': local_ip1, 'v4': local_port1, 'v5': remote_ip1,
                            'v6': remote_port1,
                            'v7': protocol1, 'v8': direction1, 'v9': action1, 'v10': type1, 'v11': enalbled1,
                            'v12': profile1,'v13':redirect_ip1,'v14':redirect_port1}

                empty_error = {'error1': '', 'error2': '', 'error3': '', 'error4': '', 'error5': '', 'error6': '',
                               'error7': '',
                               'error8': '', 'error9': '', 'error10': '', 'error11': '', 'error12': '','error13': '','error14': '', }

                values_t, empty_error, ok = check(values_t, empty_error, 2)
                # same as add
                # ok = 1  #
                if ok == 1:
                    # print(1)

                    tmp = web1.models.Course.objects.get(pk=request.session['id_c_c'])

                    if action1 == "redirect":
                        content_all = "name:" + name1 + " process:" + process1 + " local_ip:" + local_ip1 + " local_port:" + local_port1 + " remote_ip:" + remote_ip1 + " remote_port:" + remote_port1 + " protocol:" + protocol1 + " direction:" + direction1 + " action:" + action1 + " type:" + type1 + " enalbled:" + enalbled1 + " profile:" + profile1 + " redirect_ip:" + redirect_ip1 + " redirect_port:" + redirect_port1
                    else:
                        content_all = "name:" + name1 + " process:" + process1 + " local_ip:" + local_ip1 + " local_port:" + local_port1 + " remote_ip:" + remote_ip1 + " remote_port:" + remote_port1 + " protocol:" + protocol1 + " direction:" + direction1 + " action:" + action1 + " type:" + type1 + " enalbled:" + enalbled1 + " profile:" + profile1

                        web1.models.Course.objects.filter(id = request.session['id_c_c']).update(name=name1, process=process1, local_ip=local_ip1,
                                                   local_port=local_port1,
                                                   remote_ip=remote_ip1, remote_port=remote_port1, protocol=protocol1,
                                                   direction=direction1,
                                                   action=action1, type=type1, enalbled=enalbled1, profile=profile1,
                                                   redirect_ip=redirect_ip1, redirect_port=redirect_port1,
                                                   content_all1=content_all,last_change = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+" User:"+request.session['user_name'])

                        web1.models.log.objects.create(operation='Change', user=request.session['user_name'], befor=tmp.content_all1,
                                              after=content_all, id_f=request.session['id_c_c'])

                else:
                    z = {**values_t, **empty_error}
                    return render(request, 'test_info_change_page.html', z)

            else:
                pass
            rule_list = web1.models.Course.objects.all()
            return render(request, 'infor_department_test.html', {'li': rule_list})
        # init get the policy
        rule_list = web1.models.Course.objects.all().filter(id=request.get_full_path().split("id=", 1)[1])
        for li in rule_list:
            name1 = li.name
            process1 = li.process
            local_ip1 = li.local_ip
            local_port1 = li.local_port
            remote_ip1 = li.remote_ip
            remote_port1 = li.remote_port
            protocol1 = li.protocol
            direction1 = li.direction
            action1 = li.action
            type1 = li.type
            enalbled1 = li.enalbled
            profile1 = li.profile
            redirect_ip1 = li.redirect_ip
            redirect_port1 = li.redirect_port
        values = {'v1': name1, 'v2': process1, 'v3': local_ip1, 'v4': local_port1, 'v5': remote_ip1, 'v6': remote_port1,
                  'v7': protocol1, 'v8': direction1, 'v9': action1, 'v10': type1, 'v11': enalbled1, 'v12': profile1,'v13':redirect_ip1,'v14':redirect_port1 }
        print(values['v1'])
        return render(request, 'test_info_change_page.html', values)
    else:
        return redirect('/login')

# main page
def index(request):
    # session'log_info' used in search , must be none if out of search page
    if request.session.get('log_info'):
        request.session.pop('log_info')
    if request.session.get('log_back'):
        request.session.pop('log_back')
    rule_list = web1.models.Department.objects.all().filter(level="1")
    if request.method == "POST":
        rule_list = web1.models.Department.objects.all().filter(level="1")
    # rule_list_1 = web1.models.Course.objects.all()
    # return render(request, 'infor_department_test.html', {'li': rule_list_1})
    # web1.models.Question_2.objects.create(questioner = '1' , title = '2' , question = '3' , question_time = '4')
    # web1.models.Anwser.objects.create(question_id='1', anwser='2', anwser_time='3', respondent_level='4' , respondent_id = '5' , star = '6' , star_guy = '7')
    return render(request,'info_all_department.html',{'li':rule_list})

def index_test(request):
    # session'log_info' used in search , must be none if out of search page
    if request.session.get('log_info'):
        request.session.pop('log_info')
    if request.session.get('log_back'):
        request.session.pop('log_back')
    rule_list = web1.models.Course.objects.all()
    if request.method == "POST":
        rule_list = web1.models.Course.objects.all()
    # rule_list_1 = web1.models.Course.objects.all()
    # return render(request, 'infor_department_test.html', {'li': rule_list_1})
    return render(request,'infor_department_test.html',{'li':rule_list})

def index_QA(request):
    # session'log_info' used in search , must be none if out of search page
    if request.session.get('log_info'):
        request.session.pop('log_info')
    if request.session.get('log_back'):
        request.session.pop('log_back')

    QA_list = web1.models.Question_2.objects.all().order_by('-question_time')
    for item in QA_list:
        item.hot = len(web1.models.Anwser.objects.all().filter(question_id = item.id))
        for item2 in web1.models.Anwser.objects.all().filter(question_id = item.id):
            item.hot = int(item.hot)+int(item2.star)

    if request.method == "POST":
        QA_list = web1.models.Question_2.objects.all().order_by('-question_time')
        for item in QA_list:
            item.hot = len(web1.models.Anwser.objects.all().filter(question_id=item.id))
            for item2 in web1.models.Anwser.objects.all().filter(question_id=item.id):
                item.hot = int(item.hot)+int(item2.star)
    # rule_list_1 = web1.models.Course.objects.all()
    # return render(request, 'infor_department_test.html', {'li': rule_list_1})
    return render(request,'info_Q_A_all.html',{'li':QA_list})

# show one policy
def show(request):
    # confirm login
    if  request.session.get('is_login', None):
        # back
        if 's_back' in request.POST:
            rule_list = web1.models.Department.objects.all().filter(level="1")
            return render(request, 'info_all_department.html', {'li': rule_list})
        # get id
        # request.session['id_c_c'] =request.get_full_path().split("id=", 1)[1]
        # dp = web1.models.Department.objects.get(pk=request.session['id_c_c'])
        idd = request.get_full_path().split("id=", 1)[1]
        dp = web1.models.Department.objects.get(pk=idd)
        print(dp.id_f)
        if dp.id_f == "list":
            dp_list = web1.models.Department.objects.all().filter(super=dp.code)
            return render(request, 'info_all_department.html', {'li': dp_list})
        if dp.id_f == '':
            return render(request, 'NO_file.html')
        l = web1.models.CaseFile.objects.all().filter(id=dp.id_f)
        if len(l)==0:
            return render(request, 'NO_file.html')
        cs_file = web1.models.CaseFile.objects.get(pk=dp.id_f)
        error , name_of_department, pre_course_1, pre_course_1_addi, pre_course_2, pre_course_2_addi, req_course_base, req_course_base_addi, req_course_core, req_course_core_addi, req_course_exp, req_course_exp_addi, ele_course, ele_course_addi, exp_course, exp_course_addi, tb, fun_of_sci_eng, fun_of_sci_eng_addi, Eng, Eng_addi, Ipe, Ipe_addi, Pe, Pe_addi, W_c, W_c_addi = decode_xlx(
            cs_file.file_name)

        #
        print(name_of_department)
        print(pre_course_1)
        print(pre_course_1_addi)
        print(pre_course_2)
        print(pre_course_2_addi)
        print(req_course_base)
        print(req_course_base_addi)
        print(req_course_core)
        print(req_course_core_addi)
        print(req_course_exp)
        print(req_course_exp_addi)
        print(ele_course)
        print(ele_course_addi)
        print(exp_course)
        print(exp_course_addi)
        print(tb)
        print(fun_of_sci_eng)
        print(fun_of_sci_eng_addi)
        print(Eng)
        print(Eng_addi)
        print(Ipe)
        print(Ipe_addi)
        print(Pe)
        print(Pe_addi)
        print(W_c)
        print(W_c_addi)

        id_user = request.session['user_id']
        user = web1.models.User.objects.get(pk = id_user)
        course_list_t = user.course.split('/')
        course_list = []
        for item in course_list_t:
            if item != '':
                course_list.append(item)


        pre_course_1_c = []
        pre_course_2_c = []
        fun_of_sci_eng_c = []
        Eng_c = []
        Ipe_c = []
        Pe_c = []
        W_c_c = []
        req_course_base_c = []
        req_course_core_c = []
        req_course_exp_c = []
        ele_course_c = []
        exp_course_c = []


        for course_code in pre_course_1:
            for tmp in web1.models.Course.objects.all().filter(name_code=course_code):
                c_list = []
                c_list.append(tmp.name_code)
                if tmp.replace_course !='':
                    for item in tmp.replace_course.split('/'):
                        c_list.append(item)
                print(c_list)
                for item in c_list:

                    k_list = item.split('&')
                    print(k_list)
                    ok = 1
                    for iitem in k_list:
                        if iitem not in course_list:
                            ok = 0
                    if ok == 1 :
                        tmp.ok = "PASS"


                pre_course_1_c.append(tmp)

        for course_code in fun_of_sci_eng:
            for tmp in web1.models.Course.objects.all().filter(name_code=course_code):
                c_list = []
                c_list.append(tmp.name_code)
                if tmp.replace_course !='':
                    for item in tmp.replace_course.split('/'):
                        c_list.append(item)

                for item in c_list:
                    k_list = item.split('&')
                    ok = 1
                    for iitem in k_list:
                        if iitem not in course_list:
                            ok = 0
                    if ok == 1 :
                        tmp.ok = "PASS"
                fun_of_sci_eng_c.append(tmp)

        for course_code in pre_course_2:
            for tmp in web1.models.Course.objects.all().filter(name_code=course_code):
                c_list = []
                c_list.append(tmp.name_code)
                if tmp.replace_course !='':
                    for item in tmp.replace_course.split('/'):
                        c_list.append(item)

                for item in c_list:
                    k_list = item.split('&')
                    ok = 1
                    for iitem in k_list:
                        if iitem not in course_list:
                            ok = 0
                    if ok == 1 :
                        tmp.ok = "PASS"
                pre_course_2_c.append(tmp)

        for course_code in req_course_base:
            for tmp in web1.models.Course.objects.all().filter(name_code=course_code):
                c_list = []
                c_list.append(tmp.name_code)
                if tmp.replace_course !='':
                    for item in tmp.replace_course.split('/'):
                        c_list.append(item)

                for item in c_list:
                    k_list = item.split('&')
                    ok = 1
                    for iitem in k_list:
                        if iitem not in course_list:
                            ok = 0
                    if ok == 1 :
                        tmp.ok = "PASS"
                req_course_base_c.append(tmp)

        for course_code in req_course_core:
            for tmp in web1.models.Course.objects.all().filter(name_code=course_code):
                c_list = []
                c_list.append(tmp.name_code)
                if tmp.replace_course !='':
                    for item in tmp.replace_course.split('/'):
                        c_list.append(item)

                for item in c_list:
                    k_list = item.split('&')
                    ok = 1
                    for iitem in k_list:
                        if iitem not in course_list:
                            ok = 0
                    if ok == 1 :
                        tmp.ok = "PASS"
                req_course_core_c.append(tmp)

        for course_code in req_course_exp:
            for tmp in web1.models.Course.objects.all().filter(name_code=course_code):
                c_list = []
                c_list.append(tmp.name_code)
                if tmp.replace_course !='':
                    for item in tmp.replace_course.split('/'):
                        c_list.append(item)

                for item in c_list:
                    k_list = item.split('&')
                    ok = 1
                    for iitem in k_list:
                        if iitem not in course_list:
                            ok = 0
                    if ok == 1 :
                        tmp.ok = "PASS"
                req_course_exp_c.append(tmp)

        for course_code in ele_course:
            for tmp in web1.models.Course.objects.all().filter(name_code=course_code):
                c_list = []
                c_list.append(tmp.name_code)
                if tmp.replace_course !='':
                    for item in tmp.replace_course.split('/'):
                        c_list.append(item)

                for item in c_list:
                    k_list = item.split('&')
                    ok = 1
                    for iitem in k_list:
                        if iitem not in course_list:
                            ok = 0
                    if ok == 1 :
                        tmp.ok = "PASS"
                ele_course_c.append(tmp)

        for course_code in exp_course:
            for tmp in web1.models.Course.objects.all().filter(name_code=course_code):
                c_list = []
                c_list.append(tmp.name_code)
                if tmp.replace_course !='':
                    for item in tmp.replace_course.split('/'):
                        c_list.append(item)

                for item in c_list:
                    k_list = item.split('&')
                    ok = 1
                    for iitem in k_list:
                        if iitem not in course_list:
                            ok = 0
                    if ok == 1 :
                        tmp.ok = "PASS"
                exp_course_c.append(tmp)

        for course_code in Eng:
            for tmp in web1.models.Course.objects.all().filter(name_code=course_code):
                c_list = []
                c_list.append(tmp.name_code)
                if tmp.replace_course !='':
                    for item in tmp.replace_course.split('/'):
                        c_list.append(item)

                for item in c_list:
                    k_list = item.split('&')
                    ok = 1
                    for iitem in k_list:
                        if iitem not in course_list:
                            ok = 0
                    if ok == 1 :
                        tmp.ok = "PASS"
                Eng_c.append(tmp)

        for course_code in Ipe:
            for tmp in web1.models.Course.objects.all().filter(name_code=course_code):
                c_list = []
                c_list.append(tmp.name_code)
                if tmp.replace_course !='':
                    for item in tmp.replace_course.split('/'):
                        c_list.append(item)

                for item in c_list:
                    k_list = item.split('&')
                    ok = 1
                    for iitem in k_list:
                        if iitem not in course_list:
                            ok = 0
                    if ok == 1 :
                        tmp.ok = "PASS"
                Ipe_c.append(tmp)

        for course_code in Pe:
            for tmp in web1.models.Course.objects.all().filter(name_code=course_code):
                c_list = []
                c_list.append(tmp.name_code)
                if tmp.replace_course !='':
                    for item in tmp.replace_course.split('/'):
                        c_list.append(item)

                for item in c_list:
                    k_list = item.split('&')
                    ok = 1
                    for iitem in k_list:
                        if iitem not in course_list:
                            ok = 0
                    if ok == 1 :
                        tmp.ok = "PASS"
                Pe_c.append(tmp)

        for course_code in W_c:
            for tmp in web1.models.Course.objects.all().filter(name_code=course_code):
                c_list = []
                c_list.append(tmp.name_code)
                if tmp.replace_course !='':
                    for item in tmp.replace_course.split('/'):
                        c_list.append(item)

                for item in c_list:
                    k_list = item.split('&')
                    ok = 1
                    for iitem in k_list:
                        if iitem not in course_list:
                            ok = 0
                    if ok == 1 :
                        tmp.ok = "PASS"
                W_c_c.append(tmp)

        rule_list = web1.models.Department.objects.all().filter(level="1")
        print(pre_course_1_c)
        output = {}
        output['pre_course_1'] = pre_course_1_c
        output['pre_course_1_addi'] = pre_course_1_addi
        output['pre_course_2'] = pre_course_2_c
        output['pre_course_2_addi'] = pre_course_2_addi
        output['tb'] = tb
        output['fun_of_sci_eng'] = fun_of_sci_eng_c
        output['fun_of_sci_eng_addi'] = fun_of_sci_eng_addi
        output['Eng'] = Eng_c
        output['Eng_addi'] = Eng_addi
        output["Pe"] = Pe_c
        output["Pe_addi"] = Pe_addi
        output['Ipe'] = Ipe_c
        output['Ipe_addi'] = Ipe_addi
        output['W_c'] = W_c_c
        output['W_c_addi'] = W_c_addi
        output['req_course_base'] = req_course_base_c
        output['req_course_base_addi'] = req_course_base_addi
        output['req_course_core'] = req_course_core_c
        output['req_course_core_addi'] = req_course_core_addi
        output['req_course_exp'] = req_course_exp_c
        output['req_course_exp_addi'] = req_course_exp_addi
        output['ele_course'] = ele_course_c
        output['ele_course_addi'] = ele_course_addi
        output['exp_course'] = exp_course_c
        output['exp_course_addi'] = exp_course_addi
        output['code_p'] = name_of_department
        # output['pre_course_1'] = pre_course_1_c
        # output['pre_course_1'] = pre_course_1_c
        # output['pre_course_1'] = pre_course_1_c
        # output['pre_course_1'] = pre_course_1_c
        # output['pre_course_1'] = pre_course_1_c
        # output['pre_course_1'] = pre_course_1_c
        # output['pre_course_1'] = pre_course_1_c

        return render(request, 'info_one_department.html', output)
    else:
        return redirect('/login')

def download_in_one(request):
    if request.session.get('is_login', None):
        if request.method == "POST":
            code = request.POST['code_p']
            print(code)
            tmp_file_list = web1.models.CaseFile.objects.all().filter(name = code)
            for li in tmp_file_list:
                tmp_file = li.file_name
                response = FileResponse(tmp_file)
                response['Content-Type'] = 'application/octet-stream'
                response['Content-Disposition'] = 'attachment;filename="xlsx_file.xlsx"'
            return response
    else:
        return redirect('/login')

def Coures_show(request):
    if  request.session.get('is_login', None):
        # back
        rule_list = web1.models.Course.objects.all().filter(id=request.get_full_path().split("id=", 1)[1])
        for li in rule_list:

            name1 = li.name
            name_code1 = li.name_code
            credit1 = li.credit
            credit_for_exp1 = li.credit_for_exp
            hours_per_week1 = li.hours_per_week
            Opening_semester1 = li.Opening_semester
            recommended_Opening_semester1 = li.recommended_Opening_semester
            language1 = li.language
            prerequisite_courses1 = li.prerequisite_courses
            department1 = li.department
            replace_course1 = li.replace_course

        values = {'v1': name1, 'v2': name_code1, 'v3': credit1, 'v4': credit_for_exp1, 'v5': hours_per_week1, 'v6': Opening_semester1,
                  'v7': recommended_Opening_semester1, 'v8': language1, 'v9': prerequisite_courses1, 'v10': department1 , 'v11' : replace_course1}
        print(values['v1'])
        return render(request, 'test_info_one.html', values)
    else:
        return redirect('/login')