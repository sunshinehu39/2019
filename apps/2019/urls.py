
from django.urls import path
from .views import *

urlpatterns = [
    path('2019', teamView, name='2019'),  # 2019
    path('uploadsimg', uploadsimg, name='uploadsimg'),  # 图片上传
]
