from django.shortcuts import render, redirect
from .forms import SeatVoteForm
from .models import Vote
from candidates.models import Candidate
from election_app.models import Election

def vote_view(request, election_id):
    election = Election.objects.get(id=election_id)

    if request.method == 'POST':
        form = SeatVoteForm(request.POST, election=election)
        if form.is_valid():
            for seat_field, candidate in form.cleaned_data.items():
                if candidate:
                    # Check if the user has already voted for this seat in the election
                    if not Vote.objects.filter(user=request.user, candidate=candidate).exists():
                        Vote.objects.create(
                            user=request.user,
                            candidate=candidate,
                            election=election,
                            voting_value=1  # Assuming voting_value is 1 for a selected candidate
                        )
                        # Increment the candidate's vote tally
                        candidate.votes = models.F('votes') + 1
                        candidate.save(update_fields=['votes'])
            
            return redirect('results_page')  # Replace with your actual results page
    else:
        form = SeatVoteForm(election=election)

    return render(request, 'voting/voting.xhtml', {'form': form, 'election': election})

