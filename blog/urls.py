from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),  
    # url(r'^post/(?P<pk>[0-9]+)$', views.post_datail, name='post_datail'),
    path('post/<int:pk>', views.post_detail, name='post_detail'),
    # url('post/(?P<pk>[0-9]+)', views.post_detail, name='post_detail'),
    url(r'^post/create/$', views.post_create, name='post_create'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>[0-9]+)/delete/$', views.post_delete, name='post_delete'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^login/$', views.user_login, name='login'),
]