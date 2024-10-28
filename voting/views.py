from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from .forms import SeatVoteForm
from .models import Election, Vote, Candidate
from django.contrib.auth.decorators import login_required
import logging

logger = logging.getLogger(__name__)

@login_required
def vote_view(request, election_id):
    logger.info("Vote view accessed for election ID: %s", election_id)
    election = get_object_or_404(Election, id=election_id)
    candidates = Candidate.objects.filter(election=election)

    if request.method == 'POST':
        form = SeatVoteForm(request.POST, election=election, user=request.user)

        if form.is_valid():
            if Vote.objects.filter(user=request.user, election=election).exists():
                messages.error(request, "You have already voted in this election.")
                return redirect(reverse('election_app:elections'))

            selected_candidates = [candidate_id for candidate_id, selected in form.cleaned_data.items() if selected]

            if len(selected_candidates) != 1:
                messages.error(request, "You must select exactly one candidate to vote for.")
                return redirect(reverse('election_app:elections'))

            candidate_id = selected_candidates[0]
            candidate = get_object_or_404(Candidate, id=candidate_id)
            Vote.objects.create(user=request.user, candidate=candidate, election=election)

            messages.success(request, "Your vote has been successfully submitted!")
            return redirect(reverse('election_app:elections'))  # Redirect to elections

    else:
        form = SeatVoteForm(election=election, user=request.user)

    context = {
        'form': form,
        'election': election,
        'candidates': candidates,
    }
    return render(request, 'voting/voting.xhtml', context)
