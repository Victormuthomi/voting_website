from django.db import models
from election_app.models import Election
from candidates.models import Candidate

class Vote(models.Model):
    """Details of the voting portal"""
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='votes')
    voting_value = models.IntegerField()  # Default value representing a vote, can be adjusted as needed
    timestamp = models.DateTimeField(auto_now_add=True)


    class Meta:
        unique_together = ('candidate', 'election')

    def __str__(self):
        return f'Vote for {self.candidate} in {self.election}'


