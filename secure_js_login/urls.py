# coding: utf-8


from django.conf.urls import patterns, url

from secure_js_login import views


urlpatterns = patterns('',
    url(r'^', views.login_honeypot, name='Auth-login_honeypot'),
)
