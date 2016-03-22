from django.conf.urls import url, include
from educarinova.management.views import dashboard, list_, edit, new, delete


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
]