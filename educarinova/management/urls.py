from django.conf.urls import url, include
from educarinova.management.views.viewsa import dashboard, list_, edit, new, delete
from educarinova.management.views.views_classroom import *
from educarinova.management.views.views_unit import *
from educarinova.management.views.views_serie import *
from educarinova.management.views.views_subject import *
from educarinova.management.views.views_class import *
from educarinova.management.views.view_boleto import *


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
    url(r'^classroom/new/$', new_classroom, name='new_classroom'),

    url(r'^unit/$', list_unit, name='list_unit'),
    url(r'^unit/new/$', new_unit, name='new_unit'),

    url(r'^serie/$', list_serie, name='list_serie'),
    url(r'^serie/new/$', new_serie, name='new_setie'),

    url(r'^subject/$', list_subject, name='list_subject'),
    url(r'^subject/new/$', new_subject, name='new_subject'),

    url(r'^class/$', list_class, name='list_class'),
    url(r'^class/new/$', new_class, name='new_class'),

    url(r'^gerarboleto/$', print_all, name='gerar_boleto'),


]