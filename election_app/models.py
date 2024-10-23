from django.db import models

class Election(models.Model):
    """An election to be held."""
    name = models.CharField(max_length=50)
    date = models.DateField()
    details = models.TextField()

    def __str__(self):
        """Return the name of the election on the admin panel."""
        return self.name