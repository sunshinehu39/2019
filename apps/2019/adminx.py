
import xadmin
from .models import *

class FactionAdmin(object):
    list_display = ["fid","name","photo"]
    search_fields = ["fid", "name"]

class MemberAdmin(object):
    list_display = ["fid","mid","truename", "name","password"]
    list_filter =["fid","mid",]
    list_editable = ["password","truename", "name"]
    search_fields = ["mid", "name"]

class DreamAdmin(object):
    list_display = ["name","fid","mid","type","dream","state","rate"]
    list_filter =["fid","mid","type",]
    search_fields = ["name","type","dream","state","rate"]
    list_editable = ["rate"]

class GoalAdmin(object):
    list_display = ["M_id", "year","month","goal","done"]
    list_filter =["M_id", "year","month","goal","done"]
    search_fields = ["M_id", "year","month","goal","done"]

class DiaryAdmin(object):
    list_display = ["M_id", "start_time","stop_time","work","done"]
    list_filter = ["M_id", "start_time","stop_time","work","done"]
    search_fields =  ["M_id", "start_time","stop_time","work","done"]

xadmin.site.register(Faction,FactionAdmin)
xadmin.site.register(Member,MemberAdmin)
xadmin.site.register(Dream,DreamAdmin)
xadmin.site.register(Goal,GoalAdmin)
xadmin.site.register(Diary,DiaryAdmin)
xadmin.site.register(Plansum)
xadmin.site.register(Diarydetail)
