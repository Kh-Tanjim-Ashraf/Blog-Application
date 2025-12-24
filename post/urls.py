from django.urls import path
from . import views

app_name = 'PostApp'

urlpatterns = [
    path('', views.postList, name='postList'),
    path('post-add/', views.postAdd, name='postAdd'),
    path('<slug:slug>/', views.postDetail, name='postDetail'),  # The first 'slug' is the type specified, the 2nd one is the param that need to be same in both the frontend & django function's parameter
]