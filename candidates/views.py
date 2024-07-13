from django.shortcuts import render

# Create your views here.
def index(request):
    """The home page for Voting website"""
    return render(request, 'candidates/index.xhtml')

