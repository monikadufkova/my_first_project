from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', include(views.post_list), name='post_list'),
]

