from django.db.models import ManyToOneRel, ManyToManyRel, ManyToManyField
from django.http import HttpResponse
from django.shortcuts import render,redirect
from NewModel import models
import os
import traceback
from django.contrib import auth
from django.core.cache import cache
# 认证模块
from django.contrib import auth
# 对应数据库
from django.contrib.auth.models import User
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import redis
#from utils.redis_pool import POOL
def Main(request):
    IsLogin=False
    #IsLogin=request.COOKIES.get('is_Login')
    if request.COOKIES.get('is_Login'):
        IsLogin=True
    return render(request,os.path.join(BASE_DIR , r'templates\X-admin\index.html'),{'IsLogin':IsLogin})
def welcome(request):
    print(request)
    if request.POST:
        print(request.POST['username'])
    return HttpResponse('<p align="center">欢迎来到中国农业大学学生管理系统！</p>')
    #return render(request,os.path.join(BASE_DIR , r'templates\X-admin\welcome.html'))

def add_student(request):

    #cache.set('mykey','abx');    print(cache.get('k1'));

    #allStudent = models.student.objects.all()
    #print(allStudent,type(allStudent))
    namelist=[]
    for i in models.student._meta.get_fields():
        if type(i)!=ManyToOneRel and type(i)!=ManyToManyRel \
                and type(i)!=ManyToManyField:
            namelist.append(i.name)
        #print(i.verbose_name,i.name,type(i),type(type(i)))
    # QuerySet类型，类似于list，访问 url 时数据显示在命令行窗口中。
    print(namelist,models.student._meta.get_fields())
    #books = models.student.objects.create(name="如来神掌",age=22)
    #print(models.UserInfo.objects.get(id=books.id).values('user'))
    #print(books.id,books.values('age'))
    notice=''
    if request.POST:
        try:
            temp=request.POST.dict()
            del temp['csrfmiddlewaretoken']
            del temp['id']
            temp['Class_Grade_id']=round(float(temp['Class_Grade']))
            del temp['Class_Grade']
            newStudent=models.student.objects.create(**temp)
            notice='成功新增一个学生！该学生id为'+str(newStudent.id)+'。'
        except(Exception):
            #print('{0}'.format(Exception))
            traceback.print_exc()
            notice='新增学生失败！'
    return render(request,
                  os.path.join(BASE_DIR , r'templates\X-admin\add_student.html'),
                  {'namelist':namelist,'notice':notice})

def find_student(request):
    namelist=[]
    for i in models.student._meta.get_fields():
        if type(i)!=ManyToOneRel and type(i)!=ManyToManyRel \
                and type(i)!=ManyToManyField:
            namelist.append(i.name)

    # QuerySet类型，类似于list，访问 url 时数据显示在命令行窗口中。
    #print(namelist,models.student._meta.get_fields())

    notice=''
    if request.POST:
        try:
            temp=request.POST.dict()
            temp0=list(temp.keys())
            for i in temp0:
                if not temp[i]:
                    del temp[i]
            del temp['csrfmiddlewaretoken']
            #del temp['id']
            if 'Class_Grade' in temp:
                temp['Class_Grade_id']=round(float(temp['Class_Grade']))
                del temp['Class_Grade']


            #newStudent=models.student.objects.create(**temp)
            result = models.student.objects.filter(**temp)
            re=[]
            for i in result:
                re.append(i.id)
            notice='符合条件的学生的ID是：'+str(re)+'。'
        except(Exception):
            #print('{0}'.format(Exception))
            traceback.print_exc()
            notice='查找失败！'
    return render(request,
                  os.path.join(BASE_DIR , r'templates\find_student.html'),
                  {'namelist':namelist,'notice':notice})

def delete_student(request):
    namelist=[]
    for i in models.student._meta.get_fields():
        if type(i)!=ManyToOneRel and type(i)!=ManyToManyRel \
                and type(i)!=ManyToManyField:
            namelist.append(i.name)

    notice=''
    if request.POST:
        try:
            temp=request.POST.dict()
            temp0=list(temp.keys())
            for i in temp0:
                if not temp[i]:
                    del temp[i]
            del temp['csrfmiddlewaretoken']
            #del temp['id']
            if 'Class_Grade' in temp:
                temp['Class_Grade_id']=round(float(temp['Class_Grade']))
                del temp['Class_Grade']


            result = models.student.objects.filter(**temp).delete()

            notice='已删除符合条件的'+str(result[0])+'个学生。'
        except(Exception):
            #print('{0}'.format(Exception))
            traceback.print_exc()
            notice='删除失败！'
    return render(request,
                  os.path.join(BASE_DIR , r'templates\delete_student.html'),
                  {'namelist':namelist,'notice':notice})

def register(request):
    status=request.COOKIES.get('is_Login')
    print('status!',status)
    if status:
        return redirect('/')#访问注册界面时，如果用户已经登录则回主页
    notice=''
    if request.POST:
        try:
            User.objects.create_user(username=request.POST['u0'],password=request.POST['p0'])
            notice='注册成功，用户名为：'+request.POST['u0']+'。'
        except(Exception):
            traceback.print_exc()
            notice='注册失败！'
    return render(request,'register.html',{'notice':notice})

def login(request):

    #print(conn.get('age'))
    status=request.COOKIES.get('is_Login')
    if status:
        return redirect('/') #访问登录界面时，如果用户已经登录则回主页
    #return redirect('/')
    notice='未能成功登录！'
    if request.method=='GET' or request.POST['username']=='':
        return render(request,r'X-admin\login.html')
    POOL = redis.ConnectionPool(host='127.0.0.1', port=6379,password='')
    conn = redis.Redis(connection_pool=POOL)
    num=conn.get(request.POST['username'])
    if num:
        pass
    else:
        import time
        t = time.localtime()
        Remaining_time=24*60*60-t.tm_hour*60*60+t.tm_min*60+t.tm_sec
        conn.set(request.POST['username'], 0,ex=Remaining_time)
        #conn.expire(request.POST['username'],Remaining_time)
        num=conn.get(request.POST['username'])
    Threshold=4 #错误阈值
    if int(num)>Threshold:
        Remaining_time=int(conn.ttl(request.POST['username']))
        print(Remaining_time,type(Remaining_time))
        notice='该账户今日输入密码错误已达到'+str(int(num))+'次，今日内不可再登陆！'\
               +str(Remaining_time)+'秒后解除限制。'
        return render(request,r'X-admin\login.html',{'notice':notice})
    user_obj=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
    if not user_obj:
        conn.incr(request.POST['username'])
        pass;
        #return render(request,r'X-admin\login.html',{'notice':notice})
    else:
        auth.login(request,user_obj)
        print(user_obj.username,'已成功登录。')
        #path=request.GET.get('next') or '/welcome'
        #if request.GET['next']:path=request.GET['next']
        #rep=redirect('/login')
        rep=redirect('/')

        rep.set_cookie("is_Login", True)
        return rep
        #return redirect(path)
    num=int(conn.get(request.POST['username']))
    if num>=3:
        notice='未能成功登录！该账户今日输入密码错误已达到'+str(num)+'次。错误次数达到'\
               +str(Threshold+1)+'次后则今日内不可再登陆。'
    return render(request,r'X-admin\login.html',{'notice':notice})

def logout(request):
    rep=redirect('/')
    rep.delete_cookie('is_Login')
    #rep.set_cookie("is_Login", False)
    return rep

def Login_check(request):
    status=request.COOKIES.get('is_Login')
    print('status',status)
    notice=''
    print(request.POST.get("username"))
    if status:
        notice='已登录。'
        return render(request,'Login_check.html',{'notice':notice})
        return HttpResponse("<p>已登录。</p>")
    else :
        notice='未登录。'
        return render(request,'Login_check.html',{'notice':notice})
        return HttpResponse("<p>未登录。</p>")

def add_class(request):

    namelist=[]
    for i in models.class_grade._meta.get_fields():
        if type(i)!=ManyToOneRel:
            namelist.append(i.name)
        #print(i.verbose_name,i.name,type(i),type(type(i)))
    # QuerySet类型，类似于list，访问 url 时数据显示在命令行窗口中。
    #print(namelist,models.class_grade._meta.get_fields())
    notice=''
    if request.POST:
        try:
            temp=request.POST.dict()
            del temp['csrfmiddlewaretoken']
            del temp['id']
            newClass=models.class_grade.objects.create(**temp)
            notice='成功新增一个班级！该班级id为'+str(newClass.id)+'。'
        except(Exception):
            #print('{0}'.format(Exception))
            traceback.print_exc()
            notice='新增班级失败！'
    return render(request,
                  os.path.join(BASE_DIR , r'templates\add_class.html'),
                  {'namelist':namelist,'notice':notice})

def add_course(request):
    namelist=[]
    for i in models.course._meta.get_fields():
        if type(i)!=ManyToOneRel and type(i)!=ManyToManyRel:
            namelist.append(i.name)
        #print(i.verbose_name,i.name,type(i),type(type(i)))
    # QuerySet类型，类似于list，访问 url 时数据显示在命令行窗口中。
    #print(namelist,models.course._meta.get_fields())
    notice=''
    if request.POST:
        try:
            temp=request.POST.dict()
            del temp['csrfmiddlewaretoken']
            del temp['id']
            newCourse=models.course.objects.create(**temp)
            notice='成功新增一个课程！该班级id为'+str(newCourse.id)+'。'
        except(Exception):
            #print('{0}'.format(Exception))
            traceback.print_exc()
            notice='新增课程失败！'
    return render(request,
                  os.path.join(BASE_DIR , r'templates\add_course.html'),
                  {'namelist':namelist,'notice':notice})

def course_selection(request):
    namelist=[]
    for i in models.student_course._meta.get_fields():
        #if type(i)!=ManyToOneRel and type(i)!=ManyToManyRel:
        namelist.append(i.name)
        #print(i.verbose_name,i.name,type(i),type(type(i)))
    # QuerySet类型，类似于list，访问 url 时数据显示在命令行窗口中。
    #print(namelist,models.course._meta.get_fields())
    notice=''
    if request.POST:
        try:
            temp=request.POST.dict()
            del temp['csrfmiddlewaretoken']
            del temp['id']
            if 'Course' in temp:
                temp['Course_id']=round(float(temp['Course']))
                del temp['Course']
            if 'Student' in temp:
                temp['Student_id']=round(float(temp['Student']))
                del temp['Student']
            newSC=models.student_course.objects.create(**temp)
            notice='成功选课！学生id为'+str(temp['Student_id'])\
                   +'，课程id为'+str(temp['Course_id'])+'。'
        except(Exception):
            #print('{0}'.format(Exception))
            traceback.print_exc()
            notice='选课失败！'
    return render(request,
                  os.path.join(BASE_DIR , r'templates\course_selection.html'),
                  {'namelist':namelist,'notice':notice})



