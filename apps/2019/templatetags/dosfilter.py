import re
from django import template
register = template.Library()

# 自定义过滤器：日期转星期
@register.filter
def week(date):
    weekday = date.weekday()
    weekday_dict = {
        0: '星期一',
        1: '星期二',
        2: '星期三',
        3: '星期四',
        4: '星期五',
        5: '星期六',
        6: '星期天',
    }
    cweekday = weekday_dict[weekday]
    return cweekday

# 自定义过滤器：添加锚点
@register.filter
def anchor(old_content):
    data=[]
    reg = re.compile('<[^>]*>')

    data2 = re.findall(r'<blockquote>(.*?)</blockquote>', old_content)
    for j in data2:
        data.append(re.sub("&nbsp;", "", reg.sub('',j)))

    old_content_list = re.split(r"(<blockquote>)", old_content)

    new_content_list = []
    i=1
    k=0
    for index,j in enumerate(data) :
        new_content_list.append(old_content_list[index+k])
        new_content_list.append(re.sub(r"(<blockquote>)", "<a name="+j+"></a><blockquote>",old_content_list[index+i]))
        i+=1
        k+=1

    new_content_list.append(old_content_list[i + k -1])

    return ''.join(new_content_list)