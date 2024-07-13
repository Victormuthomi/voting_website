"""Defines the urls for the candidates app"""

from django.urls import path

from .import views

app_name = 'candidates'

urlpatterns=[
        #Home page
        path('', views.index, name='index'),

]
