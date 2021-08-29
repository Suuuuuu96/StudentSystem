"""StudentSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views
import redis
urlpatterns = [
    url(r'^$',views.Main),
    url(r'^add_student$',views.add_student),
    url(r'^welcome.html$',views.welcome),
    url(r'^welcome$',views.welcome),
    url(r'^register$',views.register),
    url(r'^login$',views.login),
    url(r'^Login_check$',views.Login_check),
    url(r'^logout$',views.logout),
    url(r'^add_class$',views.add_class),
    url(r'^add_course$',views.add_course),
    url(r'^find_student$',views.find_student),
    url(r'^delete_student$',views.delete_student),
    url(r'^course_selection$',views.course_selection),


    #url(r'^admin/', admin.site.urls),
    #url(r'', admin.site.urls),
]


#python manage.py runserver
#django-admin.py startapp NewModel
#python manage.py migrate
#python manage.py makemigrations NewModel
#python manage.py migrate NewModel
#css文件需要放在statics文件夹里面并注册才能使用

# rep=redirect('/Login_check');
# rep.set_cookie("is_Login", True);
# return rep
# 第一次设置cookie之后，必须返回给客户端、让客户端保存cookie
# 之后客户端再发消息到服务器就自动携带cookie