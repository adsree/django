from django.urls import path, include
from . import views
app_name = 'app1'

urlpatterns = [
    path('', views.home),
    path('work1/', views.work1),
    path('list/', views.data, name= "data"),
]