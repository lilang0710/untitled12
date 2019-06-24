'''#from django.short time
# Create youtcuts import render
# from django.shortcuts import HttpResponse
# imporr views here.
def say(request):
    s='Hello World!'
    nt=time.localtime()
    ft="%Y-%m-%d %H:%M:%S"
    current_time=time.strftime(ft,nt)
    html='<html><head></head><body><h1> %s </h1><p> %s </p></body></html>'%(s,current_time)
    return HttpResponse()'''
#coding=UTF-8
#-*-coding:utf-8 -*-
#from django.db import
from django.http import HttpResponse
from django.urls import path
from django.shortcuts import render
import pymysql
from li.models import DepartmentInformation
from li.models import AccessControlEquipment
from li.models import EmployeeInformation
from li.models import OpenRecordThroughAccessControl
from li.models import User
#from _future_ import unicode_literals
#from li.models import DepatmentInformationTable
from django.shortcuts import render
from django.shortcuts import HttpResponse
#from models import DepartmentInformation
def login(request):
    #指定要访问的页面，render的功能：讲请求的页面结果提交给客户端
    return render(request,'login.html')
#注册页面
def regiter(request):
    return render(request,'regiter.html')
def change(request):
    return render(request,'change.html')
#定义一个函数，用来保存注册的数据
def save(request):
    has_regiter = 0#用来记录当前账号是否已存在，0：不存在 1：已存在
    a = request.GET#获取get()请求
    #print(a)
    #通过get()请求获取前端提交的数据
    MARK_NO = a.get('mark_no')
    PASSWORD1 = a.get('password1')
    PASSWORD2 = a.get('password2')
    #print(userName,passWord)
    #连接数据库
    db = pymysql.connect('127.0.0.1','root','lilang1314','ll')
    #创建游标
    cursor = db.cursor()
    #SQL语句
    sql1 = 'select * from user'
    #执行SQL语句
    cursor.execute(sql1)
    #查询到所有的数据存储到all_users中
    all_users = cursor.fetchall()
    i = 0
    while i < len(all_users):
        if MARK_NO in all_users[i]:
            ##表示该账号已经存在
            has_regiter = 1

        i += 1
    if has_regiter == 0:
        if PASSWORD1 == PASSWORD2:
        # 将用户名与密码插入到数据库中
          sql2 = 'insert into user(mark_no,password) values(%s,%s)'
          cursor.execute(sql2,(MARK_NO,PASSWORD1))
          db.commit()
          cursor.close()
          db.close()
          return HttpResponse('注册成功')
        else:
          return HttpResponse('两次密码输入不一致，请重新注册')
    else:

        cursor.close()
        db.close()
        return HttpResponse('该账号已存在')
def changes(request):
    a = request.GET
    #NEWPASSWORD = a.get('newpassword')
    MARK_NO = a.get('mark_no')
    OLDPASSWORD = a.get('oldpassword')
    NEWPASSWORD = a.get('newpassword')
    NEWPASSWORD2 =a.get('newpassword2')
    user_tup = (MARK_NO,OLDPASSWORD)

    db = pymysql.connect('127.0.0.1','root','lilang1314','ll')
    cursor = db.cursor()
    sql = 'select * from user'
    cursor.execute(sql)
    all_users = cursor.fetchall()
   # print(all_users)

    cursor.close()
    db.close()
    has_user = 0
    i = 0
    while i < len(all_users):
        if user_tup == all_users[i]:
            has_user = 1
        i += 1
    if has_user == 1:
         if NEWPASSWORD == NEWPASSWORD2:
     #  return path('http://127.0.0.1:8000/show/')
      #  return render(request,'zhujiemian.html')
     #sql2 = 'insert into user(mark_no,password) values(%s,%s)'
    # cursor.execute(sql2, (MARK_NO, PASSWORD))
           db = pymysql.connect('127.0.0.1', 'root', 'lilang1314', 'll')
           cursor = db.cursor()

     #sql3=' update user set password= where mark_no=MARK_NO'
     #try:
     #cursor.execute(sql3)
           updatesql3='update user set password=%s  where mark_no=%s'
     #updateParam=('NEWPASSWORD','')
           cursor.execute(updatesql3,(NEWPASSWORD,MARK_NO,))
           db.commit()
    # except:
    #db.rollback()
           cursor.close()
           db.close()
           return HttpResponse('修改密码成功')
           #return render(request,list())
         else:
           return HttpResponse('两次密码不一致，请重新输入')
    else:
        return HttpResponse('用户名或密码有误')

def query(request):
    a = request.GET
    MARK_NO = a.get('mark_no')
    PASSWORD = a.get('password')
    user_tup = (MARK_NO,PASSWORD)
    db = pymysql.connect('127.0.0.1','root','lilang1314','ll')
    cursor = db.cursor()
    sql = 'select * from user '
    cursor.execute(sql)
    all_users = cursor.fetchall()
   # print(all_users)
    cursor.close()
    db.close()
    has_user = 0
    i = 0
    while i < len(all_users):
        if user_tup == all_users[i]:
            has_user = 1
        i += 1
    if has_user == 1:
     #  return path('http://127.0.0.1:8000/show/')
        return render(request,'zhujiemian.html')

           #return render(request,list())
    else:
        return HttpResponse('用户名或密码有误')
def u(request):
    '''people_list=DepatmentInformationTable.objects.get(dept_code=100000)
    #people_list=get_dept.dept_code
    return render(request, 'show.html', {"people_list":people_list})
    return HttpResponse(1)'''
    people_list = models.DepartmentInformationTable.objects.all()
    return render(request, 'show.html', {"people_list": people_list})
def v(request):
    new_user=DepartmentInformation(
      dept_code='100002',
      dept_name='sd',
      dept_type='e'
    )
    new_user.save()
    return HttpResponse()
def index(request):
    return HttpResponse(u"hellao 中 、！")
def list(request):
    people_list=DepartmentInformation.objects.all()
    return render(request,'show.html',{"people_list":people_list})
def listp(request):
    pass_word=User.objects.all()
    return render(request,'password.html',{"pass_word":pass_word})
def listc(request):
    control_list=AccessControlEquipment.objects.all()
    return render(request,'control.html',{"control_list":control_list})
def liste(request):
    employee_list=EmployeeInformation.objects.all()
    return render(request,'employee.html',{"employee_list":employee_list})
def listo(request):
    open_list=OpenRecordThroughAccessControl.objects.all()
    return render(request,'open.html',{"open_list":open_list})
