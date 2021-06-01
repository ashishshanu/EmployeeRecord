from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.create, name = "home"),
    path('data/', views.retrieve_listView, name = 'retrive'),
    path('data/<int:_id>',views.retrieve_detailView, name = 'detailview'),
    path('data/<int:_id>/update', views.Update, name= 'update'),
    path('data/<int:_id>/delete', views.DeleteView, name = 'delete'),

]