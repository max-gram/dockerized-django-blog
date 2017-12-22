from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', views.detail, name='detail'),
    url(r'^$', views.index, name='index'),
]
