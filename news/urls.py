from django.urls import path
from django.urls.conf import path
from .import views


urlpatterns = [
    path('', views.news, name='news'),
]
