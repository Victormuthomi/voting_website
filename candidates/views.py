from django.shortcuts import render, get_object_or_404
from .models import Candidate

from election_app.models import Election

# Create your views here.
def index(request):
    """The home page for Voting website"""
    return render(request, 'candidates/index.xhtml')

def candidates(request, election_id):
    """Show all the candidates for a particular election"""
    election = get_object_or_404(Election, id=election_id)
    candidates = Candidate.objects.filter(election=election).order_by('first_name')
    context = { 'candidates': candidates, 'election': election }

    return render(request, 'candidates/candidates.xhtml', context)

