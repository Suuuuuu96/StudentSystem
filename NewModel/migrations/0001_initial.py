# Generated by Django 3.2.5 on 2021-07-24 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='class_grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='班级名')),
            ],
        ),
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='课程名称')),
                ('score', models.IntegerField(blank=True, verbose_name='学分')),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='学生姓名')),
                ('sex', models.CharField(max_length=50, verbose_name='性别')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('address', models.CharField(blank=True, max_length=250, verbose_name='家庭住址')),
                ('remarks', models.TextField(blank=True, verbose_name='备注')),
                ('Class_Grade', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='NewModel.class_grade')),
            ],
        ),
        migrations.CreateModel(
            name='student_course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='选课记录名')),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='NewModel.course')),
                ('Student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='NewModel.student')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(through='NewModel.student_course', to='NewModel.course'),
        ),
    ]
