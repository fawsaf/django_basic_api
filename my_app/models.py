# Create your models here.
from django.db import models
from uuid import uuid4

class Employee(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True,unique=True, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    position = models.CharField(max_length=100)
    hiring_date = models.DateField()
    email = models.EmailField(unique=True)

class Vacation(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approve', 'Approved'),
        ('reject', 'Rejected'),
    )

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    attachment_url = models.URLField()
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending',
    )
