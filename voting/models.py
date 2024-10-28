# voting/models.py
from django.db import models
from django.contrib.auth.models import User
from candidates.models import Candidate  # Adjust import if your Candidate model is elsewhere
from election_app.models import Election  # Adjust import if your Election model is elsewhere

class Election(models.Model):
    title = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    
    def is_ongoing(self):
        from django.utils import timezone
        return self.start_time <= timezone.now() <= self.end_time

    def is_upcoming(self):
        return self.start_time > timezone.now()

    def __str__(self):
        return self.title

class Candidate(models.Model):
    name = models.CharField(max_length=255)
    election = models.ForeignKey(Election, related_name='candidates', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the user who voted
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)  # Link to the selected candidate
    election = models.ForeignKey(Election, on_delete=models.CASCADE)  # Link to the associated election
    timestamp = models.DateTimeField(auto_now_add=True)  # Record when the vote was cast

    class Meta:
        unique_together = ('user', 'election')  # Ensure that a user can vote only once per election

    def __str__(self):
        return f"{self.user} voted for {self.candidate} in {self.election}"
