from django.urls import re_path
from master_stok import views

urlpatterns = [
    re_path(r'^master_stock/$', views.master_stock_list, name='master_stock'),
    # re_path(r'^transaction/(?P<pk>[0-9]+)$', views.tutorial_detail),
    # re_path(r'^transaction/published$', views.tutorial_list_published)
]
