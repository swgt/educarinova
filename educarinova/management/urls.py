from django.conf.urls import url, include
from educarinova.management.views.views_general import dashboard
from educarinova.management.views.views_student import list_, edit, new, delete, detail, filter_by_class
from educarinova.management.views.views_classroom import *
from educarinova.management.views.views_unit import *
from educarinova.management.views.views_serie import *
from educarinova.management.views.views_subject import *
from educarinova.management.views.views_class import *
from educarinova.management.views.view_boleto import *
from educarinova.management.views.view_systemclass import *


class LENDConf:
    def __init__(self):
        self.urlpatterns = [
            url(r'^$', list_, name='list'),
            url(r'^change/(\d+)/$', edit, name='edit'),
            url(r'^new/$', new, name='new'),
            url(r'^delete/$', delete, name='delete'),
            url(r'^(\d+)/$', detail, name='detail'),
        ]

urlpatterns = [
    url(r'^dashboard/$', dashboard, name='management'),

    url(r'^students/', include(LENDConf(), namespace='students')),

    url(r'^systemclass/$', list_systemclass, name='list_systemclass'),
    url(r'^systemclass/new/$', new_systemclass, name='new_systemclass'),
    url(r'^systemclass/(\d+)/$', detail_systemclass, name='detail_systemclass'),

    url(r'^classroom/$', list_classroom, name='list_classroom'),
    url(r'^classroom/new/$', new_classroom, name='new_classroom'),

    url(r'^unit/$', list_unit, name='list_unit'),
    url(r'^unit/new/$', new_unit, name='new_unit'),

    url(r'^serie/$', list_serie, name='list_serie'),
    url(r'^serie/new/$', new_serie, name='new_setie'),

    url(r'^subject/$', list_subject, name='list_subject'),
    url(r'^subject/new/$', new_subject, name='new_subject'),

    url(r'^class/$', list_class, name='list_class'),
    url(r'^class/new/$', new_class, name='new_class'),
    url(r'^class/(\d+)/$', detail_class, name='detail_class'),

    url(r'^gerarboleto/$', print_all, name='gerar_boleto'),

    url(r'^filter_by_class/$', filter_by_class, name='filter_by_class'),
]