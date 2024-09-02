from django import forms
from candidates.models import Candidate

class SeatVoteForm(forms.Form):
    def __init__(self, *args, **kwargs):
        election = kwargs.pop('election', None)
        super().__init__(*args, **kwargs)

        if election:
            # Fetch candidates related to the election
            candidates = Candidate.objects.filter(election=election)
            
            # Group candidates by seat
            seats = set(candidate.seat for candidate in candidates)
            
            for seat in seats:
                seat_candidates = candidates.filter(seat=seat)
                self.fields[f'seat_{seat.id}'] = forms.ModelChoiceField(
                    queryset=seat_candidates,
                    widget=forms.RadioSelect,
                    label=seat
                )

