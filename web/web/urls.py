"""web URL Configuration

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
from django.conf.urls import url
from webapp import views
from django.views.generic.base import RedirectView

urlpatterns = [

    url(r'^dianzan/',views.dianzan , name="dianzan"),
    url(r'^search/',views.search , name="search"),

    url(r'^index/' ,views.html().index , name="index"),
    url(r'^about/',views.html().about , name="about"),
    url(r'^comment/',views.html().comment , name="comment"),
    url(r'^base64/' ,views.html().base64 , name="base64"),
    url(r'^base64_ajax/',views.ajax_request().base64_ajax , name="base64_ajax"),

    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico')),
    url(r'^.*$', views.html().index),
]




