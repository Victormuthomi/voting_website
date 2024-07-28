"""Defines the urls for the results app"""

from django.urls import path

from . import views

app_name = 'results'

urlpatterns = [
        #results page
        path('results/', views.results, name='results')
]
