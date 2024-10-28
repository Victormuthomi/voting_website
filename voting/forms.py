# voting/forms.py
from django import forms
from election_app.models import Election
from candidates.models import Candidate

class SeatVoteForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.election = kwargs.pop('election')
        self.user = kwargs.pop('user')  # Pass user when initializing the form
        super().__init__(*args, **kwargs)

        # Create a field for each candidate in the election
        candidates = Candidate.objects.filter(election=self.election)
        for candidate in candidates:
            self.fields[f'vote_{candidate.id}'] = forms.BooleanField(
                label=candidate.name, 
                required=False
            )

    def clean(self):
        cleaned_data = super().clean()
        
        # Check if user has already voted in this election
        from .models import Vote  # Local import to avoid circular import

        if Vote.objects.filter(user=self.user, election=self.election).exists():
            raise forms.ValidationError("You have already voted in this election.")

        # Ensure at least one candidate is selected
        if not any(cleaned_data.get(f'vote_{candidate.id}') for candidate in Candidate.objects.filter(election=self.election)):
            raise forms.ValidationError("You must select at least one candidate to vote for.")

        return cleaned_data
