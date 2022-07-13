
from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('commonboard/', views.IndexView.as_view(), name='commonboard_list'),
    path('commonboard/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('세종대학교/', views.IndexViewP1.as_view(), name='privateboard1_list'),
    path('세종대학교/<int:pk>/', views.DetailViewP1.as_view(), name='p1_detail'),
    path('SSG대학교/', views.IndexViewP2.as_view(), name='privateboard2_list'),
    path('SSG대학교/<int:pk>/', views.DetailViewP2.as_view(), name='p2_detail'),
    path('commonboard/create', views.commonboard_create, name='commonboard_create'),
    path('index/',views.index, name='index'),
]