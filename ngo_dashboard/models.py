from django.db import models

# Create your models here.
from django.db import models

class NGOProfile(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.TextField()
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Project(models.Model):
    ngo = models.ForeignKey(NGOProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title

