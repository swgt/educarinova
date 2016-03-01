from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from educarinova.core.views import home
from educarinova.management.views import dashboard

urlpatterns = [
    url(r'^$', home),
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout, {'next_page': '/dashboard/'}),
    url(r'^dashboard/$', dashboard),
    url(r'^admin/', admin.site.urls),
]