from django.db import models

# Create your models here.
class Content(models.Model):
    firstName=models.CharField(max_length=50)
    lastName=models.CharField(max_length=50)
    userName=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)

    def __str__(self):
        return self.email
        