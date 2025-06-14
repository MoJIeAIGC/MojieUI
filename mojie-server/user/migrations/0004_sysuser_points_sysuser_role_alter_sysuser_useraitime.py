# Generated by Django 5.1.7 on 2025-04-06 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_sysuser_useraitime'),
    ]

    operations = [
        migrations.AddField(
            model_name='sysuser',
            name='points',
            field=models.PositiveIntegerField(default=0, verbose_name='积分'),
        ),
        migrations.AddField(
            model_name='sysuser',
            name='role',
            field=models.CharField(max_length=255, null=True, verbose_name='月卡状态'),
        ),
        migrations.AlterField(
            model_name='sysuser',
            name='userAITime',
            field=models.CharField(max_length=255, verbose_name='时间'),
        ),
    ]
