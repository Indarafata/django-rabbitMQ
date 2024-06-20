from django.urls import re_path
from transaction import views

urlpatterns = [
    re_path(r'^transaction/$', views.transaction_list, name='transaction'),
    # re_path(r'^transaction/(?P<pk>[0-9]+)$', views.tutorial_detail),
    # re_path(r'^transaction/published$', views.tutorial_list_published)
]
