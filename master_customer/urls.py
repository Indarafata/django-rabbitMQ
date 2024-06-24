from django.urls import re_path
from master_customer import views

urlpatterns = [
    re_path(r'^master_customer/$', views.master_customer_list, name='master_customer'),
    # re_path(r'^transaction/(?P<pk>[0-9]+)$', views.tutorial_detail),
    # re_path(r'^transaction/published$', views.tutorial_list_published)
]
