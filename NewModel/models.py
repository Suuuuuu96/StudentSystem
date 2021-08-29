from django.db import models
# 这里一个类就代表一个数据库的表
# Create your models here.

class class_grade(models.Model):
    name = models.CharField(verbose_name='班级名', max_length=100)

class course(models.Model):
    name = models.CharField(verbose_name='课程名称', max_length=50,blank=True)
    score = models.IntegerField(verbose_name='学分', blank=True)

class student(models.Model):
    name = models.CharField(verbose_name='学生姓名', max_length=50)
    sex = models.CharField(verbose_name='性别', max_length=50)
    age = models.IntegerField(verbose_name='年龄')
    address = models.CharField(verbose_name='家庭住址', max_length=250, blank=True)
    #enter_date = models.DateField(verbose_name='入学时间')
    remarks = models.TextField(verbose_name='备注', blank=True)
    Class_Grade=models.ForeignKey("class_grade", on_delete=models.CASCADE,null=True)
    courses=models.ManyToManyField(course,through='student_course')

class student_course(models.Model):
    Student=models.ForeignKey(student,on_delete=models.PROTECT)
    Course=models.ForeignKey(course,on_delete=models.PROTECT)
    remarks=models.CharField(verbose_name='选课记录名', max_length=50)



