# Generated by Django 2.0.5 on 2018-07-12 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20180711_1840'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=16, verbose_name='操作用户')),
                ('remote_ip', models.GenericIPAddressField(verbose_name='操作用户IP')),
                ('content', models.CharField(max_length=100, verbose_name='操作内容')),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='操作时间')),
            ],
        ),
    ]
