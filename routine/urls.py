from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),

    url(r'^routine/$', views.index, name='routine_index'),
    url(r'^routine/departments/$', views.departments, name='departments'),
    url(r'^routine/tasks/$', views.tasks, name='tasks'),
    url(r'^routine/audio/$', views.audio, name='audio'),
    url(r'^routine/media/$', views.media, name='media'),
    url(r'^routine/light/$', views.light, name='light'),
    url(r'^routine/stage/$', views.stage, name='stage'),
    url(r'^routine/power/$', views.power, name='power'),
    url(r'^routine/inventory/$', views.inventory, name='inventory'),
    url(r'^routine/truss/$', views.truss, name='truss'),
    url(r'^routine/temp/$', views.temp, name='temp'),

]
