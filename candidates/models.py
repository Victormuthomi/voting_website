from django.db import models

# Create your models here.
class Candidiate(models.Model):
    """Details of a candidate"""
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    id_number = models.IntegerField()
    phone_number = models.IntegerField()
    seat = models.char_field(max_length=20)

