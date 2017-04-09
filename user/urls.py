from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.user, name='index'),
    url(r'^user/$', views.user, name='test'),
    url(r'^user/submit_data', views.sub, name='sub'),
]
