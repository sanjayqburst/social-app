from django.contrib.auth.models import User
from django.db import models
from django.contrib.postgres.fields import ArrayField

class Content(models.Model):
    """
    Model for storing content of post created
    """
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.FileField(upload_to='images/')
    summary=models.CharField(max_length=400)
    time=models.TimeField(auto_now_add=True)

    def __str__(self):
        """
        Method to self describe

        Returns:
            Summary text: Gives self description as content summary
        """
        return self.summary
        

class Comments(models.Model):
    """
    Method for creating comments in database.
    """
    commented_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='created_user')
    post_id=models.ForeignKey(Content,on_delete=models.CASCADE,related_name='postrefid')
    comment = models.TextField()
    last_modified = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.comment
