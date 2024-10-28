from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Election

@login_required  # Ensure the user is logged in
def elections(request):
    """Get ongoing and upcoming elections based on the current date."""
    today = timezone.localdate()  # Get today's date in local timezone
    current_time = timezone.now()  # Get current time in UTC

    # Fetch ongoing and upcoming elections
    ongoing = Election.objects.filter(date=today)  # Ongoing elections for today
    upcoming = Election.objects.filter(date__gt=today)  # Upcoming elections

    context = {
        'ongoing_elections': ongoing,
        'upcoming_elections': upcoming,
    }

    return render(request, 'election_app/election.xhtml', context)
