from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SeatVoteForm
from .models import Vote
from candidates.models import Candidate
from election_app.models import Election

@login_required
def vote_view(request, election_id):
    election = get_object_or_404(Election, id=election_id)

    # Check if the user has already voted in this election
    if Vote.objects.filter(user=request.user, election=election).exists():
        messages.error(request, "You have already voted in this election.")
        return redirect('results')

    # Check if the election is upcoming or ongoing
    if election.is_upcoming():
        candidates = Candidate.objects.filter(election=election)
        return render(request, 'voting/view_candidates.xhtml', {'election': election, 'candidates': candidates})

    if not election.is_ongoing():
        messages.error(request, "Voting is not allowed at this time.")
        return redirect('home')

    if request.method == 'POST':
        form = SeatVoteForm(request.POST, election=election, user=request.user)

        if form.is_valid():
            for seat_field, selected in form.cleaned_data.items():
                # Verify the seat field corresponds to a candidate
                try:
                    candidate_id = seat_field.split('_')[1]  # Extract candidate ID
                    candidate = get_object_or_404(Candidate, id=candidate_id, election=election)

                    # Only create a Vote if the candidate is valid and selected
                    if selected:
                        Vote.objects.create(
                            user=request.user,
                            candidate=candidate,
                            election=election
                        )
                        messages.success(request, f"You have voted for {candidate.name}!")

                except (IndexError, ValueError, Candidate.DoesNotExist):
                    messages.error(request, "An error occurred while processing your vote.")

            return redirect('results')

    else:
        form = SeatVoteForm(election=election, user=request.user)

    return render(request, 'voting/voting.xhtml', {'form': form, 'election': election})
