from django.db import models
from election_app.models import Election
from candidates.models import Candidate

class Result(models.Model):
    """Model to store election results"""
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    class Meta:
        unique_together = ('election', 'candidate')

    def __str__(self):
        return f'{self.candidate} - {self.votes} votes'
