
from django.contrib import admin
from django.urls import path, re_path
from .import views
import re
from django.urls import path, register_converter
# from . import converters, views

# class FourDigitYearConverter:
    # regex = '[0-9]{4}'
#     regex = re.sub(r'\s+', '-')

#     def to_python(self, value):
#         return value

#     def to_url(self, value):
#         return '%s' % value

# register_converter(converters.FourDigitYearConverter, 'title')

# re.sub(r'\s+', '-')
# r'^(?P<slug>[-\w\d]+),(?P<id>\d+)/$'
# r'^(?P<slug:title>\s+,-)/$'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('images/', views.images, name="images"),
    path('images/<title>/', views.timages, name="images"),
    path('gifs/<title>/', views.g, name="g"),
    path("gif/<title>",views.gif, name="gif"),
    # re_path(r'^images/(?P<title>[\s,-]+)/$', views.timages, name="images"),
]
