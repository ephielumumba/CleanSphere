from turtle import home

from django.contrib import admin
from django.urls import path
from pollutionapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('resources/', views.resources, name='resources'),
    path('blog-details/', views.blogdetails, name='blog-details'),
    path('contact/', views.contact, name='contact'),
    path('watertracker/', views.watertracker, name='watertracker'),
    path('donate/', views.donate, name='donate'),
    path('waterdata/', views.waterdata, name='waterdata'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),
    path('delete/<int:id>', views.delete),



]
