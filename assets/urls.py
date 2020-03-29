from django.urls import path, re_path
from . import views

app_name = 'assets'
urlpatterns = [
    path('', views.AssetsListView.as_view(), name='list'),
    path('add/', views.AssetsCreateView.as_view(), name='add'),
    re_path('(?P<pk>[0-9]+)/del/', views.AssetsDelView.as_view(), name='del'),
    re_path('(?P<pk>[0-9]+)/update/', views.AssetsUpdateView.as_view(), name='update'),
    re_path('(?P<pk>[0-9]+)/detail/', views.AssetsDetailView.as_view(), name='detail;'),
]