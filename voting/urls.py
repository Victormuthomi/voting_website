from django.urls import path
from .views import vote_view

urlpatterns = [
        path('election/<int:election_id>/vote/', vote_view, name='vote_page'),
]
