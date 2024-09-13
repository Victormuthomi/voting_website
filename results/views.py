from django.shortcuts import render
from django.db.models import Sum
from datetime import datetime
from election_app.models import Election
from candidates.models import Candidate
from .models import Result

def ongoing_elections(request):
    """View for ongoing elections with total votes for each candidate"""
    ongoing_elections = Election.objects.filter(date__gt=datetime.now())
    results = Result.objects.filter(election__in=ongoing_elections).values('election', 'candidate').annotate(total_votes=Sum('votes'))
    
    election_candidate_totals = {}
    for result in results:
        election_id = result['election']
        candidate_id = result['candidate']
        total_votes = result['total_votes']
        
        if election_id not in election_candidate_totals:
            election_candidate_totals[election_id] = {}
        
        election_candidate_totals[election_id][candidate_id] = total_votes

    return render(request, 'results/ongoing_elections.xhtml', {
        'elections': ongoing_elections,
        'election_candidate_totals': election_candidate_totals
    })

def ended_elections(request):
    """View for ended elections with total votes for each candidate"""
    ended_elections = Election.objects.filter(date__lte=datetime.now())
    results = Result.objects.filter(election__in=ended_elections).values('election', 'candidate').annotate(total_votes=Sum('votes'))
    
    election_candidate_totals = {}
    for result in results:
        election_id = result['election']
        candidate_id = result['candidate']
        total_votes = result['total_votes']
        
        if election_id not in election_candidate_totals:
            election_candidate_totals[election_id] = {}
        
        election_candidate_totals[election_id][candidate_id] = total_votes

    return render(request, 'results/ended_elections.xhtml', {
        'elections': ended_elections,
        'election_candidate_totals': election_candidate_totals
    })

def election_results(request, election_id):
    """View for the results of a specific election"""
    election = get_object_or_404(Election, id=election_id)
    results = Result.objects.filter(election=election).select_related('candidate')

    # Prepare a dictionary with candidates and their total votes
    candidates_with_totals = defaultdict(int)
    for result in results:
        candidates_with_totals[result.candidate] += result.votes

    # Prepare a dictionary with candidate details and total votes
    candidates_with_totals = {
        candidate: total_votes
        for candidate, total_votes in candidates_with_totals.items()
    }

    return render(request, 'results/election_results.xhtml', {
        'election': election,
        'candidates_with_totals': candidates_with_totals
    })

    return render(request, 'results/election_results.xhtml', {
        'election': election,
        'results': results,
        'candidates_with_totals': candidates_with_totals
    })



def results(request):
    """View for all election results"""
    all_elections = Election.objects.all()
    results = {election: Result.objects.filter(election=election) for election in all_elections}
    return render(request, 'results/results.xhtml', {'results': results})

