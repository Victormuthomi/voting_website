# candidates/models.py
from django.db import models

class Seat(models.Model):
    name = models.CharField(max_length=100)
    # Add any other fields you need here

    def __str__(self):
        return self.name

class Candidate(models.Model):
    election = models.ForeignKey('election_app.Election', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    id_number = models.IntegerField()
    phone_number = models.IntegerField()
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)  # Updated to ForeignKey
    picture = models.ImageField(upload_to='candidate_pictures/')
    manifesto = models.TextField()
    motto = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name

