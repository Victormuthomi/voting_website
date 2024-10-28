from django.db import models
from election_app.models import Election 
from candidates.models import Candidate, Seat  

class Result(models.Model):
    election = models.ForeignKey(
        Election, 
        on_delete=models.CASCADE, 
        related_name='results'
    )
    candidate = models.ForeignKey(
        Candidate, 
        on_delete=models.CASCADE, 
        related_name='results'
    )
    votes = models.PositiveIntegerField(default=0)  # Default votes to zero when creating a result
    seat = models.ForeignKey(
        Seat, 
        on_delete=models.CASCADE, 
        related_name='results'
    )

    class Meta:
        unique_together = ('election', 'candidate')  # Ensure each candidate can only have one result per election

    def __str__(self):
        return f"{self.candidate} - {self.votes} votes in {self.election.name} for {self.seat.name}"
