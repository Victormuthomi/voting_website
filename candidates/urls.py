"""Defines the urls for the candidates app"""

from django.urls import path

from .import views

app_name = 'candidates'

urlpatterns=[
        #Home page
        path('', views.index, name='index'),
        # path('candidates/', views.candidates, name='candidates'),
        path('elections/<int:election_id>/candidates/',views.candidates, name='candidates')
]
