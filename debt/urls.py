from django.urls import re_path
from debt import views

urlpatterns = [
    re_path(r'^debt/$', views.debt_list, name='debt'),
    # re_path(r'^transaction/(?P<pk>[0-9]+)$', views.tutorial_detail),
    # re_path(r'^transaction/published$', views.tutorial_list_published)
]
