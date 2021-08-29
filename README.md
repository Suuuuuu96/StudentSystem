# 中国农业大学学生管理系统
## 简介
本系统是一个基于Django的中国农业大学学生管理系统。
本系统是针对学校的大量学生事务工作而开发的管理软件，实现了学生信息的录入与查询功能、课程添加与选课功能、班级的添加修改功能、用户注册登录功能等等，能高效率、规范化地管理大量的学务信息。
## 使用的主要技术
* Django：主体框架，用于接收客户端的请求并调用相关函数、返回资源等等；
* MySQL：用于学生、班级、课程、选课表等表格型数据的管理，使用Django ORM对数据库进行增删改查操作；
* Redis：用于统计各用户每天的登录和输入密码错误情况，限制多次登录失败用户当天的访问，防止暴力破解密码。
* layui和X-admin：前端框架，用于接收后端的数据并渲染、向用户展示页面。
## 主要界面展示

1、打开网站，首先看到的是登录界面。如果没有注册，也可以先在http://127.0.0.1:8000/ 页面找到相应按钮进行注册。
![image](https://github.com/Suuuuuu96/StudentSystem/blob/main/img/p1.png)

2、如果一个账号一天之内输入密码错误次数超过5次，则该用户当天不可以再登录。
![image](https://github.com/Suuuuuu96/StudentSystem/blob/main/img/p2.png)

3、登录成功后即可查看系统的主页面并使用其主要功能，如学生管理功能、班级管理功能和课程管理功能。此处以学生查找功能为例：查找名为“偶素”的学生。
![image](https://github.com/Suuuuuu96/StudentSystem/blob/main/img/p3.png)

4、系统使用MySQL作为数据库管理软件，打开HeidiSQL可以看到对应数据表中名为“偶素”的学生存在，且其ID为1。
![image](https://github.com/Suuuuuu96/StudentSystem/blob/main/img/p4.png)

5、点击提交，下方出现查找结果。可以发现该结果与数据库数据一致。
![image](https://github.com/Suuuuuu96/StudentSystem/blob/main/img/p5.png)
