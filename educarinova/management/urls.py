from django.conf.urls import url, include
from educarinova.management.views.viewsa import dashboard, list_, edit, new, delete
from educarinova.management.views.views_classroom import *


class LENDConf:
    def __init__(self):
        self.urlpatterns = [
            url(r'^$', list_, name='list'),
            url(r'^(\d+)/$', edit, name='edit'),
            url(r'^new/$', new, name='new'),
            url(r'^delete/$', delete, name='delete'),
        ]

urlpatterns = [
    url(r'^dashboard/$', dashboard),
    
    url(r'^students/', include(LENDConf(), namespace='students')),

    url(r'^classroom/$', list_classroom, name='list_classroom'),
    url(r'^classroom/new/$', new_classroom, name='list_classroom'),
]