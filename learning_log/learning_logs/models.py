from django.db import models

# Create your models here.
class Topic(models.Model):
    text=models.CharField(max_length=200)
    data_added=models.DateTimeField(auto_now_add=True) #Date而不是Data
    def __str__(self):
        return self.text