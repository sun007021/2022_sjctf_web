
from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('commonboard/', views.IndexView.as_view(), name='commonboard_list'),
    path('commonboard/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('commonboard/create', views.commonboard_create, name='commonboard_create'),
]