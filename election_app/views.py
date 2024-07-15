from django.shortcuts import render

from . models import Election
# Create your views here.
def election(request):
    """The page for returning the election"""
    return render(request, 'election_app/election.xhtml')

