from django.urls import path

from . import views

app_name = "user"

urlpatterns = [
    path('', views.index),
    path('signup/', views.signup, name='signup'),
]