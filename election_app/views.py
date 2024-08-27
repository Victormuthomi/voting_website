from django.shortcuts import render

from . models import Election

from django.utils import timezone

# Create your views here.
def elections(request):
    """First set the todays date to today"""
    today = timezone.now().date()
    """Filter the election date to be today or a day greater than today"""
    elections = Election.objects.filter(date__gte=today)
    context = { 'elections' : elections }

    return render(request, 'election_app/election.xhtml',context)

