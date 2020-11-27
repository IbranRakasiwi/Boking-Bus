from django.urls import path
from django.contrib import admin
from django.shortcuts import render
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('', views.tampil),
    path('user/', views.user, name='user'),
    path('tabel/', views.tabel, name='tabel'),
    # path('tampilguru/', views.tampilguru, name='pengajar'),
    # path('detailguru/', views.detailguru, name='gdetail'),
    # path('detailmurid/', views.detailmurid, name='mdetail'),

]