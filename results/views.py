from django.shortcuts import render
from django.db.models import Sum
from django.utils import timezone
from election_app.models import Election
from .models import Result, Seat

def results(request):
    """View for displaying election results. Shows only ended elections and a message if ongoing elections exist."""
    current_time = timezone.now()  # Get the current time

    # Fetch ended elections
    ended_elections = Election.objects.filter(date__lte=current_time)
    ongoing_elections = Election.objects.filter(date__gt=current_time)

    election_results = {}
    
    for election in ended_elections:
        # Fetch results for each ended election
        results = Result.objects.filter(election=election)\
            .select_related('candidate', 'seat')\
            .values('seat__name', 'candidate__first_name', 'candidate__last_name')\
            .annotate(total_votes=Sum('votes'))\
            .order_by('seat', '-total_votes')  # Order by seat and then total votes

        # Group results by seat
        seat_results = {}
        for result in results:
            seat_name = result['seat__name']
            if seat_name not in seat_results:
                seat_results[seat_name] = []
            seat_results[seat_name].append(result)

        election_results[election] = {
            'results': seat_results,
            'status': 'Ended'
        }

    # Check if there are ongoing elections
    if ongoing_elections.exists():
        message = "There are ongoing elections. Results will be displayed once they have ended."
    else:
        message = None  # No ongoing elections

    return render(request, 'results/results.xhtml', {
        'election_results': election_results,
        'title': 'Election Results',
        'message': message,  # Pass the message to the template
    })
