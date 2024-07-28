"""Defines the urls for the voting page."""

from django.urls import path

from .import views

app_name = 'voting'

urlpatterns =[
        #Voting page
        path('voting/', views.voting, name='voting'),
        ]
