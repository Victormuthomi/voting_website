from django.db import models

from election_app.models import Election 

# Create your models here.
class Candidate(models.Model):
    """Details of a candidate"""
    election = models.ForeignKey(Election,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    id_number = models.IntegerField()
    phone_number = models.IntegerField()
    seat = models.CharField(max_length=20)
    picture = models.ImageField()
    manifesto = models.TextField()
    motto = models.CharField(max_length=100)
    

    def __str__(self):
        """Return a string representation of the model"""
        return self.first_name 


