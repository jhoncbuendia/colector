"""colector URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from service.views import AllowedForms, SingleForm, FillForm, ColectorIdReport, FormNameReport
from service.views import FormIdReport
urlpatterns = [    

    

    url(r'^colector/allowed/forms/', AllowedForms.as_view()),
    url(r'^form/single/', SingleForm.as_view()),
    url(r'^fill/form/$', FillForm.as_view()),
    url(r'^fill/form/(?P<id>.+)/$', FillForm.as_view()),
    url(r'^filled/forms/report/colector/(?P<id>.+)/$', 'service.views.ColectorIdReport'),
    url(r'^filled/forms/report/formname/(?P<name>.+)/$', 'service.views.FormNameReport'),
    url(r'^filled/forms/report/colectorid/(?P<id>.+)/date/(?P<a>.+)/(?P<m>.+)/(?P<d>.+)/$', 'service.views.DateReport'),
    
]