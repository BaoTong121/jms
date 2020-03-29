from django.urls import path, re_path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.user_list, name='list'),
    re_path('(?P<user_id>[0-9]+)/update/', views.user_update, name='update'),
    re_path('(?P<user_id>[0-9]+)/del/', views.user_delete, name='del'),
    path('add/', views.user_add, name='add'),
    path('login/', views.login_, name='login'),
    path('logout/', views.logout_, name='logout'),

]