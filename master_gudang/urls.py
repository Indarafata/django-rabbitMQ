from django.urls import re_path
from master_gudang import views

urlpatterns = [
    re_path(r'^master_gudang/$', views.master_gudang_list, name='master_gudang'),
    # re_path(r'^transaction/(?P<pk>[0-9]+)$', views.tutorial_detail),
    # re_path(r'^transaction/published$', views.tutorial_list_published)
]
