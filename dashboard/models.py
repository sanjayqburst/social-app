from django.db import models

# Create your models here.

# class User(models.Model):
#     firstName=models.CharField(max_length=50)
#     lastName=models.CharField(max_length=50)
#     userName=models.CharField(max_length=50)
#     password=models.CharField(max_length=50)
#     email=models.EmailField(max_length=100)
    
#     def __str__(self):
#         return self.email

class Content(models.Model):
    image=models.ImageField(upload_to='images/')
    summary=models.CharField(max_length=400)
    time=models.TimeField(auto_now_add=True)
    # email=User.email

    def __str__(self):
        return self.summary
        


  