# -*- coding:utf-8 -*-

from django.shortcuts import render,redirect
from .models import *
from homepage.models import GoldenWords
from django.http import HttpResponse
from django.db.models import Sum
import datetime
import time
import os


# 极度认真的2019
def teamView(request):
    tab = request.GET.get('tab', '日')
    ps = request.GET.get('ps', '年度计划')
    tag = request.GET.get('tag', '今天')
    type = request.GET.get('type', '日程')
    fid = request.GET.get('fid', '0')
    mid = request.GET.get('mid', '1')
    show = request.GET.get('show', '')

    login = request.GET.get('login', False)
    if login == 'login':
        request.session.flush()
        password = request.POST.get('password')
        try:
            myinfo = Member.objects.get(password=password)
            request.session['login'] = True
            request.session['mymid'] = str(myinfo.mid)
            fid =  str(myinfo.fid)
            mid =  str(myinfo.mid)

            return redirect('/2019?fid='+fid+'&mid='+mid)

        except Exception as e:
            request.session['hasmsg'] = True
            msg = '口令错误，请重新输入！'
    elif login == 'logout':
        request.session.flush()
        return redirect('/2019')

    login2019 =request.session.get('login',False)
    hasmsg =request.session.get('hasmsg',False)
    mymid = request.session.get('mymid',False)

    M_id = Member.objects.get(fid=fid, mid=mid).id
    name = Member.objects.get(id=M_id).name

    year = request.GET.get('year', datetime.datetime.now().year)
    month = request.GET.get('month', datetime.datetime.now().month)

    action = request.GET.get('action', False)

    if tab=='月':
        go = request.GET.get('go', False)

        if go:

            year = int(year)
            month = int(month)

            # 上个月
            if go == 'last':
                if month == 1:
                    month = 12
                    year -= 1
                else:
                    month = month - 1

            # 下个月
            if go == 'next':
                if month == 12:
                    month = 1
                    year += 1
                else:
                    month = month + 1

            year = str(year)
            month = str(month)

        goallist = Goal.objects.filter(M_id_id=M_id, month=month, year=year)


        if action:

            # 新增目标
            if action == 'addgoal':
                M_id_id = Member.objects.get(fid=fid, mid=mid).id
                goal = request.POST.get('newgoal')

                if Goal.objects.filter(M_id_id=M_id_id, year=year, month=month, goal=goal).exists():
                    msg = 'Oh,MyGod,目标已存在!'
                else:
                    newgoal = Goal(
                        M_id_id=M_id_id,
                        year=year,
                        month=month,
                        goal=goal,
                    )
                    newgoal.save()
                    msg = '恭喜你，目标添加成功！'

            # 删除目标
            elif action == 'delgoal':
                id = request.GET.get('G_id')
                Goal.objects.get(id=id).delete()

            # 修改目标
            elif action == 'changegoal':
                id = request.POST.get('G_id')
                goal = request.POST.get('changedgoal')
                Goal.objects.filter(id=id).update(goal=goal)

            # 检查目标
            elif action == 'checkgoal':
                id = request.GET.get('G_id', '0')

                if Goal.objects.get(id=id).done:
                    Goal.objects.filter(id=id).update(done=False)
                else:
                    Goal.objects.filter(id=id).update(done=True)

            return redirect('/2019?fid='+fid+'&mid='+mid+"&year="+year+"&month="+month+'&tab='+tab+'&type='+type+'&tag='+tag+'&ps'+ps)

    elif tab=='年':

        year='2019'

        if action:

            # 编辑计划
            if action == 'editplan':
                M_id_id = Member.objects.get(fid=fid, mid=mid).id
                plan = request.POST.get('plan')

                if Plansum.objects.filter(M_id_id=M_id_id, year=year).exists():
                    Plansum.objects.filter(M_id_id=M_id_id, year=year).update(plan=plan)
                else:
                    newplan = Plansum(
                        M_id_id=M_id_id,
                        year=year,
                        plan=plan,
                    )
                    newplan.save()

            # 编辑总结
            elif action == 'editsum':
                M_id_id = Member.objects.get(fid=fid, mid=mid).id
                summary = request.POST.get('summary')

                if Plansum.objects.filter(M_id_id=M_id_id, year=year).exists():
                    Plansum.objects.filter(M_id_id=M_id_id, year=year).update(summary=summary)
                else:
                    newsummary = Plansum(
                        M_id_id=M_id_id,
                        year=year,
                        summary=summary,
                    )
                    newsummary.save()

            return redirect('/2019?fid='+fid+'&mid='+mid+"&year="+year+"&month="+month+'&tab='+tab+'&type='+type+'&tag='+tag+'&ps='+ps)

        try:
            M_id = Member.objects.get(fid=fid, mid=mid).id
            planlist = Plansum.objects.filter(M_id_id=M_id,year=year)

            # 当查询集为空时，编辑器无法初始化，所以给list定义为一个任意非空列表即可。
            if planlist.exists():
                pass
            else:
                planlist=['']
        except:
            planlist = ['']

    elif tab=='日':

        slogan = GoldenWords.objects.order_by('?')[0].content
        slogan_nums = len(slogan)

        date = time.strftime('%Y-%m-%d', time.localtime(time.time()))

        oneday = datetime.timedelta(days=1)  # datetime.timedelta(1)
        today = datetime.datetime.today()  # datetime.datetime(2018, 11, 24, 18, 11, 13, 729694)
        tomorrow = today + oneday  # datetime.datetime(2018, 11, 25, 18, 13, 5, 451691)
        yesterday = today - oneday

        tag = request.GET.get('tag', '')
        type = request.GET.get('type', '日程')
        date = request.GET.get('date', date)


        if tag != '':
            if tag == '昨天':
                date = str(yesterday)[0:10]  # 将datetime转为字符串并截取前10个日期字符
            elif tag == '今天':
                date = str(today)[0:10]
            elif tag == '明天':
                date = str(tomorrow)[0:10]
        else:
            if date == str(yesterday)[0:10]:
                tag = '昨天'
            elif date == str(today)[0:10]:
                tag = '今天'
            elif date == str(tomorrow)[0:10]:
                tag = '明天'

        datestart = date + 'T19:00'
        datestop = date + 'T21:30'
        dateremind = date + 'T17:00'

        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[8:10])

        mydate2 = datetime.datetime.strptime(date[0:10],'%Y-%m-%d')

        if Diarydetail.objects.filter(M_id_id=M_id,pubtime=datetime.date(year, month, day)).exists():
            pass
        else:
            newdairy = Diarydetail(
                M_id_id=M_id,
                pubtime=date,
            )
            newdairy.save()

        weekday = datetime.date(year, month, day).weekday()  # 星期 5   星期（0-6），星期一为'0'

        weekday_dict = {
            0: '星期一',
            1: '星期二',
            2: '星期三',
            3: '星期四',
            4: '星期五',
            5: '星期六',
            6: '星期天',
        }

        cweekday = weekday_dict[weekday]  # '星期六'

        action = request.GET.get('action', '')

        if action != '':

            if request.method == 'POST':
                if action == 'add':
                    start_time = request.POST.get('start_time')
                    stop_time = request.POST.get('stop_time')

                    new_stop_time = datetime.datetime.strptime(stop_time[0:10],'%Y-%m-%d')

                    work = request.POST.get('work')
                    money = request.POST.get('money', 0)
                    if_important = request.POST.get('if_important')
                    if_day = request.POST.get('if_day')
                    if if_important == 'on':
                        if_important = True
                    else:
                        if_important = False

                    if if_day == 'on':
                        new_start_time = datetime.datetime.strptime(start_time[0:10], '%Y-%m-%d')
                        days = (new_stop_time-new_start_time).days+1
                        mydate_time = start_time[0:10]
                        begintime = start_time[11:]
                        endtime = stop_time[11:]
                        for i in range(days):
                            newwork = Diary(
                                M_id_id=M_id,
                                type=type,
                                start_time=mydate_time+' '+begintime,
                                stop_time=mydate_time+' '+endtime,
                                work=work,
                                money=money,
                                if_important=if_important,
                            )
                            newwork.save()
                            mydate_time = str(datetime.datetime.strptime(mydate_time,'%Y-%m-%d')+oneday)[0:10]
                    else:
                        newwork = Diary(
                            M_id_id=M_id,
                            type=type,
                            start_time=start_time,
                            stop_time=stop_time,
                            work=work,
                            money=money,
                            if_important=if_important,
                            done=True,
                        )
                        newwork.save()

                elif action == 'edit':
                    id = request.POST.get('id')
                    start_time = request.POST.get('start_time')
                    stop_time = request.POST.get('stop_time')
                    work = request.POST.get('work')
                    money = request.POST.get('money')
                    if_important = request.POST.get('if_important')

                    if if_important == 'on':
                        if_important = True
                    else:
                        if_important = False

                    Diary.objects.filter(id=id).update(
                        start_time=start_time,
                        stop_time=stop_time,
                        work=work,
                        money=money,
                        if_important=if_important, )

                elif action == 'editdiary':
                    content = request.POST.get('content')
                    file = request.FILES.get('audio')
                    import os

                    try:
                        # 拼接文件路径，名字
                        file_path = os.path.join('upload/dosjh/dairy/audio', file.name)
                        # 打开这个文件， 模式为二进制模式读写打开
                        f = open(file_path, mode='wb')
                        # 写到指定文件中
                        for i in file.chunks():
                            f.write(i)
                        # 关闭文件流
                        f.close()
                        Diarydetail.objects.filter(M_id_id=M_id, pubtime=date).update(content=content, audio=file_path)
                    except:
                        Diarydetail.objects.filter(M_id_id=M_id, pubtime=date).update(content=content)

            elif action == 'save':
                id = request.GET.get('id')
                Diary.objects.filter(id=id).update(type='日程')

            elif action == 'todo':
                id = request.GET.get('id')
                Diary.objects.filter(id=id).update(type='待办')

            elif action == 'tom_do':
                id = request.GET.get('id')
                newstart_time = Diary.objects.get(id=id).start_time + oneday
                newstop_time = Diary.objects.get(id=id).stop_time + oneday
                Diary.objects.filter(id=id).update(start_time=newstart_time, stop_time=newstop_time)

            # 检查
            elif action == 'check':
                id = request.GET.get('id')

                if Diary.objects.get(id=id).done:
                    Diary.objects.filter(id=id).update(done=False)
                else:
                    Diary.objects.filter(id=id).update(done=True)

            elif action == 'del':
                id = request.GET.get('id')
                Diary.objects.filter(id=id).delete()



            return redirect('/2019?fid='+fid+'&mid='+mid+'&tab='+tab+'&type='+type+'&tag='+tag+'&ps'+ps+'&date='+date+'&show='+show)

        list = Diary.objects.filter(M_id_id=M_id, type="日程", stop_time__contains=datetime.date(year, month, day))
        dairylist = Diarydetail.objects.filter(M_id_id=M_id, pubtime=datetime.date(year, month, day))

        if list.exists():
            totalmoney = list.aggregate(Sum('money'))['money__sum']
        else:
            totalmoney = 0

        monthlist = Diary.objects.filter(M_id_id=M_id, stop_time__year=year, stop_time__month=month)

        if monthlist.exists():
            totalmoneymonth = monthlist.aggregate(Sum('money'))['money__sum']
        else:
            totalmoneymonth = 0

        todolist = Diary.objects.filter(M_id_id=M_id, type="待办")

        if todolist.exists():
            totalmoneytodo = todolist.aggregate(Sum('money'))['money__sum']
        else:
            totalmoneytodo = 0

        # 将写了日记的日期添加到一个列表，在日历上做标记
        markdatelist = []
        for mydate in Diary.objects.filter(M_id_id=M_id).values_list('stop_time', flat=True):
            markdatelist.append(mydate.strftime("%Y-%m-%d"))
        return render(request, 'dosjh/2019.html', locals())

    return render(request, 'dosjh/2019.html', locals())

# 图片上传
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json

# 上传照片
@csrf_exempt
def uploadsimg(request):

    if request.method == 'POST':

        result={}
        imglist = []

        for img_url in request.FILES.getlist('fileVal'):

            img = Img2(
                photo=img_url,
            )
            img.save()

            imglist.append('upload/'+Img2.objects.last().photo.name)

        result['data']=imglist
        result['errno'] = 0

        return HttpResponse(json.dumps(result), content_type="application/json")
