from django.urls import path
from .views import ongoing_elections, ended_elections, election_results, results

urlpatterns = [
    path('results/',results, name='results'),
    path('ongoing/', ongoing_elections, name='ongoing_elections'),
    path('ended/', ended_elections, name='ended_elections'),
    path('<int:election_id>/results/', election_results, name='election_results'),
]
