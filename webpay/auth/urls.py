from django.conf.urls.defaults import patterns, url

import views

urlpatterns = patterns('',
    url(r'^verify$', views.verify, name='auth.verify'),
)
