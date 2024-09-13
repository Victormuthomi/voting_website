from django.shortcuts import render, redirect
from .forms import SeatVoteForm
from .models import Vote
from candidates.models import Candidate
from election_app.models import Election
from django.db import models

def vote_view(request, election_id):
    election = Election.objects.get(id=election_id)

    if request.method == 'POST':
        form = SeatVoteForm(request.POST, election=election)

        if form.is_valid():
            for seat_field, candidate in form.cleaned_data.items():
                if candidate:
                    # Check if a vote already exists for this candidate and election
                    if not Vote.objects.filter(candidate=candidate, election=election).exists():
                        Vote.objects.create(
                            candidate=candidate,
                            election=election,
                            voting_value=1  # Assuming voting_value is 1 for a selected candidate
                        )
                        # Increment the candidate's vote tally
                        candidate.votes = models.F('votes') + 1
                        candidate.save(update_fields=['votes'])
                    else:
                        # Handle duplicate voting attempt
                        pass
            
            return redirect('results')  # Replace 'results' with your actual results page name
    else:
        form = SeatVoteForm(election=election)

    return render(request, 'voting/voting.xhtml', {'form': form, 'election': election})

