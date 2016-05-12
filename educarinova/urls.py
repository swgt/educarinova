from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.conf.urls import url, include
from educarinova.management.views.views_general import register
from educarinova.management import urls
from educarinova.core.views import home


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, {'next_page': '/'}, name='logout'),
    url(r'^accounts/register/$', register, name='register'),
    url(r'', include(urls)),
]