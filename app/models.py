from django.db import models

# Create your models here.

class FeedBack(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__ (self):
        return self.name
  
class Book_Project(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    topic = models.CharField(max_length=150)
    description= models.TextField()

    def __str__ (self):
        return self.name
  
