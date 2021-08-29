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

![image](https://github.com/Suuuuuu96/StudentSystem/blob/main/img/p1.png)

![image](https://github.com/Suuuuuu96/StudentSystem/blob/main/img/p2.png)

![image](https://github.com/Suuuuuu96/StudentSystem/blob/main/img/p3.png)

![image](https://github.com/Suuuuuu96/StudentSystem/blob/main/img/p4.png)

![image](https://github.com/Suuuuuu96/StudentSystem/blob/main/img/p5.png)
