"""Define the urls for the election app"""

from django.urls import path

from .import views

app_name = 'election_app'

urlpatterns=[
        path('election/', views.elections, name='elections')
]
