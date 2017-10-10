"""watpi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
<<<<<<< HEAD
    # url(r'^admin/', admin.site.urls),
=======
    # url('^', include('django.contrib.auth.urls')),
    url(r'^admin/', admin.site.urls),
>>>>>>> c8e8b3b4fe017f9b149558e619d972ab5b712ad9
    url(r'^camera/', include('apps.camera.urls', namespace='camera')),
    url(r'^dashboard/', include('apps.dashboard.urls', namespace='dashboard')),
    url(r'^rover/', include('apps.rover.urls', namespace='rover')),
    url(r'^login/', include('apps.login.urls')),
    url('^logout/$', auth_views.LogoutView.as_view()),
]
