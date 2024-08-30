"""Defines the urls for the candidates app"""

from django.urls import path

from .import views

app_name = 'candidates'

urlpatterns=[
        #Home page
        path('', views.index, name='index'),
        
        #The path to the candidates of a particular election page
        path('elections/<int:election_id>/candidates/',views.candidates, name='candidates'),
        
        #The path to the details of a specific candidate 
        path('elections/<int:election_id>/candidates/<int:candidate_id>/', views.candidate_detail, name='candidate_detail'),

]
