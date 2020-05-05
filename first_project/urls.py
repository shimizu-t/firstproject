from django.urls import path
from . import views

app_name = 'first_project'
urlpatterns=[
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('list/',views.list,name='list'),
    path('listcreate/',views.listcreate,name='listcreate'),
    path('listdetail/<int:pk>',views.listdetail,name='listdetail'),
    path('listdelete/<int:pk>',views.listdelete,name='listdelete'),
    path('listupdate/<int:pk>',views.listupdate,name='listupdate'),
    path('userdetail/<int:pk>',views.UserDetailView.as_view(),name='userdetail'),
    path('userdetail/<int:pk>/userupdate',views.UserUpdateView.as_view(),name='userupdate'),

]
