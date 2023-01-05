
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('images/<title>/', views.images, name="images"),
    path('image/<title>/', views.timages, name="image"),
    path('gifs/<title>/', views.g, name="g"),
    path("gif/<title>/",views.gif, name="gif"),

    #urls for generating images and GIFs from list
    path("image-list/",views.imagelist),
    path("gif-list/",views.giflist),
]
