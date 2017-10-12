from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="login_main"),
    url(r'^logout/$', views.logmeout, name="logout"),
]
