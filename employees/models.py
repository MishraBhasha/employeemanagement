#from django.db import models

# Create your models here.
from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    department = models.CharField(max_length=100)
    date_of_birth = models.DateField(default='2000-01-01')
    address = models.CharField(max_length=255, null=False, default='Default Address')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    