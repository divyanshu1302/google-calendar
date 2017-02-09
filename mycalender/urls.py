from django.conf.urls import url
from . import views

app_name = 'mycalender'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/$',views.event_create, name = 'create'),
    #url(r'^detail_popup/(?P<album_id>[0-9]+)/$', views.d_popup),
]
