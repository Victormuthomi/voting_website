from django.db import models
from election_app.models import Election
from candidates.models import Candidate
from django.contrib.auth.models import User

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link vote to a user
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)  # Candidate voted for
    election = models.ForeignKey(Election, on_delete=models.CASCADE)  # Election context
    created_at = models.DateTimeField(auto_now_add=True)  # When the vote was cast

    class Meta:
        unique_together = ('user', 'election')  # Ensure one vote per user per election

    def __str__(self):
        return f"{self.user.username} voted for {self.candidate} in {self.election.title}"
