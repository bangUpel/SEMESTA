from django.db import models

# Create your models here.
class Candidates(models.Model):
    name=models.CharField(max_length=100)
    vote=models.IntegerField(default=0)
    total_point = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Voter(models.Model):
    name = models.CharField(max_length=100)
    nik = models.CharField(max_length=16, blank=False)
    vote = models.BooleanField(default=False)
    
    def __str__(self):
        return (
            f"{self.name} - {self.nik}"
        )