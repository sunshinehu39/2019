from django.db import models

# 数据表建模：帮派
class Faction(models.Model):
    fid = models.IntegerField(verbose_name='帮派编号')
    name = models.CharField(verbose_name='帮派名', max_length=8)
    photo = models.ImageField(verbose_name='帮派配图', upload_to='dosjh/door',default='dosjh/door/逍遥派.jpg',blank=True, null=True)

    class Meta:
        verbose_name = '帮派'
        verbose_name_plural = verbose_name
        ordering = ['fid']

    def __str__(self):
        return self.name

# 数据表建模：成员
class Member(models.Model):
    name = models.CharField(verbose_name='江湖名', default='路人',max_length=18)
    truename = models.CharField(verbose_name='真实姓名', default='未备注',max_length=18)
    password = models.CharField(verbose_name='江湖口令',max_length=20,blank=True, null=True,unique=True)
    fid = models.IntegerField(verbose_name='门派编号',default=0)
    mid = models.IntegerField(verbose_name='派内编号',default=0)

    wxid = models.CharField(verbose_name='微信id', max_length=60,blank=True, null=True)
    nickName = models.CharField(verbose_name='微信昵称', max_length=100,blank=True, null=True)
    avatarUrl = models.URLField(verbose_name='微信头像', max_length=200,blank=True, null=True)

    gender=models.CharField(verbose_name='性 别',default='2',max_length=4,choices=(("1", u"男"), ("2", u"女")))

    class Meta:
        verbose_name = '成员'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 数据表建模：年度计划总结
class Plansum(models.Model):
    M_id = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name='江湖名')
    year = models.IntegerField(verbose_name='年')
    plan = models.TextField(verbose_name='年度计划', max_length=100000, blank=True, null=True)
    summary = models.TextField(verbose_name='年度总结', max_length=100000, blank=True, null=True)

    class Meta:
        verbose_name = '年度计划总结'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.plan

# 数据表建模：目标
class Goal(models.Model):
    M_id = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name='江湖名')
    year = models.IntegerField(verbose_name='年')
    month = models.IntegerField(verbose_name='月')
    goal = models.CharField(verbose_name='目标', max_length=80)
    done = models.BooleanField(verbose_name='是否完成',default=False)

    class Meta:
        verbose_name = '月度目标'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goal

# 数据表建模：日程
class Diary(models.Model):
    M_id = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name='江湖名')
    type = models.CharField(verbose_name='类型',max_length=8,default='日程')
    start_time = models.DateTimeField(verbose_name='开始时间',blank=True, null=True)
    stop_time = models.DateTimeField(verbose_name='截止时间',blank=True, null=True)
    work = models.CharField(verbose_name='事项',max_length=100,default='休息')
    money = models.IntegerField(verbose_name='金额',default=0)
    remind_time = models.DateTimeField(verbose_name='提醒时间',blank=True, null=True)
    done = models.BooleanField(verbose_name='是否完成',default=False)
    if_important = models.BooleanField(verbose_name='是否重要',default=False)

    class Meta:
        verbose_name = '日程'
        verbose_name_plural = verbose_name
        ordering = ['stop_time']

    def __str__(self):
        return self.work

# 数据表建模：日记
class Diarydetail(models.Model):
    M_id = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name='江湖名')
    type = models.CharField(verbose_name='类型',max_length=16,default='个人日记')
    pubtime = models.DateField(verbose_name='发布日期',blank=True, null=True )
    content = models.CharField(verbose_name='日记内容', max_length=1000,default='',blank=True, null=True)
    audio = models.FileField(verbose_name='语音日记', upload_to='dosjh/dairy/audio',blank=True, null=True)

    class Meta:
        verbose_name = '日记'
        verbose_name_plural = verbose_name
        ordering = ['-pubtime']

    def __str__(self):
        return self.content