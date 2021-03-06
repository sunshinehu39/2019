# Generated by Django 2.0.4 on 2018-12-30 15:45

from django.db import migrations, models
import django.db.models.deletion
import system.storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='日程', max_length=8, verbose_name='类型')),
                ('start_time', models.DateTimeField(blank=True, null=True, verbose_name='开始时间')),
                ('stop_time', models.DateTimeField(blank=True, null=True, verbose_name='截止时间')),
                ('work', models.CharField(default='休息', max_length=100, verbose_name='事项')),
                ('money', models.IntegerField(default=0, verbose_name='金额')),
                ('remind_time', models.DateTimeField(blank=True, null=True, verbose_name='提醒时间')),
                ('done', models.BooleanField(default=False, verbose_name='是否完成')),
                ('if_important', models.BooleanField(default=False, verbose_name='是否重要')),
            ],
            options={
                'verbose_name': '日记',
                'verbose_name_plural': '日记',
                'ordering': ['stop_time'],
            },
        ),
        migrations.CreateModel(
            name='Dream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fid', models.IntegerField(verbose_name='帮派编号')),
                ('mid', models.IntegerField(default=0, verbose_name='江湖编号')),
                ('name', models.CharField(default='路人', max_length=18, verbose_name='江湖名')),
                ('type', models.CharField(max_length=6, verbose_name='类型')),
                ('dream', models.TextField(blank=True, max_length=400, null=True, verbose_name='梦想')),
                ('state', models.TextField(blank=True, max_length=200, null=True, verbose_name='现状')),
                ('rate', models.CharField(blank=True, default=0, max_length=6, null=True, verbose_name='圆梦进度')),
            ],
            options={
                'verbose_name': '梦想进度表',
                'verbose_name_plural': '梦想进度表',
            },
        ),
        migrations.CreateModel(
            name='Faction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fid', models.IntegerField(verbose_name='帮派编号')),
                ('name', models.CharField(max_length=8, verbose_name='帮派名')),
                ('photo', models.ImageField(blank=True, default='dosjh/door/逍遥派.jpg', null=True, upload_to='dosjh/door', verbose_name='帮派配图')),
            ],
            options={
                'verbose_name': '帮派',
                'verbose_name_plural': '帮派',
                'ordering': ['fid'],
            },
        ),
        migrations.CreateModel(
            name='Fav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(verbose_name='年')),
                ('month', models.IntegerField(verbose_name='月')),
                ('goal', models.CharField(max_length=80, verbose_name='目标')),
                ('done', models.BooleanField(default=False, verbose_name='是否完成')),
            ],
            options={
                'verbose_name': '月度目标',
                'verbose_name_plural': '月度目标',
            },
        ),
        migrations.CreateModel(
            name='Img2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, storage=system.storage.ImageStorage(), upload_to='img/%Y/%m/%d', verbose_name='配图')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='路人', max_length=18, verbose_name='江湖名')),
                ('truename', models.CharField(default='未备注', max_length=18, verbose_name='真实姓名')),
                ('password', models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='江湖口令')),
                ('fid', models.IntegerField(default=0, verbose_name='门派编号')),
                ('mid', models.IntegerField(default=0, verbose_name='派内编号')),
                ('wxid', models.CharField(blank=True, max_length=60, null=True, verbose_name='微信id')),
                ('nickName', models.CharField(blank=True, max_length=100, null=True, verbose_name='微信昵称')),
                ('avatarUrl', models.URLField(blank=True, null=True, verbose_name='微信头像')),
                ('gender', models.CharField(choices=[('1', '男'), ('2', '女')], default='2', max_length=4, verbose_name='性 别')),
            ],
            options={
                'verbose_name': '成员',
                'verbose_name_plural': '成员',
            },
        ),
        migrations.CreateModel(
            name='Plansum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(verbose_name='年')),
                ('plan', models.TextField(blank=True, max_length=100000, null=True, verbose_name='年度计划')),
                ('summary', models.TextField(blank=True, max_length=100000, null=True, verbose_name='年度总结')),
                ('M_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dosjh.Member', verbose_name='江湖名')),
            ],
            options={
                'verbose_name': '年度计划总结',
                'verbose_name_plural': '年度计划总结',
            },
        ),
        migrations.CreateModel(
            name='Read',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('M_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dosjh.Member', verbose_name='已阅人')),
            ],
        ),
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pubtime', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('type', models.CharField(choices=[('人脉', '人脉'), ('信息', '信息'), ('闲置', '闲置')], default='信息', max_length=8, verbose_name='类型')),
                ('title', models.CharField(max_length=60, verbose_name='标题')),
                ('content', models.TextField(blank=True, max_length=100000, null=True, verbose_name='内容')),
                ('imglist', models.TextField(blank=True, default='', max_length=1000, null=True, verbose_name='配图')),
                ('tag', models.CharField(blank=True, max_length=20, null=True, verbose_name='标签')),
                ('favnum', models.IntegerField(default=0, verbose_name='点赞数')),
                ('favlist', models.TextField(blank=True, default='', max_length=100, null=True, verbose_name='收藏人列表')),
                ('M_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dosjh.Member', verbose_name='分享人')),
            ],
            options={
                'verbose_name': '分享',
                'verbose_name_plural': '分享',
            },
        ),
        migrations.AddField(
            model_name='read',
            name='S_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dosjh.Share', verbose_name='分享编号'),
        ),
        migrations.AddField(
            model_name='goal',
            name='M_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dosjh.Member', verbose_name='江湖名'),
        ),
        migrations.AddField(
            model_name='fav',
            name='M_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dosjh.Member', verbose_name='收藏人'),
        ),
        migrations.AddField(
            model_name='fav',
            name='S_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dosjh.Share', verbose_name='分享编号'),
        ),
        migrations.AddField(
            model_name='diary',
            name='M_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dosjh.Member', verbose_name='江湖名'),
        ),
    ]
