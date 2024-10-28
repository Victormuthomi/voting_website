from django.db import models

class Seat(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Candidate(models.Model):
    election = models.ForeignKey('election_app.Election', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)  # First name of the candidate
    last_name = models.CharField(max_length=20)   # Last name for full name representation
    id_number = models.PositiveIntegerField(unique=True)  # Unique identifier for each candidate
    phone_number = models.CharField(max_length=15)  # Changed to CharField to accommodate various formats
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)  # Foreign key to the Seat model
    picture = models.ImageField(upload_to='candidate_pictures/')  # Image field for candidate's picture
    manifesto = models.TextField()  # Text field for the candidate's manifesto
    motto = models.CharField(max_length=100)  # Candidate's campaign motto

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def total_votes(self):
        return self.vote_set.count()  # Count of votes associated with this candidate
