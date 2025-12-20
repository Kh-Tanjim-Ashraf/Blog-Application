from django.urls import path
from . import views

app_name = 'PostApp'

urlpatterns = [
    path('', views.postList, name='postList'),
]