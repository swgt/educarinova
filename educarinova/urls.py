from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout
from educarinova.core.views import home
from educarinova.management.views.views_general import register

urlpatterns = [
    url(r'^$', home),
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout, {'next_page': login}),
    url(r'^accounts/register/$', register),
    url(r'', include('educarinova.management.urls')),
    url(r'^admin/', admin.site.urls),
]