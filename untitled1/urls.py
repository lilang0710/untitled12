"""untitled1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

'''from django.contrib import admin
from django.urls import path
from untitled1 import index
from django.conf.urls import url
from django.conf.urls import *
from li.views import say
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index.index),
    url(r'^li/',say),
    url(r'^admin/',admin.site.urls),

]'''
'''
from django.conf.urls import *
from django.contrib import admin
admin.autodiscover()
urlpatterns = [
    url(r'^admin/', admin.site.urls),
]'''
"""Django01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
'''
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.conf.urls import url
from li import views
from li.views import v
import pymysql
#登录页面
def login(request):
    #指定要访问的页面，render的功能：讲请求的页面结果提交给客户端
    return render(request,'login.html')
#注册页面
def regiter(request):
    return render(request,'regiter.html')
#定义一个函数，用来保存注册的数据
def save(request):
    has_regiter = 0#用来记录当前账号是否已存在，0：不存在 1：已存在
    a = request.GET#获取get()请求
    #print(a)
    #通过get()请求获取前端提交的数据
    userName = a.get('username')
    passWord = a.get('password')
    #print(userName,passWord)
    #连接数据库
    db = pymysql.connect('127.0.0.1','root','lilang1314','db2')
    #创建游标
    cursor = db.cursor()
    #SQL语句
    sql1 = 'select * from user1'
    #执行SQL语句
    cursor.execute(sql1)
    #查询到所有的数据存储到all_users中
    all_users = cursor.fetchall()
    i = 0
    while i < len(all_users):
        if userName in all_users[i]:
            ##表示该账号已经存在
            has_regiter = 1

        i += 1
    if has_regiter == 0:
        # 将用户名与密码插入到数据库中
        sql2 = 'insert into user1(username,password) values(%s,%s)'
        cursor.execute(sql2,(userName,passWord))
        db.commit()
        cursor.close()
        db.close()
        return HttpResponse('注册成功')
    else:

        cursor.close()
        db.close()
        return HttpResponse('该账号已存在')

def query(request):
    a = request.GET
    userName = a.get('username')
    passWord = a.get('password')
    user_tup = (userName,passWord)
    db = pymysql.connect('127.0.0.1','root','lilang1314','db2')
    cursor = db.cursor()
    sql = 'select * from user1'
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
   #     return HttpResponse('http://127.0.0.1:8000/login/')


        return render(request, 'regiter.html')
    else:
        return HttpResponse('用户名或密码有误')
urlpatterns = [
    path('admin/', admin.site.urls),#系统默认创建的
    path('login/',login),#用于打开登录页面
    path('regiter/',regiter),#用于打开注册页面
    path('regiter/save',save),#输入用户名密码后交给后台save函数处理
    path('login/query',query),#输入用户名密码后交给后台query函数处理
    url('',views.index)，

   # url(r'^v',v)
]'''
from django.conf.urls import include,url
from django.contrib import admin
from li import views
from django.urls import path


'''urlpatterns = [
    url(r'^zhong/',include('zhong.urls'),
    url(r'^admin/',admin.site.urls),
    path('admin/', admin.site.urls),
]'''
urlpatterns =  [
  #  path('',views.index),
    path('admin/', admin.site.urls),
    path('show/', views.list),
    path('u/',views.u),

    path('',views.login),#用于打开登录页面
    path('regiter/',views.regiter),#用于打开注册页面
    path('regiter/save',views.save),#输入用户名密码后交给后台save函数处理
    path('change/',views.change),
    path('change/changes',views.changes),
    path('query',views.query),#输入用户名密码后交给后台query函数处理
    path('password/', views.listp),
    path('open/', views.listo),
    path('control/', views.listc),
    path('employee/', views.liste),
]
'''urlpatterns= [
    url(r'^zhong/', include('zhong.urls'),
    url(r'^admin/', admin.site.urls),
]'''
