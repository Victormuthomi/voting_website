from django.shortcuts import render

# Create your views here.
def results(request):
    """The page for returning the results"""
    return render(request, 'results/results.xhtml')

