from django.urls import path
from . import views

# 命名空间
app_name = 'info'

urlpatterns = [
    path('',views.index,name='index'),
    path('ap/list', views.ap, name='ap'),
    path('office',views.office,name='office'),
    path('smart',views.smart,name='smart'),
    path('system/list',views.system,name='system'),
]