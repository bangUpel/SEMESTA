from django.db import models

# Create your models here.
class Voter(models.Model):
    name= models.CharField(max_length=100, blank=True, null=True)
    NIK = models.CharField(max_length=20, unique=True)
    voted = models.BooleanField(default=False)
    
    def __str__(self):
        return (f"{self.name} - {self.NIK}: {self.voted}")