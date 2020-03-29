from django.urls import path, re_path
from . import views

app_name = 'perms'
urlpatterns = [
    path('', views.PermsListView.as_view(), name='list'),
    path('add/', views.PermsCreateView.as_view(), name='add'),
    re_path('^(?P<pk>[0-9]+)/', views.PermDetailView.as_view(), name='detail'),
    re_path('^(?P<pk>[0-9]+)/del/', views.PermDeleteView.as_view(), name='del'),
    ]