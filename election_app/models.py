from django.db import models
from django.utils import timezone

class Election(models.Model):
    """An election to be held."""
    name = models.CharField(max_length=50)
    date = models.DateField()
    details = models.TextField()

    def __str__(self):
        """Return the name of the election on the admin panel."""
        return self.name

    def is_upcoming(self):
        """Check if the election is scheduled for a future date."""
        return self.date > timezone.now().date()

    def is_ongoing(self):
        """Check if the election is happening today."""
        return self.date == timezone.now().date()
