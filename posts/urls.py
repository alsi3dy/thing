from django.conf.urls import url
from . import views


urlpatterns = [
    
    url(r'^create/$', views.post_create, name = "create"),
    url(r'^update/$', views.post_update, name ="other_place"),
    url(r'^delete/$', views.post_delete, name ="delete"),
    url(r'^list/$', views.post_list, name ="list"),
    url(r'^detail/$', views.post_detail, name ="detail"),
    url(r'^bye/$', views.post_bye, name ="bye"),
    url(r'^why/$', views.post_why, name ="why"),
    url(r'^sassy/$', views.post_sassy, name ="sassy"),
    url(r'^dict/$', views.post_dict, name ="dict")
]