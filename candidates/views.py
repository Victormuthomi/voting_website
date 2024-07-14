from django.shortcuts import render

# Create your views here.
def index(request):
    """The home page for Voting website"""
    return render(request, 'candidates/index.xhtml')

def candidates(request):
    """Show all the candidates"""
    candidates = Candidate.objects.order_by('first_name')
    context = { 'candidates' : candidates }

    return render(request, 'candidates/candidates.xhtml', context)

